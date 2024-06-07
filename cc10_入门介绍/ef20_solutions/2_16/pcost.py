#!/usr/bin/env python
# pcost.py

# 导入csv模块,用于读取CSV文件
import csv


# 定义一个函数portfolio_cost,参数为文件名
def portfolio_cost(filename):
    """
    计算投资组合文件的总成本(股份*价格)
    """
    # 初始化总成本为0.0
    total_cost = 0.0

    # 使用with语句打开文件,确保文件使用后正确关闭
    with open(filename) as f:
        # 创建csv阅读器对象
        rows = csv.reader(f)
        # 读取并存储文件的表头
        headers = next(rows)
        # 遍历文件的每一行
        for rowno, row in enumerate(rows, start=1):
            # 将表头和当前行的值组合成字典
            record = dict(zip(headers, row))
            try:
                # 尝试将股份转换为整数,价格转换为浮点数
                nshares = int(record["shares"])
                price = float(record["price"])
                # 计算当前行的成本并累加到总成本
                total_cost += nshares * price
            # 捕获int()和float()转换中的错误
            except ValueError:
                # 打印出错行的信息
                print(f"第{rowno}行:错误行:{row}")

    # 返回计算出的总成本
    return total_cost


# 导入sys模块,用于处理命令行参数
import sys

# 检查命令行参数的数量
if len(sys.argv) == 2:
    # 如果提供了文件名参数,则使用该文件名
    filename = sys.argv[1]
else:
    # 否则提示用户输入文件名
    filename = input("请输入文件名:")

# 调用portfolio_cost 函数并传入文件名,计算总成本
cost = portfolio_cost(filename)
# 打印总成本结果
print("总成本:", cost)
