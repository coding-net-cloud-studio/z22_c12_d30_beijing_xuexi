#!/usr/bin/env python
# report.py
import csv


# 定义一个函数,用于读取股票投资组合文件,并将其转换为包含名称,股份和价格的字典列表
def read_portfolio(filename):
    """
    读取股票投资组合文件到一个字典列表,键为名称,股份和价格.
    """
    portfolio = []  # 初始化一个空列表来存储股票信息
    with open(filename) as f:  # 打开指定的文件
        rows = csv.reader(f)  # 使用csv模块的reader函数读取文件内容
        headers = next(rows)  # 读取并忽略第一行(标题行)

        for row in rows:  # 遍历文件的每一行
            stock = {  # 创建一个新的字典来存储当前行的股票信息
                "name": row[0],  # 股票名称
                "shares": int(row[1]),  # 股票股份数量
                "price": float(row[2]),  # 股票价格
            }
            portfolio.append(stock)  # 将股票字典添加到列表中

    return portfolio  # 返回股票字典列表


# 定义一个函数,用于读取价格数据文件,并将其转换为映射名称到价格的字典
def read_prices(filename):
    """
    读取CSV格式的价格数据文件到一个映射名称到价格的字典.
    """
    prices = {}  # 初始化一个空字典来存储价格信息
    with open(filename) as f:  # 打开指定的文件
        rows = csv.reader(f)  # 使用csv模块的reader函数读取文件内容
        for row in rows:  # 遍历文件的每一行
            try:
                prices[row[0]] = float(
                    row[1]
                )  # 尝试将第二列的值转换为浮点数,并存储到字典中
            except IndexError:  # 如果出现索引错误(例如,行中没有足够的列),则忽略这一行
                pass

    return prices  # 返回价格字典


# 读取股票投资组合文件
portfolio = read_portfolio("../../ef70_work/Data/portfolio.csv")
# 读取价格数据文件
prices = read_prices("../../ef70_work/Data/prices.csv")

# 计算投资组合的总成本
total_cost = 0.0
for s in portfolio:  # 遍历投资组合中的每支股票
    total_cost += s["shares"] * s["price"]  # 计算总成本:股份数量 * 价格

print("总成本", total_cost)  # 打印总成本

# 计算投资组合的当前价值
total_value = 0.0
for s in portfolio:  # 遍历投资组合中的每支股票
    total_value += s["shares"] * prices[s["name"]]  # 计算当前价值:股份数量 * 当前价格

print("当前价值", total_value)  # 打印当前价值
print("收益", total_value - total_cost)  # 打印收益(当前价值 - 总成本)
