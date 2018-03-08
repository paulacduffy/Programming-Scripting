#Paula Duffy 07-03-2018
#Exercise 6 - Functions

def factorial(x):
    n = 1
    while x >= 1:
        n = n * x
        x = x - 1
    return n

print ("The factorial of 7 is:", factorial(7))
print ("The factorial of 5 is:", factorial(5))
print ("The factorial of 10 is:", factorial(10))
