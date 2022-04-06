# Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения
# функции и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# # ValueError: wrong val -5
# Примечание: сможете ли вы замаскировать работу декоратора?
import sys
from functools import wraps


# Декоратор с аргументами

def val_checker(fanny_func):
    def inner_val_checker(func):
        # print(func.__name__)
        @wraps(func)
        def wraper(*args):
            for item in args:
                if fanny_func(item):
                    msg = func(item)
                    print(msg, sep=", ", end=", ")

                else:
                    raise ValueError(f'wrong val: {item}')
            return msg

        # print(wraper)
        return wraper

    return inner_val_checker


# def calc_cube1(lambda x : x > 0):
#     return x ** 3

@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


if __name__ == "__main__":
    help(calc_cube)
    for param in sys.argv:
        calc_cube(param)
