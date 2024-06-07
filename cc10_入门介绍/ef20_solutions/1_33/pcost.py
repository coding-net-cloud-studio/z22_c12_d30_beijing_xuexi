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
    with open(filename, "rt") as f:
        # 创建csv阅读器对象
        rows = csv.reader(f)
        # 读取并跳过表头行
        headers = next(rows)
        # 遍历文件的每一行
        for row in rows:
            try:
                # 将行中的第二个元素转换为整数,代表股份数量
                nshares = int(row[1])
                # 将行中的第三个元素转换为浮点数,代表每股价格
                price = float(row[2])
                # 计算当前行的成本并累加到总成本
                total_cost += nshares * price
            # 捕获int()和float()转换过程中的错误
            except ValueError:
                # 如果转换失败,打印出错的行
                print("Bad row:", row)

    # 返回计算出的总成本
    return total_cost


# 导入sys模块,用于处理命令行参数
import sys

# 检查命令行参数的数量
if len(sys.argv) == 2:
    # 如果有命令行参数,使用第一个参数作为文件名
    filename = sys.argv[1]
else:
    # 如果没有命令行参数,提示用户输入文件名
    filename = input("请输入文件名:")

# 调用portfolio_cost 函数计算总成本
cost = portfolio_cost(filename)
# 打印出总成本
print("总成本:", cost)
