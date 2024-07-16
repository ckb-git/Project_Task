import requests


# base_url= "https://reqres.in"
# end_url= "/api/users?page=2"
# resp=requests.get(base_url+end_url)
resp=requests.get("https://reqres.in/api/users?page=2")
code= resp.status_code
print(code)
print(type(code))
assert code==200 ,"code not match"