#Paula Duffy 2018-02-06
#Collatz Conjecture - Week 3 Exercise

n = int(input("Please enter an integer: "))

while n > 1:
  if n % 2 == 0:
    n = n // 2 #divide by 2 if integer is even
    print (n)  
  
  elif n % 2 == 1:
    n = (n * 3) + 1 #multiply by 3 and add 1 if integer is not even
    print (n)
