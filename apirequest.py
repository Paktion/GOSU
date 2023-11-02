import requests
import json

json.loads(requests.get('https://content.osu.edu/v2/bus/routes/CC').text)