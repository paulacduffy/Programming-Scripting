#Paula Duffy 2018-02-06
#Collatz Conjecture - Week 3 Exercise

n = int(input("Please enter an integer: "))

n = 17
while n > 1:
  if n % 2 == 0:
    n = n // 2
    print (n)  
  
  elif n % 2 == 1:
    n = (n * 3) + 1
    print (n)
