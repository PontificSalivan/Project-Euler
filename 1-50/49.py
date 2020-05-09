import itertools
from functions.prime import isPrime

for i in range (2000, 9877):
    if isPrime(i):

        lsst=list()
        lst = list(itertools.permutations([int(str(i)[0]),int(str(i)[1]),
                                           int(str(i)[2]),int(str(i)[3])]))

        for n in lst:
            if isPrime(int(str(n[0])+str(n[1])+str(n[2])+str(n[3]))):
                lsst.append(int(str(n[0])+str(n[1])+str(n[2])+str(n[3])))

        for n in lsst:
            for l in lsst:
                if n - l > 0:
                    temp = int((n+l)/2)
                    for x in lsst:
                        if temp == x:
                            print(lsst)
                            print(str(l)+str(temp)+str(n))
                            exit(0)












