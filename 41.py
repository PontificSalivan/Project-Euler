from functions.prime import isPrime

pan_prime_max = 0
for n in range (1000000,1000000000):
    if isPrime(n):
        str_n = str(n)
        count = 0
        for i in str_n:
            if str_n.count(i) == 1:
                count += 1
            else:
                break
        print(n)
        if count == len(str_n):
            pan_prime_max = n
            print(pan_prime_max)
print(pan_prime_max)

    
    


