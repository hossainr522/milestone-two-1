import requests

user_api = 'https://api.ipify.org/?format=json'
response = requests.get(user_api)
# print(response.status_code)
# print(response.json())
if response.status_code == 200:
    data = response.json()
    ip_address = data.get('ip')
    print('Your Ip address is: ',ip_address)