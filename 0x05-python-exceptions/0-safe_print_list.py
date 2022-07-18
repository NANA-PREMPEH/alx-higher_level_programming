#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    while j < x and x > 0:
        try:
            print(my_list[j], end='')
            j += 1
        except Exception as e:
            break
    print("")
    return int(j)
