import json
from urllib.request import urlopen
import requests as rq

with urlopen('http://echo.jsontest.com/key/value/one/two') as test:
    ans = test.read()
    # print(ans)

data = json.loads(ans)

print(json.dumps(data, indent=2))