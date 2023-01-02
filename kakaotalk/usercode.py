import requests
import json
# access token, refresh_token 등 받는 코드

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : "193e6096885cfe6b68342fc258676cfd",
    "redirect_uri" : "https://localhost.com",
    "code"         : "3FDR7xs2dMQMfo-bqxJLZnnts5h5gOdRJH7ZTgs4JffG6kD4j5Llxd0E7kjWdg-d2Yussgo9c04AAAGFcF9v0g"
    
}
response = requests.post(url, data=data)

tokens = response.json()

print(tokens)

with open("./kakao_token.json", "w") as fp:
    json.dump(tokens, fp)

