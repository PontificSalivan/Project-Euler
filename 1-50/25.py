def fib(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a

for i in range (1, 10**10):
    x=str(fib(i))
    if len(x) == 1000:
        print(i)
        break
