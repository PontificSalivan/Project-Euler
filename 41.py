from functions.prime import isPrime

pan_prime_max = 0
for n in range (9876543, 9000000, -1):
    if isPrime(n):
        str_n = str(n)
        count = 0
        for i in str_n:
            if i == '0':
                break
            if str_n.count(i) == 1:
                count += 1
            else:
                break
        if count == len(str_n):
            pan_prime_max = n
            print(pan_prime_max)
print(pan_prime_max)

    
    


