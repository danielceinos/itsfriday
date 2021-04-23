# -*- coding: utf-8 -*-

import requests
import os
import json, re

webhookUrl = os.environ['WEBHOOK']

headers = {'Content-type': 'application/json'}
payload = {"markdown":"### It's friday then!!\nhttps://www.youtube.com/watch?v=1TewCPi92ro"}
r = requests.post(webhookUrl, headers= headers, data=json.dumps(payload))

print(r)
