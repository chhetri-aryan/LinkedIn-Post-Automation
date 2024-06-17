import requests
import json

url = "https://api.linkedin.com/v2/userinfo"

headers = {
    'Authorization': 'Bearer AQV5Z8lmiTsIYjmO8isWHvYwJChaIhczx6YLvLF8P6AhtO-p_aC1vjq4XWEpVm8gn4E36-9kewnbzRaP12U_P37wlVhdTlYznQ5wJ1xO4hP22MLdcJjCSK3-W3G0ntZzdUxjdiVXhsu5DJ0Kz1j-162uJpznS-bfs4eOrPmYuay4ZOKUaEwcuhuUgGwkYcbfT5RzGh5U92lYC4LtU-GiulT8eUWxpy9i9_fe-A2AWX1OJMcFG_2lCUb9CBfx20K8lqmgHlW5280Izi5hcqQZNrOOSHza5fEx7br4R0x201LF243GTm5AFsTAENijrwEo5rL1YStjspvHNYt6IOBuP_SiBvJmDg',
    'X-Restli-Protocol-Version': '2.0.0'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    user_data = response.json()
    print(json.dumps(user_data, indent=2))
else:
    print(f"Error: {response.status_code} - {response.text}")
