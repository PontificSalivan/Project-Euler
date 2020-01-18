max_count = 0
p_max = 0
for p in range(100, 1001, 2):
    count = 0
    for angle_1 in range (2, int(p/2)+1):
        for angle_2 in range (angle_1, int(p/2)+1):
            if (p - angle_1 - angle_2)**2 == angle_1**2 + angle_2**2:
                count += 1 
        if count > max_count:
            max_count = count
            p_max = p

print(p_max)




