count=45

i=99120
lst = list()

while i < 130000:
    if str(2**(i+196))[0:3] == '123':
        lst.append(196)
        i += 196
        print(lst)
    elif str(2**(i+289))[0:3] == '123':
        lst.append(289)
        i += 289
        print(lst)
    elif str(2**(i+485))[0:3] == '123':
        lst.append(485)
        i += 485
        print(lst)


    


#answer in 686.txt file
