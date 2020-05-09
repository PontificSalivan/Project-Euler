from functions.prime import isPrime


square_lst = list()
for n in range (1, 1000):
    square_lst.append(2*n**2)

for i in range (35, 10000, 2):
    Gate = False
    if isPrime(i)== False:
        prime_lst = list()

        for n in range (i-2 , 2, -1):
            if isPrime(n):
                prime_lst.append(n)

        for n in prime_lst:
            if Gate == False:
                k = i - n 
                for l in square_lst:
                    if k == l:
                        Gate = True
                        break
            else:
                break
            

        if Gate == False:
            print(i)
            break





                

            

            



