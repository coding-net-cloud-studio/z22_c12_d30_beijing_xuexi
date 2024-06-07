#!/usr/bin/env python
# report.py

import fileparse  # 导入文件解析模块
from stock import Stock  # 导入股票类
from portfolio import Portfolio  # 导入投资组合类
import tableformat  # 导入表格格式化模块


# 读取投资组合文件并返回一个投资组合对象列表
def read_portfolio(filename, **opts):
    """
    从CSV文件中读取股票投资组合数据,返回一个字典列表,包含名称,股份和价格.
    """
    with open(filename) as lines:  # 打开文件
        return Portfolio.from_csv(
            lines, **opts
        )  # 使用Portfolio 类的静态方法从 CSV 数据中创建投资组合


# 读取价格文件并返回一个映射股票名称到价格的字典
def read_prices(filename, **opts):
    """
    从CSV文件中读取价格数据,返回一个将名称映射到价格的字典.
    """
    with open(filename) as lines:  # 打开文件
        return dict(
            fileparse.parse_csv(lines, types=[str, float], has_headers=False, **opts)
        )  # 解析CSV文件并创建字典


# 根据投资组合列表和价格字典生成报告数据
def make_report(portfolio, prices):
    """
    给定投资组合列表和价格字典,生成一个(名称, 股份, 价格, 变动)元组的列表.
    """
    rows = []  # 初始化空列表以存储报告行
    for s in portfolio:  # 遍历投资组合中的每支股票
        current_price = prices[s.name]  # 获取当前价格
        change = current_price - s.price  # 计算价格变动
        summary = (
            s.name,
            s.shares,
            current_price,
            change,
        )  # 创建一个包含所需信息的元组
        rows.append(summary)  # 将元组添加到报告行列表中
    return rows  # 返回报告行列表


# 打印格式化的报告表
def print_report(reportdata, formatter):
    """
    从(名称, 股份, 价格, 变动)元组的列表中打印出格式化的表格.
    """
    formatter.headings(["Name", "Shares", "Price", "Change"])  # 设置表头
    for name, shares, price, change in reportdata:  # 遍历报告数据
        rowdata = [
            name,
            str(shares),
            f"{price:0.2f}",
            f"{change:0.2f}",
        ]  # 准备每行的数据
        formatter.row(rowdata)  # 打印行数据


# 生成股票报告
def portfolio_report(portfoliofile, pricefile, fmt="txt"):
    """
    给定投资组合和数据文件,生成股票报告.
    """
    # 读取数据文件
    portfolio = read_portfolio(portfoliofile)  # 读取投资组合文件
    prices = read_prices(pricefile)  # 读取价格文件

    # 创建报告数据
    report = make_report(portfolio, prices)  # 使用投资组合和价格数据生成报告

    # 打印报告
    formatter = tableformat.create_formatter(fmt)  # 根据指定的格式创建格式化器
    print_report(report, formatter)  # 使用格式化器打印报告


# 主函数,用于处理命令行参数和执行报告生成
def main(args):
    if len(args) != 4:  # 检查参数数量是否正确
        raise SystemExit(
            "Usage: %s portfile pricefile format" % args[0]
        )  # 参数不正确时抛出异常
    portfolio_report(args[1], args[2], args[3])  # 调用 portfolio_report 函数生成报告


# 当脚本被直接执行时,调用 main 函数
if __name__ == "__main__":
    import sys  # 导入系统模块以获取命令行参数

    main(sys.argv)  # 调用 main 函数并传入命令行参数
