from itertools import groupby

def lst_replace(lst):
    gate = False
    lst_1 = list()

    lst = ''.join(lst)

    lst=lst.replace('T','10')
    lst=lst.replace('J','11')
    lst=lst.replace('Q','12')
    lst=lst.replace('K','13')
    lst=lst.replace('A','14')

    for char in lst:
        if gate:
            lst_1.append(int('1' + char))
            gate = False
        else:
            if char == '1':
                gate = True
            else:
                lst_1.append(int(char))

    return (lst_1)
def value_of_cards(lst):
    n_1=list()
    n_2=list()

    lst_answer = list()

    same_lst_1 = list()
    same_lst_2 = list()

    for i in range(0,5):
        n_1.append(lst[i][0])
        n_2.append(lst[i][1])
    
    n_1 = lst_replace(n_1)
    n_1.sort()
     
    n_2.sort()
    groupped_str = groupby(n_2)

    for elem, grouper in groupped_str:
        same_lst_2.append(len(list(grouper)))  
    same_lst_2.sort()
    same_2 = int(same_lst_2[len(same_lst_2)-1])

    groupped_str = groupby(n_1)
    for elem, grouper in groupped_str:
        same_lst_1.append(list((str(len(list(grouper))),elem)))
    same_lst_1.sort()
    
    same_1_1 = int(same_lst_1[len(same_lst_1)-1][0])
    same_1_2 = int(same_lst_1[len(same_lst_1)-2][0])
    if  same_1_1 == same_1_2 and int(same_lst_1[len(same_lst_1)-1][1]) > int(same_lst_1[len(same_lst_1)-2][1]):
        same_1_12 = int(same_lst_1[len(same_lst_1)-1][1])
    else:
        same_1_12 = int(same_lst_1[len(same_lst_1)-2][1])
    
    if same_2 == 5:
        if n_1[4] == '14' and n_1[3] == '13' and n_1[2] == '12' and n_1[1] == '11' and n_1[0] == '10':
            lst_answer.append(10)
            lst_answer.append(14)
            return lst_answer
        elif int(n_1[4])-int(n_1[3])==1 and int(n_1[3])-int(n_1[2])==1 and int(n_1[2])-int(n_1[1])==1 and int(n_1[1])-int(n_1[0])==1:
            lst_answer.append(9)
            lst_answer.append(n_1[4])
            return lst_answer
        else:
            lst_answer.append(6)
            lst_answer.append(n_1[4])
            return lst_answer
            
    elif same_2 == 4:
        if int(n_1[4])-int(n_1[3])==1 and int(n_1[3])-int(n_1[2])==1 and int(n_1[2])-int(n_1[1])==1 and int(n_1[1])-int(n_1[0])==1:
            lst_answer.append(5)
            lst_answer.append(n_1[4])
            return lst_answer
        elif same_1_1 == 2:
                lst_answer.append(2)
                lst_answer.append(int(same_lst_1[len(same_lst_1)-1][1]))
                return lst_answer
        else:
            lst_answer.append(1)
            lst_answer.append(n_1[4])
            return lst_answer

    elif same_2 == 3:
        if int(n_1[4])-int(n_1[3])==1 and int(n_1[3])-int(n_1[2])==1 and int(n_1[2])-int(n_1[1])==1 and int(n_1[1])-int(n_1[0])==1:
            lst_answer.append(5)
            lst_answer.append(n_1[4])
            return lst_answer
        elif same_1_1 == 2:
            if same_1_2 == 2:
                lst_answer.append(3)
                lst_answer.append(same_1_12)
                return lst_answer
            else:
                lst_answer.append(2)
                lst_answer.append(int(same_lst_1[len(same_lst_1)-1][1]))
                return lst_answer
        elif same_1_1 == 3:
            lst_answer.append(4)
            lst_answer.append(int(same_lst_1[len(same_lst_1)-1][1]))
            return lst_answer
        else:
            lst_answer.append(1)
            lst_answer.append(n_1[4])
            return lst_answer
            
    else:
        if int(n_1[4])-int(n_1[3])==1 and int(n_1[3])-int(n_1[2])==1 and int(n_1[2])-int(n_1[1])==1 and int(n_1[1])-int(n_1[0])==1:
            lst_answer.append(5)
            lst_answer.append(n_1[4])
            return lst_answer
        elif same_1_1 == 2:
            if same_1_2 == 2:
                lst_answer.append(3)
                lst_answer.append(same_1_12)
                return lst_answer
            else:
                lst_answer.append(2)
                lst_answer.append(int(same_lst_1[len(same_lst_1)-1][1]))
                return lst_answer
        elif same_1_1 == 3:
            if same_1_2 == 2:
                lst_answer.append(7)
                lst_answer.append(int(same_lst_1[len(same_lst_1)-1][1]))
                return lst_answer
            else:
                lst_answer.append(4)
                lst_answer.append(int(same_lst_1[len(same_lst_1)-1][1]))
                return lst_answer
        elif same_1_1 == 4:
            lst_answer.append(8)
            lst_answer.append(int(same_lst_1[len(same_lst_1)-1][1]))
            return lst_answer
        else:
            lst_answer.append(1)
            lst_answer.append(n_1[4])
            return lst_answer

f = open('54.txt', 'r')

count = 0

lst = list(f)

for i in range (0,1000):
    lst_1,lst_2  = list(),list()
    for j in range (1,11):
        if j < 6:
            lst_1.append(lst[i][3*(j-1):3*j][:2])
        else:
            lst_2.append(lst[i][3*(j-1):3*j][:2]) 
            
    lst_1 = value_of_cards(lst_1)
    lst_2 = value_of_cards(lst_2)
    
    if int(lst_1[0])>int(lst_2[0]):
        count += 1
    elif int(lst_1[0])==int(lst_2[0]) and int(lst_1[1])>int(lst_2[1]):
        count += 1

print(count)


    


    


   



     

