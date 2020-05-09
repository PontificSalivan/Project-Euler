
max_sum = 0

for i in range (11,101):
    for j in range (11,101):
        sums = i**j
        current_sums = sum(map(int, list(str(sums))))
        if current_sums > max_sum:
            max_sum = current_sums
            
print(max_sum)