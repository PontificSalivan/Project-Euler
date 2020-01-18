greatest_len_period = 0
greatest_len_period_d = 0
for d in range(2,1001):
    if d % 5 != 0 and d % 2 != 0 and d % 3 !=0 :
        
        len_period = 0
        check = 0
        len_period_alg = 10

        while check != 1:
            check = len_period_alg % d
            len_period_alg *= 10
            len_period += 1

        if len_period > greatest_len_period:
            greatest_len_period = len_period
            greatest_len_period_d = d 

print(greatest_len_period_d)



