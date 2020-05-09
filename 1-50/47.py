from functions.prime import isPrime, prime_factors

n=1
count_of_multipliers = 4
current_count_of_multipliers = []
while len(current_count_of_multipliers) < count_of_multipliers:
    primes = set(prime_factors(n))
    if len(primes)== count_of_multipliers:
        current_count_of_multipliers.append(n)
    else:
        current_count_of_multipliers = []
    n += 1
print(current_count_of_multipliers[0])











    
