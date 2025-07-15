def reverse_list(items):
    rev_list = []
    for i in range(len(items) - 1, -1, -1):
        rev_list.insert(0, items[i])
        print(rev_list)
    return rev_list

test = [1,2,3,4,5]
print(test)

print(reverse_list(test))
