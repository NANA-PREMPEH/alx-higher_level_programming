#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    while y < x and x > 0:
        try:
            print(my_list[i], end='')
            y += 1
        except Exception as e:
            break
    print("")
    return int(y)
