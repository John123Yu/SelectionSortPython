from random import randint
import datetime

x = []
counter = 0;

for num in range(0,100):
	randomNumber = randint(0,10000) 
	x.append(randomNumber)

for j in range(0,len(x)):
	minimum = x[j]
	indexofmin = j
	for i in range(j+1,len(x)):
		if x[i] < minimum:
			minimum = x[i]
			indexofmin = i
	temp = x[j]
	x[j] = minimum
	x[indexofmin] = temp
print x