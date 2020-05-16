
count = 9
for i in range(4,10):
    for j in range(2,10**10):
        if len(str(i**j)) == j:
            count += 1
        else:
            break
print(count)