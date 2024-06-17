import requests
import json

url = "https://api.linkedin.com/v2/userinfo"

headers = {
    'Authorization': '1',
    'X-Restli-Protocol-Version': '2.0.0'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    user_data = response.json()
    print(json.dumps(user_data, indent=2))
else:
    print(f"Error: {response.status_code} - {response.text}")
