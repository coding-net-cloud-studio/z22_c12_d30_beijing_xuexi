#!/usr/bin/env python
# report.py
import csv


# 定义函数read_portfolio,用于读取股票投资组合文件
def read_portfolio(filename):
    """
    读取股票投资组合文件到一个字典列表,包含键名name,shares和price.
    """
    portfolio = []  # 初始化一个空列表用于存储股票信息
    with open(filename) as f:  # 打开文件
        rows = csv.reader(f)  # 创建CSV阅读器
        headers = next(rows)  # 读取并存储文件的头部信息

        for row in rows:  # 遍历每一行数据
            record = dict(zip(headers, row))  # 将行数据与头部信息配对成字典
            stock = {  # 创建一个新的字典存储股票信息
                "name": record["name"],
                "shares": int(record["shares"]),
                "price": float(record["price"]),
            }
            portfolio.append(stock)  # 将股票信息添加到列表中

    return portfolio  # 返回股票信息列表


# 定义函数read_prices,用于读取价格数据文件
def read_prices(filename):
    """
    读取CSV格式的价格数据文件到一个将名称映射到价格的字典.
    """
    prices = {}  # 初始化一个空字典用于存储价格信息
    with open(filename) as f:  # 打开文件
        rows = csv.reader(f)  # 创建CSV阅读器
        for row in rows:  # 遍历每一行数据
            try:
                prices[row[0]] = float(row[1])  # 将名称和价格添加到字典中
            except IndexError:  # 如果出现索引错误(例如空行)则跳过
                pass

    return prices  # 返回价格信息字典


# 定义函数make_report_data,用于根据投资组合列表和价格字典生成报告数据
def make_report_data(portfolio, prices):
    """
    根据投资组合列表和价格字典生成一个(name, shares, price, change)元组的列表.
    """
    rows = []  # 初始化一个空列表用于存储报告数据
    for stock in portfolio:  # 遍历投资组合中的每一支股票
        current_price = prices[stock["name"]]  # 获取当前价格
        change = current_price - stock["price"]  # 计算价格变化
        summary = (
            stock["name"],
            stock["shares"],
            current_price,
            change,
        )  # 创建一个包含股票信息的元组
        rows.append(summary)  # 将元组添加到报告数据列表中
    return rows  # 返回报告数据列表


# 读取数据文件并创建报告数据
portfolio = read_portfolio("../../ef70_work/Data/portfolio.csv")  # 读取投资组合文件
prices = read_prices("../../ef70_work/Data/prices.csv")  # 读取价格文件

# 生成报告数据
report = make_report_data(portfolio, prices)  # 使用投资组合和价格数据生成报告

# 输出报告
headers = ("Name", "Shares", "Price", "Change")  # 定义报告头部信息
print("%10s %10s %10s %10s" % headers)  # 打印报告头部信息
print(("-" * 10 + " ") * len(headers))  # 打印分隔线
for row in report:  # 遍历报告数据
    print("%10s %10d %10.2f %10.2f" % row)  # 打印报告数据行
