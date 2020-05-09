from functions.prime import isPrime

count = 0
max_count = 0
number = 0
max_count_number = 0

lst=list()
lst.append(2)

for i in range (3,100000,2):
    if isPrime(i):
        lst.append(i)

while len(lst):
    for i in lst:
        number += i
        count +=1
        if number > 100000 and number < 1000000 and isPrime(number):
            if count > max_count :
                max_count = count
                max_count_number = number
    number = 0
    count = 0
    del lst[0]

print(max_count_number)   





            
        
            


        

print()




    