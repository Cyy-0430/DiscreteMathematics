from tools import *


def func(pro):
    """(p∧q)∨(￢p∧q∧r)"""
    p, q, r = pro[0], pro[1], pro[2]
    return (p & q) | (bit_not(p) & q & r)


if __name__ == '__main__':
    count = 3
    calculator = Calculator(count, func)
    calculator.print_table("(p∧q)∨(￢p∧q∧r)")
