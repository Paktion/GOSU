import requests
import json

x = requests.get('https://content.osu.edu/v2/bus/routes/CC')

print(x.text)