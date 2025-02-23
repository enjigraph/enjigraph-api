import urllib.request
import urllib.parse
import json
import openai

openai.api_key = {OPENAI API KEY}

# Enjigraph APIから最新情報を取得
url = "https://api.enjigraph.com/v1/data?q="+urllib.parse.quote("自動運転")+"&lang=ja"
req = urllib.request.Request(url)
req.add_header("X-ENJI-API-KEY",{ENJIGRAPH API KEY})

with urllib.request.urlopen(req) as res:
    body = json.loads(res.read())

    # OpenAI APIに、質問文と最新情報を送信し、回答を生成
    information = ""
    for data in body["data"]:
        information += "title:"+str(data["title"])+" description:"+str(data["description"])+"\n"
    
    role = """
    #命令文
    あなたは、プロのリサーチャーです。
    以下の制約条件と質問をもとに的確な解答を出力してください
    
    #制約条件
    ・初心者でもわかりやすく
    ・重要なキーワードを抜けもれなく含める
    ・具体的な事例・事実を含める
    ・できるだけ最新の情報に基づく

    #質問
    規模言語モデルの開発はどこまで進んでいる？
    
    #解答
    大規模言語モデルの開発は現在、OpenAIやGoogle、Microsoftを筆頭に開発が進められています。つい最近、OpenAIは法人向けサービスを開始しています。
    """

    question = """
    #命令文
    あなたは、プロのリサーチャーです。
    以下の制約条件と質問をもとに的確な解答を出力してください
    
    #制約条件
    ・初心者でもわかりやすく
    ・重要なキーワードを抜けもれなく含める
    ・具体的な事例・事実を含める
    ・できるだけ最新の情報に基づく
    ・次の情報も加味する
    """+information+"""

    #質問
    自動運転はどこまで開発が進んでいる？
    """
    
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role":"system","content":role},{"role":"user","content":question}])
    print(completion.choices[0].message.content)
