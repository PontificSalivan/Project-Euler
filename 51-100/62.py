from itertools import permutations,groupby
import sys
from math import modf

def value_of_number(i):
    value_of_0,value_of_1,value_of_2,value_of_3,value_of_4,value_of_5,value_of_6,value_of_7,value_of_8,value_of_9=0,0,0,0,0,0,0,0,0,0
    for j in i:
        if j =='0':
            value_of_0 += 1
        elif j == '1':
            value_of_1 += 1
        elif j == '2':
            value_of_2 += 1
        elif j == '3':
            value_of_3 += 1
        elif j == '4':
            value_of_4 += 1
        elif j == '5':
            value_of_5 += 1
        elif j == '6':
            value_of_6 += 1
        elif j == '7': 
            value_of_7 += 1
        elif j == '8': 
            value_of_8 += 1
        else: 
            value_of_9 += 1
    return value_of_0,value_of_1,value_of_2,value_of_3,value_of_4,value_of_5,value_of_6,value_of_7,value_of_8,value_of_9



duplicates = {}
lst = list()
new_lst=list()

for i in range(1,10000):
    lst.append(str(i**3))

for i in lst:
    i = ''.join(sorted(i))
    new_lst.append(i)


for el, group in groupby(sorted(new_lst)):
    count = len(list(group))
    if count > 4:
        duplicates[el] = count 

for i in duplicates:
    for k in lst:
        if value_of_number(i) == value_of_number(k) and len(i) == len(k):
            print(k)
            sys.exit()
      

