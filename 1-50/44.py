lst = list()
for n in range (2, 10001):     
    lst.append(int(n*(3*n-1)/2))

for i in range(len(lst)):
    for n in range(i+1,len(lst)):

        if (((24 * (lst[i]+lst[n]) + 1)**0.5 + 1)/6).is_integer():
            if (((24 * (lst[n]-lst[i]) + 1)**0.5 + 1)/6).is_integer():                    
                print(int(lst[n] - lst[i]))
                exit(0)

