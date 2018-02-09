# A program that displays Fibonacci numbers using people's names.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Duffy"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

# Week 1 
# My name is Paula, so the first and last letter of my name (P + A = 16 + 1) give the number 17. The 17th Fibonacci number is 1597.
# Week 2
# My surname is Duffy
#The first letter D is number 68
#The last letter y is number 121
#Fibonacci number 189 is 1409869790947669143312035591975596518914
#Ord() returns an integer representing the unicode code point for the given character
