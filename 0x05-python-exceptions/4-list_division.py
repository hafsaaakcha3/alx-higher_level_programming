#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for idx in range(list_length):
        try:
            div_idx = my_list_1[idx] / my_list_2[idx]
        except (TypeError, ValueError):
            print("wrong type")
            div_idx = 0
        except ZeroDivisionError:
            print("division by 0")
            div_idx = 0
        except IndexError:
            print("out of range")
            div_idx = 0
        finally:
            new_list.append(div_idx)
    return (new_list)
