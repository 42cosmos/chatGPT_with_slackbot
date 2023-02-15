import json
from revChatGPT.V1 import Chatbot


with open("/home/eunbinpark/.config/revChatGPT/config.json") as f:
    chatgpt_config = json.load(f)

def ChatGPT(prompt):
    chatbot = Chatbot(config=chatgpt_config)

    response = ""

    for data in chatbot.ask(prompt):
        response = data["message"]

    return response