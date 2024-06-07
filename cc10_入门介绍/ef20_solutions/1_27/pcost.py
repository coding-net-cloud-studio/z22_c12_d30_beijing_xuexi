#!/usr/bin/env python
# pcost.py

# 初始化总成本变量
total_cost = 0.0

# 打开文件
with open("../../ef70_work/Data/portfolio.csv", "rt") as f:
    # 读取文件第一行
    headers = next(f)
    # 遍历文件每一行
    for line in f:
        # 分割每一行
        row = line.split(",")
        # 将第二列转换为整数
        nshares = int(row[1])
        # 将第三列转换为浮点数
        price = float(row[2])
        # 计算每一行的成本
        total_cost += nshares * price

# 输出总成本
print("Total cost", total_cost)
