from functions.prime import isPrime

count = 0
for i in range (2,1000001):
    if isPrime(i):
        Gate = True
        for _ in range (len(str(i))-1):
            new_i = str(i)[len(str(i))-1] + str(i // 10)
            if isPrime(new_i) == False:
                Gate = False
                break
            i = int(new_i)
        if Gate:
            count += 1 
              
print(count)


