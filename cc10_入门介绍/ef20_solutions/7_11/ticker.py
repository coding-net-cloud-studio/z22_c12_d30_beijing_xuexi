#!/usr/bin/env python
# ticker.py

# 导入所需的模块
import csv
import report
import tableformat
from follow import follow


# 定义一个函数,用于从数据行中选择指定的列
def select_columns(rows, indices):
    for row in rows:
        # 使用列表推导式,根据索引选择列
        yield [row[index] for index in indices]


# 定义一个函数,用于将数据行的值转换为指定的类型
def convert_types(rows, types):
    for row in rows:
        # 使用zip函数将类型转换函数和数据值配对,并应用转换
        yield [func(val) for func, val in zip(types, row)]


# 定义一个函数,用于将数据行转换为字典
def make_dicts(rows, headers):
    # 使用zip函数将表头和数据行配对,然后创建字典
    return (dict(zip(headers, row)) for row in rows)


# 定义一个函数,用于解析股票数据
def parse_stock_data(lines):
    rows = csv.reader(lines)  # 创建CSV阅读器
    rows = select_columns(rows, [0, 1, 4])  # 选择特定的列
    rows = convert_types(rows, [str, float, float])  # 转换列的类型
    rows = make_dicts(rows, ["name", "price", "change"])  # 将行转换为字典
    return rows


# 定义主函数ticker,用于处理股票数据的显示
def ticker(portfile, logfile, fmt):
    portfolio = report.read_portfolio(portfile)  # 读取投资组合文件
    lines = follow(logfile)  # 跟踪日志文件的变化
    rows = parse_stock_data(lines)  # 解析股票数据
    rows = (row for row in rows if row["name"] in portfolio)  # 过滤出投资组合中的股票
    formatter = tableformat.create_formatter(fmt)  # 创建格式化对象
    formatter.headings(["Name", "Price", "Change"])  # 设置表头
    for row in rows:
        # 格式化并输出每一行数据
        formatter.row([row["name"], f"{row['price']:0.2f}", f"{row['change']:0.2f}"])


# 定义程序的主入口
def main(args):
    # 检查命令行参数的数量是否正确
    if len(args) != 4:
        raise SystemExit("用法:%s 投资组合文件 日志文件 格式" % args[0])
    ticker(args[1], args[2], args[3])  # 调用ticker函数


# 当脚本被直接运行时,执行main函数
if __name__ == "__main__":
    import sys

    main(sys.argv)
