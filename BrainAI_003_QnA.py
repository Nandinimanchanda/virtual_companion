#open ai
fileopen = open("E:\\nanni\\asnanni\\nanni phone\\skivvy\\AI_JARVIS-20230131T094340Z-001\\AI_JARVIS\\Data\\apikey.txt","r")
API = fileopen.read()
fileopen.close()
print(API)

import openai
from dotenv import load_dotenv

#coding

openai.api_key = API
load_dotenv()
completion = openai.Completion()

def QnA(question,chat_log = None):
    Filelog = open("E:\\nanni\\asnanni\\nanni phone\\skivvy\\AI_JARVIS-20230131T094340Z-001\\AI_JARVIS\\Database\\chat_log_003_QnA.txt","r")
    chat_log_template = Filelog.read()
    Filelog.close()
    
    if chat_log is None:
        chat_log = chat_log_template
        
    prompt = f'{chat_log}You : {question}\nskivvy : '
    response = completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0)
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nYou : {question} \nskivvy : {answer}"
    Filelog = open("E:\\nanni\\asnanni\\nanni phone\\skivvy\\AI_JARVIS-20230131T094340Z-001\\AI_JARVIS\\Database\\chat_log_003_QnA.txt","w")
    Filelog.write(chat_log_template_update)
    Filelog.close()
    return answer

# while True: 
#     kk = input("Enter : ")  
#     print(ReplyBrain(kk))  
    
    