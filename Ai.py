import requests

api_url = 'https://api.linkedin.com/v2/ugcPosts'


headers = {
    'Authorization': f'Bearer AQV5Z8lmiTsIYjmO8isWHvYwJChaIhczx6YLvLF8P6AhtO-p_aC1vjq4XWEpVm8gn4E36-9kewnbzRaP12U_P37wlVhdTlYznQ5wJ1xO4hP22MLdcJjCSK3-W3G0ntZzdUxjdiVXhsu5DJ0Kz1j-162uJpznS-bfs4eOrPmYuay4ZOKUaEwcuhuUgGwkYcbfT5RzGh5U92lYC4LtU-GiulT8eUWxpy9i9_fe-A2AWX1OJMcFG_2lCUb9CBfx20K8lqmgHlW5280Izi5hcqQZNrOOSHza5fEx7br4R0x201LF243GTm5AFsTAENijrwEo5rL1YStjspvHNYt6IOBuP_SiBvJmDg',
    'Connection': 'Keep-Alive',
    'Content-Type': 'application/json',
}

post_body = {
    'author': 'urn:li:person:wuBUO-iIh3',
    'lifecycleState': 'PUBLISHED',
    'specificContent': {
        'com.linkedin.ugc.ShareContent': {
            'shareCommentary': {
                'text': 'Check out our latest blog post!',
            },
            'shareMediaCategory': 'ARTICLE',
            'media': [
                {
                    'status': 'READY',
                    'description': {
                        'text': 'Read our latest blog post about LinkedIn API!',
                    },
                    'originalUrl': '<your_blog_post_url>',
                },
            ],
        },
    },
    'visibility': {
        'com.linkedin.ugc.MemberNetworkVisibility': 'PUBLIC',
    },
}

response = requests.post(api_url, headers=headers, json=post_body)
if response.status_code == 201:
    print('Post successfully created!')
else:
    print(f'Post creation failed with status code {response.status_code}: {response.text}')
