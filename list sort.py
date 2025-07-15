def solution(A):
    B = []
    for i in range (len(A)):
        unique = True
        for j in range (len(A)):
            if i == j:
                pass
            elif A[i] == A[j]:
                unique = False
                break
        if unique:
            B.append(A[i])

    print (A)
    print (B)
    for x in A:
        for y in B:
            if x==y:
                return x
    return -1


print(solution([1,2,5,1,2,3]))