# coding: UTF-8
import urllib.request
import json

headers = {"Content-Type" : "application/json","Authorization": "Bearer {BOT USER OAUTH TOKEN}"}

# Enjigraph APIから最新情報を取得
url = "https://api.enji-graph.com/v1/data?q=ChatGPT&lang=ja&filter=domainAuthority&num=10"

req = urllib.request.Request(url)
req.add_header("X-ENJI-API-KEY",{ENJIGRAPH API KEY})

with urllib.request.urlopen(req) as res:
    body = json.loads(res.read())

    # Slackへ投稿
    for information in body["data"]:
        obj = {
            "channel":{CHANNEL ID},
            "text":information["url"]
        }

        json_data = json.dumps(obj).encode('utf-8')

        request = urllib.request.Request("https://slack.com/api/chat.postMessage", data=json_data, method="POST", headers=headers)
        with urllib.request.urlopen(request) as response:
            response_body = response.read().decode('utf-8')
            jsonData = json.loads(response_body)
            print(jsonData)
