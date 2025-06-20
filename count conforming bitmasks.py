def solution(A, B, C):
    countA = 0
    countB = 0
    countC = 0
    countAB = 0
    countAC = 0
    countBC = 0
    countABC = 0
    txtA=(bin(A)[2:]).zfill(30)
    txtB=(bin(B)[2:]).zfill(30)
    txtC=(bin(C)[2:]).zfill(30)
    for i in range(30):
        if txtA[i] == "0":
            countA+=1
    for i in range(30):
        if txtB[i] == "0":
            countB+=1
    for i in range(30):
        if txtC[i] == "0":
            countC+=1
    for i in range(30):
        #because it's only 30 bits, don't need to do range(len(A))
        if txtA[i] == "0" and txtB[i] == "0":
            countAB+=1
    for i in range(30):

        if txtA[i] == "0" and txtC[i] == "0":
            countAC+=1
    for i in range(30):

        if txtB[i] == "0" and txtC[i] == "0":
            countBC+=1
    for i in range(30):

        if txtA[i] == "0" and txtB[i] == "0" and txtC[i] == "0":
            countABC+=1

    return(2**(countA)+2**(countB)+2**(countC)-(2**(countAB)+2**(countAC)+2**(countBC))+2**(countABC))
A = 5
B = 156
C = 1000
solution(A, B, C)