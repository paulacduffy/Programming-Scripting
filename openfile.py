#Paula Duffy 03-01-2018
#Week 5 Exercise

with open ("data/iris.csv") as f:
    for line in f:
      print (line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3])
