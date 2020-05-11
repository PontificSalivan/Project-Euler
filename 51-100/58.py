from functions.prime import isPrime


primes_count = 8
count = 13
len_of_square = 7

while primes_count/count > 0.1:

    for i in range(len_of_square**2,(len_of_square+2)**2+1,len_of_square+1):
       
        if isPrime(i):          
            primes_count += 1
    count += 4
    len_of_square += 2

print(len_of_square)
    



