from typing import *

# 自定义类型标注
Bit = int
Params = List[List[Bit]]
Result = List[Bit]
NormalFrom = Dict[str, List[Bit]]
Function = Callable[[List[Bit]], Bit]


def bit_not(_p: Bit) -> Bit:
    """按位或"""
    return ~_p & 1


def contain(_p: Bit, _q: Bit) -> Bit:
    """蕴含"""
    return bit_not(_p) | _q  # 蕴含等值律 P -> Q == !P | Q


def iff(_p: Bit, _q: Bit) -> Bit:
    """当且仅当"""
    return bit_not(_p ^ _q)


def judge(result: Result) -> str:
    """ 永假 永真 可满足"""
    ans = result[0]
    if ans == 0:
        for i in range(1, len(result)):
            if result[i] == 1:
                return "可满足式"
        return "永假式"

    else:
        for i in range(1, len(result)):
            if result[i] == 0:
                return "可满足式"
        return "永真式"


def normal_from(result: Result) -> NormalFrom:
    """获得主吸取范式和主合取范式"""
    ans = {"m": [], "M": []}
    for i, val in enumerate(result):
        if val == 0:
            ans["M"].append(i)
        else:
            ans["m"].append(i)
    return ans


def print_normal_from(result: Result) -> NoReturn:
    """获得主吸取范式和主合取范式"""
    ans = normal_from(result)
    print(f"范式类型为：{judge(result)}")

    print(f"主吸取范式：", end="")
    temp = ""
    for val in ans["m"]:
        print(temp, end="")
        print("m" + str(val), end="")
        temp = " ∨ "

    print(f"\n主合取范式：", end="")
    temp = ""
    for val in ans["M"]:
        print(temp, end="")
        print("M" + str(val), end="")
        temp = " ∧ "
    print()


def print_table(a: Params, result: Result, name: str) -> NoReturn:
    """打印真值表"""
    chars = "PQRSTUVWXYZ"
    for char in chars[0: len(a[0])]:
        print(char, end="\t")
    print(name)

    for i, pro in enumerate(a):
        for j, val in enumerate(pro):
            print(val, end="\t")
        print(f"{result[i]}")


def init(count: int) -> Params:
    """初始化p q r"""
    if count > 11:
        raise Exception("count大小不能超过11")

    all = 1 << count
    a = []
    for num in range(all):
        # mask
        pro = []
        for _ in range(count):
            p = num & 1
            pro.insert(0, p)
            num = num >> 1
        a.append(pro)
    return a


def calc(a: Params, func: Function) -> Result:
    """计算结果"""
    result = []
    for pro in a:
        res = func(pro)
        result.append(res)
    return result


class Calculator:
    def __init__(self, count: int, func: Function):
        self.__a = init(count)
        self.__result = calc(self.__a, func)
        self.__doc = func.__doc__

    def print_table(self, name: str = "result") -> NoReturn:
        """打印真值表"""
        if self.__doc is not None:
            name = self.__doc
        print_table(self.__a, self.__result, name)

    def print_normal_from(self) -> NoReturn:
        """获得主吸取范式和主合取范式"""
        print_normal_from(self.__result)


if __name__ == '__main__':
    bit_not_test = Calculator(1, lambda pro: bit_not(pro[0]))
    bit_not_test.print_table("bit_not")
    print("\n")

    contain_test = Calculator(2, lambda pro: contain(pro[0], pro[1]))
    contain_test.print_table("contain")
    print("\n")

    iff_test = Calculator(2, lambda pro: iff(pro[0], pro[1]))
    iff_test.print_table("iff")
