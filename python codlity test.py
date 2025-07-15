


#now this is code for working on the function itself
def count_function(count_vector):
    for i in count_vector:
        if i < 1:
            (count_vector.remove(i))
        else:
            pass
    print(count_vector)
    # here the only thing that matters is this half thing
    for j in range (1000000):
        if j+1 in count_vector:
            pass
        else:
            print (j+1)
            break


#alternative version which is probably better?
def count_function2(count_vector):
    for j in range (1000000):
        if j+1 in count_vector:
            pass
        else:
            return j+1

#this is example code showing how to pass a vector to a function

my_vector = [1, 3, -6, -4, -1, 2]
ans= count_function(my_vector)
print (ans)