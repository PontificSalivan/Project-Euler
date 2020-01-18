def isPrime(n):
    return all(n % i for i in range(2, n))
sumi=186 # first 4 numbers less than 100
for i in range (100,1000001):

    if str(i)[0] == '3' or str(i)[0] == '7':

        if str(i)[len(str(i))-1] == '3' or str(i)[len(str(i))-1] == '7':

            for n in str(i):
                if int(n) % 2 == 0:
                    n = '10'
                    break

            if n == str(i)[len(str(i))-1]:

                if isPrime(i):
                    current_i = i

                    while i > 0:
                        i = i // 10
                        if isPrime(i)==False:
                            break

                    if i == 0:
                        i = current_i

                        while i > 0:
                            i = int(str(i)[::-1])
                            i = i // 10
                            i = int(str(i)[::-1])
                            if isPrime(i)==False:
                                break
                            
                        if i == 0:
                            sumi += current_i      

print(sumi)

                
