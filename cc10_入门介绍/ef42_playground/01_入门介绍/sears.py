#!/usr/bin/env python
# 定义账单厚度(以米为单位),0.11毫米转换为米
bill_thickness = 0.11 * 0.001

# 定义西尔斯大厦的高度(以米为单位)
sears_height = 442

# 初始化账单数量和天数
num_bills = 1
day = 1

# 当累积的账单厚度小于西尔斯大厦的高度时,继续循环
while num_bills * bill_thickness < sears_height:
    # 打印当前天数,账单数量以及累积的账单厚度
    print(day, num_bills, num_bills * bill_thickness)

    # 天数加1
    day = day + 1

    # 账单数量翻倍
    num_bills = num_bills * 2

# 循环结束后,打印总天数,总账单数量以及最终累积的账单厚度
print("Number of days", day)
print("Number of bills", num_bills)
print("Final height", num_bills * bill_thickness)
