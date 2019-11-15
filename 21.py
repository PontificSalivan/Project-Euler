def isPrime(n):
    return all(n % i for i in range(2, n))

sumOfBros=0
lst=list()
for i in range (10,10001):
    if isPrime(i):
        continue
    else:
        for j in range (1,int(i/2)+1):
            if int(i%j) == 0:
                lst.append(j)
        if sum(map(int, lst)) != i:
            secondBro = sum(map(int, lst))
            lst=list()
            for j in range (1, int(secondBro/2)+1):
                if int(secondBro%j) ==0:
                    lst.append(j)
            if sum(map(int, lst)) == i:
                sumOfBros += secondBro + i
    lst=list()
print(int(sumOfBros/2))
