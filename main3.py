from tools import *


def func(pro):
    """func_doc"""
    p, q, r, s = pro[0], pro[1], pro[2], pro[3]
    return p & q & r & s


if __name__ == '__main__':
    count = 4
    calculator = Calculator(count, func)
    calculator.print_table()
    calculator.print_normal_from()
