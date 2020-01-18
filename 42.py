f = open('42words.txt', 'r')
sortedList = f.read()
f.close()

sortedList = sortedList.replace('"', '')
words = sortedList.split(',')
words.sort()

count=0

alphabet_to_nums = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,
                    'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,
                    'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,
                    'V':22,'W':23,'X':24,'Y':25,'Z':26}

lst = list()
for n in range(1,50):
    lst.append(0.5 * n * (n + 1))


for i in words:
    triangle_sum = 0 
    for word in i:             
        for n in alphabet_to_nums:
            if word == n:
                triangle_sum += alphabet_to_nums[n]        
    for x in lst:
        if triangle_sum == int(x): 
            count += 1
            break
print(count)
        