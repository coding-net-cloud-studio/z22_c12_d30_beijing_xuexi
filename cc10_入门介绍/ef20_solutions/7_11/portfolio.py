#!/usr/bin/env python
# portfolio.py

# 导入文件解析模块和股票模块
import fileparse
import stock


# 定义投资组合类
class Portfolio:
    # 初始化方法,创建一个空的持仓列表
    def __init__(self):
        self._holdings = []

    # 类方法,从CSV文件中读取数据并创建投资组合实例
    @classmethod
    def from_csv(cls, lines, **opts):
        # 创建投资组合实例
        self = cls()
        # 解析CSV文件中的数据,只选择'name', 'shares', 'price'列,并指定数据类型
        portdicts = fileparse.parse_csv(
            lines, select=["name", "shares", "price"], types=[str, int, float], **opts
        )
        # 遍历解析后的字典列表,将每个字典转换为股票对象并添加到持仓列表中
        for d in portdicts:
            self.append(stock.Stock(**d))
        # 返回投资组合实例
        return self

    # 向投资组合中添加一个持仓对象
    def append(self, holding):
        self._holdings.append(holding)

    # 实现迭代器协议,允许遍历持仓列表
    def __iter__(self):
        return self._holdings.__iter__()

    # 返回持仓列表的长度
    def __len__(self):
        return len(self._holdings)

    # 通过索引获取持仓对象
    def __getitem__(self, index):
        return self._holdings[index]

    # 检查持仓列表中是否包含特定名称的股票
    def __contains__(self, name):
        return any(s.name == name for s in self._holdings)

    # 计算投资组合的总成本
    @property
    def total_cost(self):
        return sum(s.shares * s.price for s in self._holdings)

    # 统计各股票的持股数量
    def tabulate_shares(self):
        from collections import Counter

        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
