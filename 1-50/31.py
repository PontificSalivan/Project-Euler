
count = 1+1+1+1+1+1+1+1
for p100 in range(0,2):
    for p50 in range (0,4):
        for p20 in range (0,10):
            for p10 in range (0,20):
                for p5 in range (0,40):
                    for p2 in range (0,100):
                        for p1 in range (0,200):
                            if  p100*100 + p50*50 + p20*20 + p10*10 + p5 * 5 + p2 * 2 + p1 == 200:
                                count += 1
print(count)






