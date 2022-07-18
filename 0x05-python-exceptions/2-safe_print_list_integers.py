#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    y = 0
    j = 0
    while y < x and x > 0:
        try:
            val = my_list[y]
            if isinstance(val, int):
                print(my_list[y], end='')
                j += 1
            y += 1
        except IndexError:
            break
    print("")
    return int(j)
