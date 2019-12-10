from collections import Counter
from itertools import groupby

lst_char = list()
lst = list()
for i in range (0, 2000):
    for j in range (0, 2000):
        contStr = str(i)+ str(j)+ str(i*j)
        
        for char in contStr:
            lst_char.append(char)

        arr = Counter(lst_char)
        lst_char= list()

        if arr['1'] == 1 and arr['2'] == 1 and arr['3'] == 1 and arr['4'] == 1 and arr['5'] == 1 and arr['6'] == 1 and arr['7'] == 1 and arr['8'] == 1 and arr['9'] == 1 and arr['0'] == 0:
            lst.append(i*j)

lst.sort()
new_lst = [el for el, _ in groupby(lst)]

print(sum(new_lst))


