import requests
import hashlib
import hmac
import time
import yaml

with open('E:\workspace\config\password.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

api_key = config['binance']['api_key']
api_secret = config['binance']['api_secret']

print(api_key)
print(api_secret)

## 获取时间
# result = requests.request("get","https://api.binance.com/api/v3/time").json()
# print(result)
#
# # 获取k线
# result = requests.request("get","https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m").json()
# print(result)

############################################### 获取账户信息
# timestamp: int = int(time.time() * 1000)
#
# params = {
#     "timestamp": timestamp,
# }
#
# payload: str = "&".join([f"{k}={v}" for k, v in sorted(params.items())])
# signature: str = hmac.new(
#     api_secret.encode(),
#     payload.encode("utf-8"),
#     hashlib.sha256
# ).hexdigest()
#
# headers: dict = {
#             "Content-Type": "application/x-www-form-urlencoded",
#             "Accept": "application/json",
#             "X-MBX-APIKEY": api_key,
#             "Connection": "close"
# }
#
# # 获取时间
# response = requests.request("get",f"https://api.binance.com/api/v3/account?timestamp={timestamp}&signature={signature}",headers=headers)
# print(response.status_code)
# print(response.text)


############################################### 测试获取时间增加TIMESTAMP
timestamp: int = int(time.time() * 1000)

params = {
    "timestamp": timestamp,
}

payload: str = "&".join([f"{k}={v}" for k, v in sorted(params.items())])
signature: str = hmac.new(
    api_secret.encode(),
    payload.encode("utf-8"),
    hashlib.sha256
).hexdigest()

headers: dict = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
            "X-MBX-APIKEY": api_key,
            "Connection": "close"
}

# 请求账户信息
response = requests.request("get",f"https://fapi.binance.com/fapi/v1/time?timestamp={timestamp}&signature={signature}",headers=headers)
print(response.status_code)
print(response.text)
