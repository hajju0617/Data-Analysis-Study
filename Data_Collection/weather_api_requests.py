import requests
import json

url = 'https://api.open-meteo.com/v1/forecast?'
params = {
    'latitude' : '35.87988',
    'longitude' : '128.6286',
    'current' : 'temperature_2m'
}

try:
    response = requests.get(url, params = params, timeout = 5)
    response.raise_for_status()

    data = response.json()
    print('API 응답 : ', data)
    print(f"동대구역의 현재 온도는 : {data['current']['temperature_2m']}{data['current_units']['temperature_2m']} 입니다.")
except requests.exceptions.RequestException as e:
    print(f'API 호출 실패 : {e}')
except json.JSONDecodeError as e:
    print(f'JSON 파싱 실패 : {e}')