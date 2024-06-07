#!/usr/bin/env python
# stock.py

# 导入typedproperty模块,用于定义类型化属性
from typedproperty import String, Integer, Float


# 定义一个表示股票持有量的类
class Stock:
    """
    一个股票持有量实例,包括名称,股份和价格.
    """

    # 使用类型化属性定义类属性
    name = String("name")  # 股票名称
    shares = Integer("shares")  # 股份数量
    price = Float("price")  # 股票价格

    # 构造函数,初始化股票对象
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    # 返回对象的字符串表示形式
    def __repr__(self):
        return f"Stock({self.name!r}, {self.shares!r}, {self.price!r})"

    # 定义一个只读属性cost,计算持有成本(股份*价格)
    @property
    def cost(self):
        """
        返回成本,即股份乘以价格
        """
        return self.shares * self.price

    # 定义一个方法sell,卖出一定数量的股份并返回剩余股份数量
    def sell(self, nshares):
        """
        卖出一定数量的股份,并返回剩余的股份数量.
        """
        self.shares -= nshares
