#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            value1 = my_list_1[i]
            value2 = my_list_2[i]
            if not isinstance(value1, (int, float)) or \
                    not isinstance(value2, (int, float)):
                raise TypeError("wrong type")
            if value2 == 0:
                raise ZeroDivisionError("division by 0")
            result.append(value1 / value2)
        except IndexError as e:
            print("Error:", e)
            result.append(0)
        except TypeError as e:
            print("Error:", e)
            result.append(0)
        except ZeroDivisionError as e:
            print("Error:", e)
            result.append(0)
        finally:
            continue
    # print(result)
    return (result)
