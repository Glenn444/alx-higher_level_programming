#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")

            dividend = my_list_1[i]
            divisor = my_list_2[i]
            dividend_type = isinstance(dividend, (int, float))
            divisor_type = isinstance(divisor, (int, float))

            if not dividend_type or not divisor_type:
                raise TypeError("wrong type")

            if divisor == 0:
                raise ZeroDivisionError("division by 0")

            result = dividend / divisor
        except IndexError as e:
            print("out of range")
            result = 0
        except TypeError as e:
            print("wrong type")
            result = 0
        except ZeroDivisionError as e:
            print("division by 0")
            result = 0
        finally:
            result_list.append(result)

    return result_list
