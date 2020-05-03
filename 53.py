from math import factorial

def C_sample(n,r):
    return int((factorial(n))/(factorial(r)*factorial(n-r)))

count = 0

for n in range(1,101):
    for r in range (0,n):
        value = C_sample(n,r)
        if value > 1000000:
            count += 1
print(count)
