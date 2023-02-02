#Set 1.1

#L = [1,2,3,3,4,4,4,5,6,6]

def linearSearch1(L,t):
    for i in range(len(L)):
        if L[i] == t:
            return i
    return -1

#print(linearSearch1(L,7))

#Set 1.2

def binarySearch1(L,t):
    start = 0
    end = len(L) -1
    while start <= end:
        mid = (start + end) // 2
        if L[mid] == t:
            return mid
        elif L[mid] < t:
            start = mid + 1
        else:
            end = mid - 1
    return -1

#print(binarySearch1(L,7))

#Set 1.3

descL = [6,5,4,3,2,1]

def binarySearch2(L,t):
    start = 0
    end = len(L) - 1
    while start <= end:
        mid = (start + end) // 2
        if L[mid] == t:
            return mid
        elif L[mid] < t:
            end = mid - 1
        else:
            start = mid + 1
    return -1

#print(binarySearch2(descL,7))

#Set 2.4

def linearSearch2(L,t):
    cur = 0
    prev = -1
    for i in range(len(L)):
        if L[i] > t:
            cur = L[i]
            if prev == -1:
                prev = cur
            else:

                if cur < prev:
                    prev = cur
    return prev

#print(linearSearch2(L,1))

#Set 2.5

def linearSearch3(L,t):
    cur = 0
    prev = -1
    for i in range(len(L)):
        if L[i] < t:
            cur = L[i]
            if prev == -1:
                prev = cur
            else:
                if cur > prev:
                    prev = cur
    return prev

#print(linearSearch3(L,4))

#Set 2.6
#Not able to do due to unavailable text file

#3.7

def binarySearch3(L,t):
    start = 0
    end = len(L) - 1
    while start <= end:
        mid = (start + end) // 2
        if L[mid] == t:
            if mid == len(L) - 1:
                return -1
            else:
                if L[mid + 1] != t:
                    return L[mid + 1]
                else:
                    mid += 1
                    while mid != len(L):
                        if L[mid] > t:
                            return L[mid]
                        else:
                            mid += 1
        elif L[mid] > t:
            end = mid - 1
        else:
            start = mid + 1
    return -1

#print(binarySearch3(L,4))
            
#Set 3.8

def binarySearch4(L,t):
    start = 0
    end = len(L) - 1
    while start <= end:
        mid = (start + end) // 2
        if L[mid] == t:
            if mid == 0:
                return -1
            else:
                if L[mid - 1] != t:
                    return L[mid - 1]
                else:
                    mid -= 1
                    while mid != -1:
                        if L[mid] < t:
                            return L[mid]
                        else:
                            mid -= 1
        elif L[mid] > t:
            end = mid - 1
        else:
            start = mid + 1
    return -1

#print(binarySearch4(L,5))

#Set 3.9
#Not able to do due to unavailable text file

#Set 3.10
from random import randint
import datetime

n = [100,500,1000,5000,10000]
k = 30
results = []
for i in n:
    totalLinear = 0
    totalBinary = 0
    for j in range(1,k+1):
        L = [x for x in range(1,(i*2) + 1)]
        t = randint(1,(i*2)+1)
        past = int(datetime.datetime.now().strftime("%f"))
        temp = linearSearch1(L,t)
        present = int(datetime.datetime.now().strftime("%f"))
        interval = present - past
        totalLinear += interval

        past = int(datetime.datetime.now().strftime("%f"))
        temp = binarySearch1(L,t)
        present = int(datetime.datetime.now().strftime("%f"))
        interval = present - past
        totalBinary += interval
    results.append(((totalLinear/30),(totalBinary/30)))

print("Linear Search:")
print()
print("{0:<13}{1:<3}{2:<12}".format("List Size (n)"," ","Average Time"))
print("{0:<13}{1:<3}{2:<12}".format("-------------"," ","------------"))
for i in range(5):
    print("{0:<13}{1:<3}{2:<12}".format(n[i]," ",results[i][0]))

print()
print()
print()

print("Binary Search:")
print()
print("{0:<13}{1:<3}{2:<12}".format("List Size (n)"," ","Average Time"))
print("{0:<13}{1:<3}{2:<12}".format("-------------"," ","------------"))
for i in range(5):
    print("{0:<13}{1:<3}{2:<12}".format(n[i]," ",results[i][1]))
