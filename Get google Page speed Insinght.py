import requests
api_key = 'AIzaSyBtKokvQa7QEG9_nJOstZvBJGiA4Ykh2ko'
url = 'https://developers.google.com'
api_url = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key={api_key}'
res = requests.get(api_url)

if res.status_code == 200:
    data = res.json()
    cls = data.get('loadingExperience').get('metrics').get('CUMULATIVE_LAYOUT_SHIFT_SCORE').get('percentile')
    print(cls)
else:
    print('Error')