#Paula Duffy 21-02-2018
#Project Euler Problem 5

i = 2520

for i in range (i,1000000000000,2520): #the answer must be a multiple of 2520
    if (i%11 + i%12 + i%13 + i%14 +i%15 + i%16 + i%17 + i%18 + i%19 + i%20 == 0): #if the number is divisible by each of these it is also divisible by other numbers less than 20
    
        print (i)
        break
    else:
        i = i + 2520
