from itertools import groupby
from functions.prime import isPrime

sumOfAbundant = 0

lst=list()
excessList=list()

for i in range (2,28123):
    if isPrime(i):
        continue
    for j in range (1,int(i/2)+1):
        if int(i%j) == 0:
            lst.append(j)
    if sum(map(int, lst)) > i:
        excessList.append(i)
    lst=list()

for i in excessList:
    for j in excessList:
        if i + j < 28123:
            lst.append(i+j)

lst.sort()
new_lst = [el for el, _ in groupby(lst)]

for x in range (1, 28123):
    for i in new_lst:
        if x == i:
            break
    else:
        sumOfAbundant += x

print(sumOfAbundant)

# Last number = 20161


