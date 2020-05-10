from functions.prime import isPrime

diag_numbers = 2
primes_count = 0
count = 1
for i in range(3,10,diag_numbers):
    if isPrime(i):
        primes_count += 1
    count += 1
print(primes_count/count)


