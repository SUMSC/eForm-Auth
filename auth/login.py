import requests
import jwt
import json
from datetime import datetime, timedelta

url = 'http://ids1.suda.edu.cn/amserver/UI/Login?goto=http://myauth.suda.edu.cn/default.aspx?app=eform&gx_charset=UTF-8'
headers = {"Content-Type": "application/x-www-form-urlencoded"}
body = "IDToken1={}&IDToken2={}"


def dologin(data: dict, secret: str) -> (bool, dict):
    id = data['id']
    token = data['token']
    resp = requests.post(url=url, headers=headers, data=body.format(id, token))
    res = resp.text

    if res.strip()[0] == '<':
        return False, "Login Failed"
    else:
        data = json.loads(res)['data']
        data['exp'] = datetime.utcnow() + timedelta(days=3)
        print(secret)
        return True, jwt.encode(payload=data, key=secret, algorithm='HS256').decode('utf8')
