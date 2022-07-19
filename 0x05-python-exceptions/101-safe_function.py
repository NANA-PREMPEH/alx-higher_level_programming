#!/usr/bin/python3
def safe_function(fct, *args):
    import sys

    try:
        respond = fct(*args)
        return respond

    except (TypeError, ValueError, ZeroDivisionError, IndexError) as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
