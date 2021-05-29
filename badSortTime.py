import time
import sys
import math
from random import seed
from random import randint
from fractions import Fraction

# function: badSortFunction
# purpose: sort an array of ints
# description: Does a terrible job of sorting data, takes a long time
def badSortFunction(intArray,alpha):
	length = len(intArray)
	# length of one or two are the base cases
	if(length == 1):
		return intArray 
	if(length == 2): 
		if intArray[0] > intArray[1]:
			temp = intArray[1]
			intArray[1]=intArray[0]
			intArray[0]=temp
		return intArray
	elif(length > 2):
		# if alpha is 2/3 then grab the ceiling for m other wise if 3/4 grab the floor
		m=0
		if(alpha < 3/4):
			m = math.ceil(alpha * length)
		if(alpha == 3/4):
			m = math.floor(alpha * length)
		# break the array into a fraction of its length
		firstArray = intArray[0:m]
		firstArray = badSortFunction(firstArray,alpha)
		# recombine array
		firstArray= firstArray + intArray[m:length]
		length = len(firstArray)
		# break the array into a fraction of its length
		secondArray = firstArray[(length-m):length]
		secondArray = badSortFunction(secondArray,alpha)
		# recombine array
		secondArray = firstArray[0:length-m] + secondArray
		# break the array into a fraction of its length
		thirdArray = secondArray[0:m]
		thirdArray = badSortFunction(thirdArray, alpha)
		# recombine array
		intArray= thirdArray + secondArray[m:length]
		return intArray
# Generates an array of a given input
def generateRandom(n):
	seed(1)
	i = 0
	intArray = []
	while i<n:
		intArray.append(randint(0,20000))		
		i = i+1
	return intArray
intArray = generateRandom(200)
start = time.time()
intArray = badSortFunction(intArray,3/4)
end = time.time()
print("n: 200 alpha: 3/4 time: ", end-start)
intArray = generateRandom(300)
start = time.time()
intArray = badSortFunction(intArray,3/4)
end = time.time()
print("n: 300 alpha: 3/4 time: ", end-start)
intArray = generateRandom(400)
start = time.time()
intArray = badSortFunction(intArray,3/4)
end = time.time()
print("n: 400 alpha: 3/4 time: ", end-start)
intArray = generateRandom(500)
start = time.time()
intArray = badSortFunction(intArray,3/4)
end = time.time()
print("n: 500 alpha: 3/4 time: ", end-start)
intArray = generateRandom(200)
start = time.time()
intArray = badSortFunction(intArray,2/3)
print(intArray)
end = time.time()
print("n: 200 alpha: 2/3 time: ", end-start)
intArray = generateRandom(300)
start = time.time()
intArray = badSortFunction(intArray,2/3)
end = time.time()
print("n: 300 alpha: 2/3 time: ", end-start)
intArray = generateRandom(400)
start = time.time()
intArray = badSortFunction(intArray,2/3)
end = time.time()
print("n: 400 alpha: 2/3 time: ", end-start)
intArray = generateRandom(500)
start = time.time()
intArray = badSortFunction(intArray,2/3)
end = time.time()
print("n: 500 alpha: 2/3 time: ", end-start)

