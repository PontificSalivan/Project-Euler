newSum=0
requiredSum = 0

for i in range (10, 1000000): # Just huge number
    for char in str(i):
        newSum += int(char)**5
    if newSum == i:
        requiredSum += i
    newSum=0
    
print(requiredSum)




    


