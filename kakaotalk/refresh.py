import json
import requests

url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type" : "refresh_token",
    "client_id"  : "193e6096885cfe6b68342fc258676cfd",
    "refresh_token" : "<refresh token을 입력하세요>"
}
response = requests.post(url, data=data)

print(response.json())