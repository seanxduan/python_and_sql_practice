#first step, lets define our function

def binary_gap_fxn(numeric_entry):
    temp_string=bin(numeric_entry)[2:]
    trunc_string=temp_string[temp_string.find("10"):temp_string.rfind("01")+2]
    #all this code is to chop our initial string down to just what we want based on positional indices
    print(trunc_string)
    value_maximum = 0
    # we set what we're referencing to at 0 so we don't update it while doing the for loop and own ourselves
    special_pocket = 0
    # we put this in here so we can define it before we need to reference it in the first step of the for loop
    for i in trunc_string:
        if i=="1":
            # this code tells us to update our value-max, if increasing our binary integer is greater than the saved value
            if special_pocket > value_maximum:
                value_maximum = special_pocket
            special_pocket=0
            #we put this element here because we want to only update our max BEFORE we reset, we don't need to check each time we increment 0
        else:
            special_pocket+=1

    print(value_maximum)


mynum = 15

#first step is to crank out the number we're looking at

binary_gap_fxn(mynum)


    