from math import ceil

def isPrime(num, cache ={2: True}):
    if isinstance(num, str):
        num = int(num)
    if num in cache:
        return cache[num]
    
    if num % 2 == 0 :
        cache[num] = False
        return False
    top = int(ceil(num ** 0.5))
    for x in range (3, top + 1, 2):
        if num % x == 0:
            cache[num]=False
            return False
    cache[num] = True
    return True