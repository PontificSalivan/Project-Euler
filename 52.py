import itertools

gate = False

for i in range (10,1000001):
    lst = list(itertools.permutations(list(str(i))))

    for j in range(2,7):
        lst_2 = list(str(i*j))

        for listing in lst:    
            if lst_2 == list(listing):
                gate = True
                break
        if gate and j < 6:
            gate=False
        else:
            break       
    if j == 6 and gate:
        print(i)
        break

         






