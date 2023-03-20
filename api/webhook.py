import requests
import json
import time

webhook_url = 'https://flask-hello-git-main-pythonian1027.vercel.app/webhook'

data = {'name': 'rich'}

r = requests.post(webhook_url, data=json.dumps(data), headers = {'Content-Type': 'application/json'})