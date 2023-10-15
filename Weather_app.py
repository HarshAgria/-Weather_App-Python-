import os
import win32com.client as wincom
import requests
import json
s=wincom.Dispatch("SAPI.SpVoice")
print("Welcome!!\nWhich city weather you want to know? ")
s.Speak("Welcome!! ......... Which city weather you want to know? ")
city=input()
url=f"http://api.weatherapi.com/v1/current.json?key=e0452b5a986b4154a6d81256231405%20&q={city}&aqi=no"
r=requests.get(url)
# print(r.text)
# print(type(r.text))
Wdic=json.loads(r.text)
w=Wdic["current"]["temp_c"]
print(f"The current weather in {city} is {w} degree celcius.")
s.Speak(f"The current weather in {city} is {w} degree celcius............ and more details are shown below.")
print()
print()
print(r.text)


