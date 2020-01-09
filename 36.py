sumP = 0
for i in range (1, 1000001):
    if str(i) == str(i)[::-1]:
        b = ''
        n=i
        while n > 0:
            b = str(n % 2) + b
            n = n // 2
        if b == b[::-1]:
            sumP +=  i
print(sumP)