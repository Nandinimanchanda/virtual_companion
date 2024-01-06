import os
import  openai

openai.apikey = os.getenv("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")

inp = "iron man in air"
res = openai.Image.create(prompt=inp,n=1,size="1024x1024")

url = res['data'][1]['url']
print(url)