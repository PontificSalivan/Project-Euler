
jump = 2
count = 0
i = 1
sumOfDiag = 1
while i != 1002001:
    i += jump
    sumOfDiag += i
    count += 1
    if count == 4:
        count = 0
        jump += 2
print(sumOfDiag)





