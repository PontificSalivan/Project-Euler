lst= list()
newSum=0
requiredSum = 0
for i in range (10, 1000000): # Just huge number
    for char in str(i):
        lst.append(char)
    for el in lst:
        newSum += int(el)**5
    if newSum == i:
        requiredSum += i
    newSum=0
    lst = list()
print(requiredSum)




    


