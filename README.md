# 如何使用该项目

```python
# 导入主要功能模块
from tools import *


# 写上所需要计算的函数, 文档注释建议写上，后续直接打印出来
def func(pro):
    """func_doc"""
    p, q, r, s = pro[0], pro[1], pro[2], pro[3]
    return p & q & r & s


# 程序入口
if __name__ == '__main__':
    # 参数数量(p, q, r, s)
    count = 4

    # 照做，别问为什么
    calculator = Calculator(count, func)

    # 打印真值表
    # 如果写上了文档注释，就这样调用
    calculator.print_table()
    # 如果没写文档注释，就这样调用
    # calculator.print_table("func_name")

    # 打印范式相关
    calculator.print_normal_from()

```