import requests


errors = 0

#############################
# md5 test 

response = requests.get("http://localhost:4000/md5/Hello World")
data = response.json()
if response.status_code == 200:
    print("Test Passed")
else:
    print("Test Failed")
    errors += 1

response = requests.get("http://localhost:4000/md5/    white   space")
data = response.json()
if response.status_code == 200:
    print("Test Passed")
else:
    print("Test Failed")
    errors += 1

response = requests.get("http://localhost:4000/md5/37258943570265410")
data = response.json()
if response.status_code == 200:
    print("Test Passed")
else:
    print("Test Failed")
    errors += 1

response = requests.get("http://localhost:4000/md5/String_Value")
data = response.json()
if response.status_code == 200:
    print("Test Passed")
else:
    print("Test Failed")
    errors += 1

response = requests.get("http://localhost:4000/md5/GROUP4 TEST CASES")
data = response.json()
if response.status_code == 200:
    print("Test Passed")
else:
    print("Test Failed")
    errors += 1


#############################
# factorial test 

response = requests.get("http://localhost:4000/factorial/HelloWorld")
data = response.json()
if response.status_code == 200:
    print("Test Passed")
else:
    print("Test Failed")
    errors += 1

response = requests.get("http://localhost:4000/factorial/123553")
data = response.json()
if response.status_code == 200:
    print("Test Passed")
else:
    print("Test Failed")
    errors += 1

response = requests.get("http://localhost:4000/factorial/   white space  ")
data = response.json()
if response.status_code == 200:
    print("Test Passed")
else:
    print("Test Failed")
    errors += 1

response = requests.get("http://localhost:4000/factorial/true")
data = response.json()
if response.status_code == 200:
    print("Test Passed")
else:
    print("Test Failed")
    errors += 1

response = requests.get("http://localhost:4000/factorial/stringvalue")
data = response.json()
if response.status_code == 200:
    print("Test Passed")
else:
    print("Test Failed")
    errors += 1

#############################
# fibonacci test 

response = requests.get("http://localhost:4000/fibonacci/2355463")
data = response.json()
if response.status_code == 200:
    print("Test Passed")
else:
    print("Test Failed")
    errors += 1

response = requests.get("http://localhost:4000/fibonacci/Hello World")
data = response.json()
if response.status_code == 200:
    print("Test Passed")
else:
    print("Test Failed")
    errors += 1

response = requests.get("http://localhost:4000/fibonacci/     white  space  ")
data = response.json()
if response.status_code == 200:
    print("Test Passed")
else:
    print("Test Failed")
    errors += 1

response = requests.get("http://localhost:4000/fibonacci/-239402548032")
data = response.json()
if response.status_code == 200:
    print("Test Passed")
else:
    print("Test Failed")
    errors += 1

response = requests.get("http://localhost:4000/fibonacci/-0")
data = response.json()
if response.status_code == 200:
    print("Test Passed")
else:
    print("Test Failed")
    errors += 1

#############################
# is prime test 

response = requests.get("http://localhost:4000/is-prime/Hello World")
data = response.json()
if response.status_code == 200:
    print("Test Passed")
else:
    print("Test Failed")
    errors += 1

response = requests.get("http://localhost:4000/is-prime/32478329481")
data = response.json()
if response.status_code == 200:
    print("Test Passed")
else:
    print("Test Failed")
    errors += 1

response = requests.get("http://localhost:4000/is-prime/         White Space    ")
data = response.json()
if response.status_code == 200:
    print("Test Passed")
else:
    print("Test Failed")
    errors += 1

response = requests.get("http://localhost:4000/is-prime/stringvalue")
data = response.json()
if response.status_code == 200:
    print("Test Passed")
else:
    print("Test Failed")
    errors += 1

response = requests.get("http://localhost:4000/is-prime/true")
data = response.json()
if response.status_code == 200:
    print("Test Passed")
else:
    print("Test Failed")
    errors += 1

#############################
# slack alert 

response = requests.get("http://localhost:4000/slack-alert/Post this string into our Slack Channel to test API functionality")
data = response.json()
if response.status_code == 200:
    print("Test Passed")
else:
    print("Test Failed")
    errors += 1


def noErrors():
    return 0

if errors == 0:
    noErrors()
else:
    print("You have errors within your API. Edit accordingly and rerun test file!")



