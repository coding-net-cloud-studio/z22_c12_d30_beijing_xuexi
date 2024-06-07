#!/usr/bin/env python
# bounce.py

# 初始化高度和反弹次数
height = 100
bounce = 1

# 当反弹次数小于等于10时,执行循环
while bounce <= 10:
    # 计算新的高度(每次反弹高度乘以3/5)
    height = height * (3 / 5)
    # 打印反弹次数和四舍五入后的高度
    print(bounce, round(height, 4))
    # 反弹次数加1
    bounce += 1
