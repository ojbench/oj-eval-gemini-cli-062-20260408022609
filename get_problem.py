import os
import requests
token = os.environ.get("ACMOJ_TOKEN")
headers = {"Authorization": f"Bearer {token}"}
response = requests.get("https://acm.sjtu.edu.cn/OnlineJudge/api/v1/problem/1336", headers=headers)
print(response.json())
