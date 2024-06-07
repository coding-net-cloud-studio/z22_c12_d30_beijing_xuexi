#!/usr/bin/env python
# pcost.py

# 导入报告模块,该模块可能包含读取投资组合文件的函数
import report


# 定义函数 portfolio_cost,它接受一个文件名作为参数
def portfolio_cost(filename):
    """
    计算投资组合文件的总成本(股份*价格)
    """
    # 使用 report 模块中的 read_portfolio 函数读取投资组合文件
    portfolio = report.read_portfolio(filename)
    # 返回投资组合的总成本
    return portfolio.total_cost


# 定义主函数 main,它接受命令行参数
def main(args):
    # 检查参数数量是否正确,如果不正确则抛出异常
    if len(args) != 2:
        raise SystemExit("用法:%s 投资组合文件" % args[0])
    # 获取投资组合文件的名称
    filename = args[1]
    # 打印投资组合的总成本
    print("总成本:", portfolio_cost(filename))


# 当脚本被直接运行时,执行主函数
if __name__ == "__main__":
    # 导入系统模块以获取命令行参数
    import sys

    # 调用主函数并传入命令行参数
    main(sys.argv)
