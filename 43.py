import itertools

sum_pan = 0
lst = list(itertools.permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))
padlist = list()
string = ''
for padlist in lst:
    if int(padlist[7]+ padlist[8]+ padlist[9])% 17 == 0:
        if int(padlist[6]+ padlist[7]+ padlist[8])% 13 == 0:
            if int(padlist[5]+ padlist[6]+ padlist[7])% 11 == 0:
                if int(padlist[4]+ padlist[5]+ padlist[6])% 7 == 0:
                    if int(padlist[3]+ padlist[4]+ padlist[5])% 5 == 0:
                        if int(padlist[2]+ padlist[3]+ padlist[4])% 3 == 0:
                            if int(padlist[1]+ padlist[2]+ padlist[3])% 2 == 0:                                                   
                                string = ''.join(padlist)
                                sum_pan += int(string)
print(sum_pan)
