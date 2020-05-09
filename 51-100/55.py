
Lychrel_numbers_count = 0

for i in range(1,10001):
    count = 0
    while count < 51:       
        count += 1
        i = i + int(str(i)[::-1])
        if str(i) == str(i)[::-1]:
            break
    if count == 51:
        Lychrel_numbers_count +=1
print(Lychrel_numbers_count)




        