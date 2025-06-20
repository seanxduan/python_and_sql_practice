
# lets define our fnction!
#def puzzle_function(puzzle_vector):
#    for i in puzzle_vector:
#        if i != "?":
#            pass
#        else:
#            if i-1 != "a" and i+1 != "a":
#            puzzle_vector[i]="a"
#            else:
#                if i-1 != "b" and i+1 != "b":
#                puzzle_vector[i]="b"
#                else:
#                    puzzle_vector[i]="c"


# lets define our fnction!
def npc_function(puzzle_vector):
    puzzle_vector.append("*")
    puzzle_vector.insert(0,"*")
    for i in range(len(puzzle_vector)):
        if puzzle_vector[i] == "?":
            #we're referring to the entry in the vector index, not the value itself -1
            if puzzle_vector[i-1] != "a" and puzzle_vector[i+1] != "a":
                puzzle_vector[i]="a"
            elif puzzle_vector[i-1] != "b" and puzzle_vector[i+1] != "b":
                puzzle_vector[i]="b"
            else:
                puzzle_vector[i]="c"
    puzzle_vector.pop()
    puzzle_vector.pop(0)
    return "".join(map(str, puzzle_vector))

mystring = "?????a?sdk?lf/jh?hip?o?????"
print (mystring)
print(npc_function(list(mystring)))