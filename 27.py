def isPrime(k):
    return all(k % i for i in range(2, k))

maxPrimeCount = 0
primeCount = 0

for a in range (0, -999, -1): # for a in range (-999, 1000):

    for b in range (abs(a), 1000):  # for b in range (-1000, 1001):

        for n in range (0, 80):

            if  isPrime (abs(n**2 + a*n + b)):
                primeCount += 1
            else:
                break

        if primeCount > maxPrimeCount:
            maxPrimeCount = primeCount
            best_a = a
            best_b = b
        primeCount = 0

print(best_a * best_b )



