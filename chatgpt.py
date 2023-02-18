import os
import json
from revChatGPT.V1 import Chatbot

from dotenv import load_dotenv


load_dotenv()


with open(os.environ["CONFIG_FILE_PATH"]) as f:
    chatgpt_config = json.load(f)

def ChatGPT(prompt, conversation_id=None, parent_id=None):
    chatbot = Chatbot(config=chatgpt_config)
    response = {"message": "ChatGPT is at capacity right now",
               "conversation_id": None,
               "parent_id": None}
    try:
        res = list(chatbot.ask(prompt, 
                               conversation_id=conversation_id, 
                               parent_id=parent_id))
        
        if isinstance(res, list) and res:
            response = res[-1]
    except:
        pass

    return response
