import requests

r = requests.get("https://imgs.xkcd.com//comics//timeline_of_the_universe.png")
print(r)
print(r.status_code)
f = open("D:\\python\\Akshay\\api\\sample.png","wb")
f.write(r.content)
print(r.content)
f.close()
