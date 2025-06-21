def prime_integer(test):
    count = 0
    if (test % 2  == 0):
        while (test % 2 == 0):
            test = (test/2)
            count += 1
    #if it's odd, it 2 can't be raised to a power of it, thus we return 0
        return count
    else:
        return 0

print(prime_integer(24))