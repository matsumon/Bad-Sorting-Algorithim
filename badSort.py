import time
import sys
import math
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
# open input file
file = open("data.txt","r")
# open output file
outputFile= open("bad.out","a")
alpha = sys.argv[1]
alpha = Fraction(alpha)
for line in file:
    # replace new lines and then make a string into an array
	line = line.replace("\n", "")
	intArray = line.split(" ")
	intArray = [int(i) for i in intArray]
	intArray.pop(0)
	array = badSortFunction(intArray,alpha)
	# Turn array back into a string and remove uneeded chars
	string = str(array)
	string = string.strip("[]")
	string = string.replace("'","")
	string = string.replace(",","")
	string = string + "\n"
	outputFile.write(string)


