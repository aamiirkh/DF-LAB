#!/usr/bin/env python3

import requests
import json

url = "https://ipstack.com/?utm_source=any-api&utm_medium=OwnedSites"
payload = {'Query': 'xss'}

response = requests.get(url, params=payload)
json_response = response.json()

print(json.dumps(json_response))