import requests
import math

#############################
# Functions
# A utility function that returns true if x is perfect square

def isHelloWorld(x):
    if (x == "Hello World"):
        return print ("Hello World: ", True)
    else: return print ("Hello World: ", False)

def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x

def isPrime(n):
    # Corner case
    if (n <= 1):
        return print ("Prime: ", False)
 
    # Check from 2 to n-1
    for i in range(2, n):
        if (n % i == 0):
            return print ("Prime: ", False)
    else: return print ("Prime: ", True)

def isFactorial(n):
    if (n == 0):
        return print ("Factorial: ", True)
    elif (n < 0):
        return print ("Factorial: ", False)
    else:
        for i in range(1, n):
            if (n % i == 0):
                return print ("Factorial: ", False)
        else: return print ("Factorial: ", True)

# Returns true if n is a Fibonacci Number, else false
def isFibonacci(n):
 
    # n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perfect square
    b=isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)
    return print ("Fibonacci: ", b)


    

BASE = "http://0.0.0.0:4000"                                     #local host:port declared to connect with API


#############################
# md5 test 

response = requests.get(BASE + "/md5/Hello World")               #sends URI to API
data = response.json()                                           #sets data as the json output
print(data)                                                      #prints output
isHelloWorld(data)                                               #calls function to test if output is correct


#############################
# Factorial test

response = requests.get(BASE + "/factorial/4")
data = response.json()
isFactorial(data)


response = requests.get(BASE + "/factorial/0")
data = response.json()
isFactorial(data)


#############################
# Is-prime test

response = requests.get(BASE + "/is-prime/10")
data = response.json()
isPrime(data)


response = requests.get(BASE + "/is-prime/7")
data = response.json()
isPrime(data)


response = requests.get(BASE + "/is-prime/1")
data = response.json()
isPrime(data)


#############################
# Fibonacci test

response = requests.get(BASE + "/fibonacci/20")
data = response.json()
isFibonacci(data)


response = requests.get(BASE + "/fibonacci/100")
data = response.json()
isFibonacci(data)

response = requests.get(BASE + "/fibonacci/0")
data = response.json()
isFibonacci(data)

response = requests.get(BASE + "/fibonacci/200")
data = response.json()
isFibonacci(data)

response = requests.get(BASE + "/fibonacci/500")
data = response.json()
isFibonacci(data)

#############################
# Slack-Alert Test

#response = requests.get(BASE + "/slack-alert/2nd Test")
#data = response.json()
