import requests


cookie = {
    "visit-month":"May"
}
res = requests.get('http://rahulshettyacademy.com', allow_redirects=False, cookies=cookie, timeout=1)
# res = requests.get('http://github.com/', allow_redirects=False, timeout=1, cookies=cookie)
# 301, 200
print("res =",res.status_code)

cookie2 = {
    "visit-year":"2024"
}
session = requests.session()
session.cookies.update(cookie)
# res2 = requests.get("https://httpbin.org/cookies", cookies=cookie2)
res2 = session.get("https://httpbin.org/cookies", cookies=cookie2)
print("res2 =",res2.status_code)
print(res2.text)

