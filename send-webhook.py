# -*- coding: utf-8 -*-

import requests
import json, re

webhookUrl = "https://webexapis.com/v1/webhooks/incoming/Y2lzY29zcGFyazovL3VzL1dFQkhPT0svYWQ3YmFmYzMtMDQ2Yy00YTRjLThlNmEtZjA5NWJiYjYzMzZj"

headers = {'Content-type': 'application/json'}
payload = {"markdown":"https://www.youtube.com/watch?v=1TewCPi92ro"}
r = requests.post(webhookUrl, headers= headers, data=json.dumps(payload))
