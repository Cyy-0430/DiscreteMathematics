from tools import *


def func1(pro):
    """￢p->(q∧r)"""
    p, q, r = pro[0], pro[1], pro[2]
    return contain(bit_not(p), q & r)


def func2(pro):
    """￢p->(q∨r)"""
    p, q, r = pro[0], pro[1], pro[2]
    return contain(bit_not(p), q | r)


def func3(pro):
    """￢q->(p∧r)"""
    p, q, r = pro[0], pro[1], pro[2]
    return contain(bit_not(q), p & r)


if __name__ == '__main__':
    count = 3

    # a = init(count)
    #
    # r1 = calc(a, func1)
    #
    # print_table(a, r1, "￢p->(q∧r)的真值表")
    # print_normal_from(r1)
    #
    # r2 = calc(a, func2)
    #
    # print_table(a, r2, "￢p->(q∨r)的真值表")
    # print_normal_from(r2)
    #
    # r3 = calc(a, func3)
    #
    # print_table(a, r3, "￢q->(p∧r)的真值表")
    # print_normal_from(r3)

    calculator1 = Calculator(count, func1)
    calculator1.print_table("￢p->(q∧r)的真值表")
    calculator1.print_normal_from()

    calculator2 = Calculator(count, func2)
    calculator2.print_table("￢p->(q∨r)的真值表")
    calculator2.print_normal_from()

    calculator3 = Calculator(count, func3)
    calculator3.print_table("￢q->(p∧r)的真值表")
    calculator3.print_normal_from()

