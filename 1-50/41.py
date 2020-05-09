from functions.prime import isPrime

for n in range (9999999, 1000000, -2):
    if isPrime(n):
        lst = list()
        str_n = str(n)
        count = 0

        for i in str_n:
            if i == '0':
                break
            elif str_n.count(i) == 1:
                count += 1
            else:
                break

        if count == len(str_n) and str_n.count('1')==1:
            for i in str_n:
                lst.append(int(i))
            lst.sort()
            if lst[6]-lst[5] == 1 and lst[5]-lst[4] == 1 and lst[4]-lst[3] == 1  and lst[3]-lst[2] == 1 and lst[2]-lst[1] == 1 and lst[1]-lst[0] == 1:
                print(n)
                exit(0)




    
    


