f = open('22names.txt', 'r')
sortedList = f.read()
f.close()

sortedList = sortedList.replace('"', '')
names = sortedList.split(',')
names.sort()


index=1
sumOfPoints=0
pointsList = list()

alphabet_to_nums = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,
                    'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,
                    'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,
                    'V':22,'W':23,'X':24,'Y':25,'Z':26}
for i in names:
    for word in i:                    
        for n in alphabet_to_nums:
            if word == n:
                sumOfPoints += alphabet_to_nums[n]
    pointsList.append(sumOfPoints * index)
    index += 1
    sumOfPoints=0
print(sum(pointsList))



