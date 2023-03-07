import requests


BASE = "http://0.0.0.0:4000"                                  #local host:port declared to connect with API


#############################
# md5 test 

response = requests.get(BASE + "/md5/Hello World")              #sends URI to API
data = response.json()                                          #sets data as the json output
print(data)                                                     #prints output

#############################
# Factorial test

response = requests.get(BASE + "/factorial/4")
data = response.json()



response = requests.get(BASE + "/factorial/0")
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
# Fibonacci test

response = requests.get(BASE + "/fibonacci/20")
data = response.json()


response = requests.get(BASE + "/fibonacci/100")
data = response.json()


response = requests.get(BASE + "/fibonacci/0")
data = response.json()


response = requests.get(BASE + "/fibonacci/200")
data = response.json()


response = requests.get(BASE + "/fibonacci/500")
data = response.json()

#############################
# Slack-Alert Test

#response = requests.get(BASE + "/slack-alert/2nd Test")
#data = response.json()
