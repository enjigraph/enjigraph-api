# coding: UTF-8
import urllib.request
import urllib.parse
import json
import openai

openai.api_key = {OPENAI API KEY}

# Enjigraph APIから最新情報を取得
url = "https://api.enji-graph.com/v1/data?q="+urllib.parse.quote("自動運転")+"&lang=ja&filter=domainAuthority"
req = urllib.request.Request(url)
req.add_header("X-ENJI-API-KEY",{ENJIGRAPH API KEY})

with urllib.request.urlopen(req) as res:
    body = json.loads(res.read())

    # OpenAI APIに、質問文と最新情報を送信し、回答を生成
    information = ""
    for data in body["data"]:
        information += "title:"+str(data["title"])+" description:"+str(data["description"])+"\n"
    
    role = "The following is a conversation with a assistant and a manager. manager: 大規模言語モデルの開発はどこまで進んでいる？最新情報に基づいて教えて。 assistant: 大規模言語モデルの開発は現在、OpenAIやGoogle、Microsoftを筆頭に開発が進められています。つい最近、OpenAIは法人向けサービスを開始しています。"
    question = "自動運転はどこまで開発が進んでいる？次の情報も加味して教えて。"+information
    
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role":"system","content":role},{"role":"user","content":question}])
    print(completion.choices[0].message.content)
