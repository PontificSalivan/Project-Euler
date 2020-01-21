sum_i = 0
for i in range (1,1001):
    sum_i += i**i
print(str(sum_i)[len(str(sum_i))-10:len(str(sum_i))])