import json
import os 
import gpt4free
from gpt4free import Provider, you
from urllib import request

LOCATION_KEY = {
    "jakarta": "208971",
    "alaska": "3379406"
}

def fn_getCurrTemp(_lockey):
    # API link goes here
    _url = f"http://dataservice.accuweather.com/currentconditions/v1/{_lockey}?apikey=sRSVVDA3Po6BD3eLipEH4PZ4XZdq690A&details=true"
    _response = request.urlopen(_url)
    _data = json.loads(_response.read())
    return _data[0]['Temperature']['Metric']['Value']

def fn_getAdvice(_mode):
    _chat = []
    _response = you.Completion.create(
        prompt=f'how to keep your health at {_mode} temperature',
        chat=_chat)

    return _response.text


# Start
print("""
= Your Health Advisor =
Powered by AccuWeather and gpt4free
Script by Harahap      
      """)
selectedLoc = input("Input location: ")
currTemp = fn_getCurrTemp(LOCATION_KEY[f'{selectedLoc}'])
print(f"Current temperature: {currTemp} C")

#currTemp = 24
#print(f"Current temperature: {currTemp} C")

print("You AI reccomendation:")

if(currTemp > 24):
    while (True):
        respond = fn_getAdvice("hot")
        print(respond)
        if(respond != "Unable to fetch the response, Please try again."):
            break
else:
    while (True):
        respond = fn_getAdvice("cold")
        print(respond)
        if(respond != "Unable to fetch the response, Please try again."):
            break
