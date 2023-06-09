#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)

    b = 0

    new_string = my_string[:]

    for a in range(length):
        if (my_string[a] == 'c' or my_string[a] == 'C'):
            new_string = new_string[:(a - b)] + my_string[(a + 1):]
            b += 1

    return (new_string)
