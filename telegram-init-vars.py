import requests

token = 'TOKEN HERE'

url = f'https://api.telegram.org/bot{token}/getUpdates'

response = {}

response = requests.post(url).json()['result'][-1]
print(response['message']['from']['id'])
