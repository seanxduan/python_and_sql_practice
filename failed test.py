def solution (A):
    left=right=0
    direction = []
    for i in range (len(A)):
        if A[i]== "<":
            left+=1
        else:
            right +=1

    return min(left, right)

print(solution(['<', '<', '>', '<', '>']))

