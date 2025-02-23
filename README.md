# Enjigraph API
Enjigraphが収集している記事やプレスリリース、ブログなどの情報を取得することができるAPIです。

↓ Enjigraph  
https://www.enjigraph.com/

↓ Enjigraph API  
https://www.enjigraph.com/api

## レスポンスデータ
下記情報をJSON形式で取得できます。  
・タイトル  
・概要  
・URL  
・公開日  

## 利用方法
headerにAPI KEYを埋め込み、GETリクエストを送信するだけで簡単にデータを取得できます。

cURLを使った例:
```
curl -H 'X-ENJI-API-KEY : {API KEY}' https://api.enjigraph.com/v1/data
```

## リクエストパラメーター
| パラメーター | デフォルト | 概要 |
| ---- | ---- | ---- |
| q | null | 検索キーワードを指定してください。必須パラメータになります。 |
| num | 100 | 取得する情報数を指定できます。<br>デフォルトは100、最大は100です。 |
| from | null | 取得する情報の公開日の範囲を指定できます。<br>最も古い公開日を指定できます。(ISO 8601形式)<br><br>qとfilterを同時に指定した場合、fromは指定できません。 |
| to | null | 取得する情報の公開日の範囲を指定できます。<br>最も新しい公開日を指定できます。(ISO 8601形式)<br><br>qとfilterを同時に指定した場合、toは指定できません。 |
| sortOrder | desc | 情報の並び替えを指定できます。<br>昇順にする場合は「asc」を、降順にする場合は「desc」を指定してください。<br>現在、情報は公開日によって並び替えられています。<br><br>qとfilterを同時に指定した場合、sortOrderは指定できません。  |
| lang | 日本語と英語 | 取得する情報の言語を指定できます。<br>「ja」あるいは「en」が指定できます。 | 
| domains | null | 取得する情報のドメインを指定できます。<br>複数ドメインを指定したい場合は、domains=www.enjigraph.com,blog.enjigraph.com のように、カンマ区切りで列挙してください。<br><br>※filterとの併用はできません。 |

cURLを使った例:
```
curl -H 'X-ENJI-API-KEY : {API KEY}' 'https://api.enjigraph.com/v1/data?q=AI&num=50&from=2023-08-01&to=202308-20'
```

Pythonを使った例:
```
import requests

url = "https://api.enjigraph.com/v1/data"

headers = {
    'X-ENJI-API-KEY' : {API KEY}
}

params = {
    "q": "AI",
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    json_data = response.json()
    print("成功:", json_data)
else:
    print("失敗:", response.status_code)
```

レスポンス例（成功）:
```
{
    status: "success",
    data: [
        {
           url: "https://www.enjigraph.com/blog/20211123",
           title: "【米国株】NVIDIAが、AI時代に一人勝ちする理由と最新の株価とは？",
           description: "今回は、AI時代に、最も注目されている企業「エヌビディア（NVIDIA）」を、紹介したいと思います。",
           datePublished:"2021-11-23 00:00:00",
           lang: "ja"
        }
    ],
    totalResults: 100,
    monthlyLimit: 10000,
    monthlyRequestCount: 980
}
```

レスポンス例（エラー）:
```
{
    status: "error",
    code: MonthlyRequestLimit,
    message: Monthly request limit exceeded. Please upgrade your plan.
}
```

## エラーコード
- apiKeyMissing  
　API KEYがヘッダーに付与されていません。
- apiKeyInvalid  
　API KEYが正しくありません。
- MonthlyRequestLimit  
　月間リクエスト数がプラン上限を超えています。
- MonthlyRequestLimit  
　月間リクエスト数がプラン上限を超えています。
- BadRequest  
　検索キーワードを設定してください。



