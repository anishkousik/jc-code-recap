#Set 1.1

from math import sqrt
n = 100
f = open("PERFECT_SQUARES.TXT","w")
for i in range(1,n+1):
    if int(sqrt(i))**2 == i:
        f.write(str(i) + '\n')
f.close()

#Set 1.2

m = 10000
f = open("PERFECT_SQUARES.TXT","a")
for i in range(n+1,n+m+1):
    f.write(str(i) + '\n')
f.close()

#Set 1.3

f = open("iris.data","r")
L = []
for line in f:
    L.append(line.strip().split(","))
f.close()
#print(L)

#Set 2.4

L2 = []
f = open("primes1000000.txt","r")
for line in f:
    L2.append(line.strip())
test = int(input("Which number u wanna test fam?: "))
if test <= 1000000:
    if str(test) in L2:
        print("Lucky you scooby doo the number is a prime!")
    else:
        print("Lmao suck it the number ain't a prime")
else:
    check = False
    for i in L2:
        if (int(test/int(i)) * int(i)) == test:
            check = True
            break
    if check is True:
        print("Lmao suck it the number ain't a prime")
    else:
        print("Lucky you scooby doo the number is a prime!")

#Set 3.5
import re
f = open("shakespeare-romeo-48.txt","r")
L = []
for line in f:
    L.append(line.strip().split())
f.close()

#print(L)
L2 = []
import string
for i in L:
    for j in i:
        L2.append(j.translate(str.maketrans('','',string.punctuation)).lower())

dictionary = {}

for i in L2:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1


f = open("R&J_WORD_FREQS.TXT","w")
for key in dictionary:
    f.write(key + " : " + str(dictionary[key]) + '\n')
f.close()
