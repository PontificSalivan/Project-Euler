from math import factorial as f
numb = 0
answer = 0
for i in range (10, 100000):
    for char in (str(i)):
        numb += f(int(char))
    if numb == i:
        answer += i
    numb = 0
print(answer)
    
    