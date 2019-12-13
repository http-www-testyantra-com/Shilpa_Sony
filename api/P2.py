#TO GET JSON DATA
import requests
import json
parm = {"page":2, "count":4}
r = requests.get("http://httpbin.org/get"\
                 ,params=parm)
print(r.status_code)
print(r.text,type(r.text))
json_data = json.loads(r.text)
print(r.json())
print(json_data)
print(type(json_data))
print(r.json(), type(r.json()))