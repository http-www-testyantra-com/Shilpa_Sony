#USING POST
import requests
import json
parm = {"useranme" :"corey","password":"testing"}
r = requests.get("http://httpbin.org/post",data=parm)
print(r.status_code)
print(r.text)

