from itertools import groupby

greatest_pan = 0

for i in range (1, 10000):
    pan = ''
    n=1
    while len(pan) < 9:
        pan = pan + str(i*n)
        n += 1

    if len(pan) == 9:
        lst = list()
        for n in pan:
            if n == '0':
                lst = list()
                break
            lst.append(n)
        lst.sort()
        new_lst = [el for el, _ in groupby(lst)]

        if len(new_lst) == 9:
            if int(pan) > greatest_pan:
                greatest_pan = int(pan)
                
print(greatest_pan)
        
