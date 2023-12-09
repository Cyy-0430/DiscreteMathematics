# <div align="center">离散数学实验</div>

## 一、如何使用该项目
1. 先点击页面右上角的**Star**和**Fork**，给予我一点小小的帮助
2. 如果你安装了**Git**，可以直接用以下的命令来调用
```bash
git clone https://github.com/Cyy-0430/DiscreteMathematics.git
```
3. 如果没有安装**Git**, 那就点击页面的**Code**然后选择**Download ZIP**便可以直接使用
4. 要求环境在[**Python>=3.7.0**](https://www.python.org/)内运行，因为存在大量的**f格式化字符串**不兼容之前的版本

## 二、快速使用
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

## 三、如何编写函数
* 代码核心依靠**位运算**
* **P ∧ Q** 在该代码里是`p & q`
* **P ∨ Q** 在该代码里是`p | q`
* **￢ P** 在该代码里是`bit_not(p)`
* **P -> Q** 在该代码里是`contain(p, q)`
* **P <-> Q** 在该代码里是`iff(p, q)`