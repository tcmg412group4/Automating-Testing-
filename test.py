import requests

BASE = "http://127.0.0.1:4000"                                  #local host


#############################
# md5 test 

response = requests.get(BASE + "/md5/Hello World")              #sends URI to API
data = response.json()                                          #sets data as the json output
print(data)                                                     #prints output

input()                                                          # pauses script when running it, press enter to print out the next statement

#############################
# Factorial test

response = requests.get(BASE + "/factorial/4")
data = response.json()
print(data)

input() 

response = requests.get(BASE + "/factorial/0")
data = response.json()
print(data)

input()

#############################
# Is-prime test

response = requests.get(BASE + "/is-prime/10")
data = response.json()
print(data)

input()

response = requests.get(BASE + "/is-prime/7")
data = response.json()
print(data)

input() 

response = requests.get(BASE + "/is-prime/1")
data = response.json()
print(data)

#############################
# Fibonacci test

response = requests.get(BASE + "/fibonacci/20")
data = response.json()
print(data)

input()

response = requests.get(BASE + "/fibonacci/100")
data = response.json()
print(data)

input()

response = requests.get(BASE + "/fibonacci/0")
data = response.json()
print(data)

#############################
# Slack-Alert Test

response = requests.get(BASE + "/slack-alert/2nd Test")
data = response.json()
print(data)
