#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    reserve_list = []
    for i in range(0, list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except (IndexError):
            print("out of range")
        except (TypeError, ValueError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            reserve_list.append(result)
    return reserve_list
