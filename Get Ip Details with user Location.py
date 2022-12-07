from requests import get

ip_api = 'https://api.ipify.org/?format=json'
my_ip = get(ip_api)
if my_ip.status_code == 200:
    data = my_ip.json()
    ip = data.get('ip')


loc = f'http://ipwho.is/{ip}'
user_details_get = get(loc)
if user_details_get.status_code == 200:
    user_details = user_details_get.json()
    city = user_details.get('city')
    region_code = user_details.get('region_code')
    country_name = user_details.get('country')

sentence = f'Ip {ip} is located in {city} {region_code}, {country_name}.'
print(sentence)