answer_i=1
answer_j=1
for i in range (10, 100):
    for j in range (10, 100):
        if i != j and float(str(j)[1]) != 0.0 and float(str(i)[1]) == float(str(j)[0]) and float(str(i)[0]) / float(str(j)[1]) == i/float(j):
            answer_j *= int(str(j)[1])
            answer_i *= int(str(i)[0])

print(int(answer_j/answer_i)) 



        
        
