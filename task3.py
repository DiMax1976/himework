# Написать декоратор для логирования типов позиционных аргументов функции, например:

# def type_logger...
#  .....


# @type_logger
# def calc_cube(x):
# return x ** 3

# >>> a = calc_cube(5)
# 5: <class 'int'>

# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения функции?
# Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя
# функции, например, в виде:

# >> a = calc_cube(5)
# calc_cube(5: <class 'int'>)
import sys
from functools import wraps


def type_logger(callback):
    @wraps(callback)
    def wrapper(*args):
        for item in args:
            type_x = callback(item)
            type_c2 = type_x[0]
            type_c3 = type_x[1]
            type_c4 = str(callback.__name__)
            type_c5 = type(type_c3)
            result_log = type_c4 + '(' + str(type_c2) + ': ' + str(type_c5) + ')'
            print(result_log, sep=", ", end=", ")
        return type_c3

    return wrapper


@type_logger
def calc_cube(*args):
    '''_Help'''
    for x in args:
        return x, x ** 3


# a = calc_cube ( 5 )
# print ( a )
# a = calc_cube ( 5.6 )
# print ( a )
# a = calc_cube ( 2 )
# print ( a )

if __name__ == "__main__":
    for param in sys.argv:
        calc_cube(param)
