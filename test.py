import requests

BASE = "http://0.0.0.0:4000"                                  #local host:port declared to connect with API


#############################
# md5 test 

response = requests.get(BASE + "/md5/Hello World")              #sends URI to API
data = response.json()                                          #sets data as the json output
                                              
response = requests.get(BASE + "/md5/   ")             
data = response.json()  

response = requests.get(BASE + "/md5/^*&#^#*$#")             
data = response.json()  

response = requests.get(BASE + "/md5/test_case-354_324532_-=")             
data = response.json()  

response = requests.get(BASE + "/md5/blank     space")             
data = response.json()  

response = requests.get(BASE + "/md5/1247893574389725802543")             
data = response.json()  

response = requests.get(BASE + "/md5/mvdbmnbsjbn . bjk.g nr n")             
data = response.json()  

response = requests.get(BASE + "/md5/Test Cases Above were generated using random characters from keyboard")             
data = response.json()  

#############################
# Factorial test

response = requests.get(BASE + "/factorial/4")
data = response.json()

response = requests.get(BASE + "/factorial/00")
data = response.json()

response = requests.get(BASE + "/factorial/words")
data = response.json()

response = requests.get(BASE + "/factorial/blank   space   ")
data = response.json()

response = requests.get(BASE + "/factorial/true")
data = response.json()

response = requests.get(BASE + "/factorial/false")
data = response.json()

response = requests.get(BASE + "/factorial/-345682934")
data = response.json()

response = requests.get(BASE + "/factorial/Test cases above were randomly generated.")
data = response.json()

#############################
# Is-prime test

response = requests.get(BASE + "/is-prime/10")
data = response.json()

response = requests.get(BASE + "/is-prime/7")
data = response.json()

response = requests.get(BASE + "/is-prime/1")
data = response.json()

#############################
### Fibonacci test

response = requests.get(BASE + "/fibonacci/20")
data = response.json()

response = requests.get(BASE + "/fibonacci/100")
data = response.json()

response = requests.get(BASE + "/fibonacci/0")
data = response.json()

#############################
##### Slack-Alert Test

#response = requests.get(BASE + "/slack-alert/2nd Test")
#data = response.json()
