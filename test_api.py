import requests, re

# session = requests.Session()
# response_1 = requests.get("http://127.0.0.1:8000/api/v1/drf-auth/login/")

# # woman = {"title": "MADINAAAAAAA", "content": "LOREM IPSUUM!", "category": 2}
# # category = {"name": "Ученые"}

# login = {
#     "login-form[username]": "deshruh",
#     "login-form[password]": "tgyhujik1",
#     "login-form[rememberMe]": "0",
#     "csrftoken": "OC68qrM1Ngu2d5UXTlT73Qng0LPlpGxu",
# }
# response = requests.post("http://127.0.0.1:8000/api/v1/drf-auth/login/", data=login)
# print(login)
# print(response.status_code)
# print(response_1.cookies)


# login = {"username": "JoJo2", "password": "tgyhujik1", "email": "test_1@gmail.com"}
# r = requests.post("http://127.0.0.1:8000/api/v1/auth/users/", data=login)

# print(r.text)


# auth = {"username": "JoJo2", "password": "tgyhujik1"}
# r = requests.post("http://127.0.0.1:8000/auth/token/login/", data=auth)

# print(r.text)

headers = {"Authorization": "Token 572c1875f670e7ce67cd365929af7d39e9830663"}
r = requests.get("http://127.0.0.1:8000/api/v1/womenlist/", headers=headers)

print(r.text)
