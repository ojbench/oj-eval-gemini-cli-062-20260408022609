import os
import sys
import requests
sys.path.append('submit_acmoj')
from acmoj_client import ACMOJClient

client = ACMOJClient(os.environ.get("ACMOJ_TOKEN"))
try:
    data = {"language": "git", "code": "https://github.com/ojbench/oj-eval-gemini-cli-062-20260408022609.git"}
    response = requests.post(f"{client.api_base}/problem/1336/submit", headers=client.headers, data=data)
    print(response.status_code)
    print(response.text)
except Exception as e:
    print(e)
