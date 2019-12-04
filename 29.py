from itertools import groupby

lst = list()

for a in range (2, 101):

    for b in range  (2, 101):
        
        lst.append(a**b)

lst.sort()
new_lst = [el for el, _ in groupby(lst)]

print(len(new_lst))