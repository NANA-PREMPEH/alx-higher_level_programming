#!/usr/bin/python3
def magic_calculation(a, b):
    start = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                start += (a ** b) / i
        except Exception:
            start = b + a
            break
    return (start)
