import json
from urllib import request

selectedCity = input('Masukkan nama kota / daerah: ')

url = f"https://goweather.herokuapp.com/weather/{selectedCity}"

# lakukan http request
response = request.urlopen(url)

# parsing data json
data = json.loads(response.read())

print(data)

# lebih rapih

print(f"""
      
= Cuaca {selectedCity} =

{data['description']}
Suhu    : {data['temperature']}    
 
= Prakiraan Suhu 3 hari kedepan =

1 Hari kedepan  : {data['forecast'][0]['temperature']}
2 Hari kedepan  : {data['forecast'][1]['temperature']}
3 Hari kedepan  : {data['forecast'][2]['temperature']}

      """)