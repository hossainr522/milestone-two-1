from requests import get

def res_data(url):
    my_ip = get(url)
    if my_ip.status_code == 200:
        data = my_ip.json()
    return data


ip_api = 'https://api.ipify.org/?format=json'
data = res_data(ip_api)
ip = data.get('ip')

loc = f'http://ipwho.is/{ip}'
user_details = res_data(loc)
city = user_details.get('city')
region_code = user_details.get('region_code')
country_name = user_details.get('country')

sentence = f'Ip {ip} is located in {city} {region_code}, {country_name}.'
print(sentence)