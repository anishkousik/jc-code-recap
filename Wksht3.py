#Set 1.1
from array import array
from math import sqrt
sqFile = open("PERFECT_SQUARES.TXT", "w")
n = int(input("Input a number n: "))
for i in range(1,n+1):
    if str(sqrt(i))[-2:] == ".0":
        sqFile.write(str(i)+'\n')
sqFile.close()

#Set 1.2
sqFile = open("PERFECT_SQUARES.TXT", "a")
m = int(input("Input a number m: "))
for i in range(n+1,n+m+1):
    sqFile.write(str(i)+'\n')
sqFile.close()

#Set 1.3
irisData = open("iris.data", 'r')
L = []
for line in irisData:
    if line != '\n':
        line = line.strip().split(',')
        L.append(line)
print(L)

#Set 2
def primeChecker(n):
    primeFile = open("primes1000000.txt",'r')
    for i in primeFile:
        if int(i) == n:
            return True
    return False

def largeprimeChecker(n):
    for i in range(2,n):
        if str(n/i)[-2:] == '.0':
            print(i)
            return False
    return True
print(primeChecker(7))
print(largeprimeChecker(1000001))

#Set 3
import re
temp = open("shakespeare-romeo-48.txt",'r')
arr = []
arr2 = []
count = 0
for line in temp:
    tempArray = line.strip().split()
    if tempArray != []:
        for i in tempArray:
            #print(i)
            j = re.split("[][,:;?!'.)(]" ,i)
            for k in j:
                if k != '':
                    k = k.lower()
                    if k in arr:
                        
                        arr2[arr.index(k)] += 1
                    else:
                        arr.append(k)
                        arr2.append(1)
temp.close()

#print(arr)
#print(arr2)
temp = open("R&J_WORD_FREQS.TXT",'w')
for i in range(len(arr)):
    a = (str(arr[i]) + ' ' + str(arr2[i]) + '\n')
    temp.write(a)
temp.close()