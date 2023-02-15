import re
import os
from dotenv import load_dotenv

from slack import RTMClient
from chatgpt import ChatGPT


load_dotenv()

# 발급받은 슬랙 bot user token 기
bot_token = os.environ["SLACK_BOT_TOKEN"]
BOT_ID = os.environ["BOT_ID"]
bot_id_regex = r"\<\@[A-Z0-9]+\>\s*"



def chatgpt_to_slack(text, channel_id, message_ts):
    response = ChatGPT(text)
    # 슬랙에 메세지 전달
    web_client.chat_postMessage(channel=channel_id, text=response, thread_ts=message_ts)

    
def remove_user_id_in_text(text):
    global bot_id_regex
    return re.sub(bot_id_regex, "", text).strip()


def extract_bot_id_in_text(text):
    global bot_id_regex
    global BOT_ID
    extracted_id = re.findall(bot_id_regex, text)[0].strip()
    
    return True if extracted_id == f"<@{BOT_ID}>" else False
    

# 지속적으로 슬랙 메세지 트래킹
@RTMClient.run_on(event="message")
def chatgptbot(**payload):    
    data = payload["data"]
    web_client = payload["web_client"]
    
    bot_id = data.get("bot_id", "")
    subtype = data.get("subtype", "")
    origin_text = data.get("text", "")
    
    # tag_code = origin_text.split(" ")[0]
    print(data)
    # 유저가 봇을 호출한 경우인지 확인 
    is_this_bot_calling = extract_bot_id_in_text(origin_text)

    # Bot이 입력한 채팅이 아닐 경우 ChatGPT 동작
    
    # bot_id: bot의 답장인 경우 값이 할당됨
    # subtype: bot의 답장인 경우- "bot_message", 
    # subtype: 사용자의 첫 스레드 답글일 경우 - "message_replied"
    
    if bot_id == "" and subtype == "" and is_this_bot_calling:
        # Extracting message send by the user on the slack
        text = remove_user_id_in_text(origin_text)
        
        # thread_ts: 해당 메세지 입력 시간을 파악하여 답글을 달 수 있도록 지정
        #받아온 텍스트를 ChatGPT에 전달하고 ChatGPT의 답변 저장
        response = ChatGPT(text)
        web_client.chat_postMessage(channel=data["channel"], text=response, thread_ts=data["ts"])
        

if __name__ == "__main__":
    try:
        # RTM 클라이언트 호출 및 시작
        rtm_client = RTMClient(token=bot_token)
        print("Starter Bot connected and running!")
        rtm_client.start()
    except Exception as err:
        print(err)
