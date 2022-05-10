import os
import json
from urllib import request
from urllib.request import Request, urlopen
from urllib.parse import unquote, urlparse, quote_plus
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.config.settings")
django.setup()

# from apps.projects.models import Project


UUID = os.environ.get("UUID")
url = f"https://api.odcloud.kr/api/3074271/v1/uddi:{UUID}"

# init params
API_KEY = os.environ.get("API_KEY")
PAGE = 1
PERPAGE = 50
URL = url + f"?page={PAGE}&perPage={PERPAGE}&serviceKey={API_KEY}"

req = Request(url)
req.add_header("accept", "application/json")
req.add_header("Authorization", API_KEY)
# print(req)

body = urlopen(req, timeout=60).read()
# print(body)

decode_data = body.decode('utf-8')
print(decode_data)
