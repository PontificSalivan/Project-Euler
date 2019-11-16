f = open('22names.txt', 'r')
sortedList = f.read()
f.close()

sortedList = sortedList.replace('"', '')
names = sortedList.split(',')
names.sort()


index=1
sumOfPoints=0
pointsList = list()

for i in names:
    for word in i:
        if word == 'A':
            sumOfPoints +=1
        elif word == 'B':
            sumOfPoints +=2
        elif word == 'C':
            sumOfPoints +=3
        elif word == 'D':
            sumOfPoints +=4
        elif word == 'E':
            sumOfPoints +=5
        elif word == 'F':
            sumOfPoints +=6
        elif word == 'G':
            sumOfPoints +=7
        elif word == 'H':
            sumOfPoints +=8
        elif word == 'I':
            sumOfPoints +=9
        elif word == 'J':
            sumOfPoints +=10
        elif word == 'K':
            sumOfPoints +=11
        elif word == 'L':
            sumOfPoints +=12
        elif word == 'M':
            sumOfPoints +=13
        elif word == 'N':
            sumOfPoints +=14
        elif word == 'O':
            sumOfPoints +=15
        elif word == 'P':
            sumOfPoints +=16
        elif word == 'Q':
            sumOfPoints +=17
        elif word == 'R':
            sumOfPoints +=18
        elif word == 'S':
            sumOfPoints +=19
        elif word == 'T':
            sumOfPoints +=20
        elif word == 'U':
            sumOfPoints +=21
        elif word == 'V':
            sumOfPoints +=22
        elif word == 'W':
            sumOfPoints +=23
        elif word == 'X':
            sumOfPoints +=24
        elif word == 'Y':
            sumOfPoints +=25
        else:
            sumOfPoints +=26
    pointsList.append(sumOfPoints * index)
    index += 1
    sumOfPoints=0
print(sum(pointsList))


    

