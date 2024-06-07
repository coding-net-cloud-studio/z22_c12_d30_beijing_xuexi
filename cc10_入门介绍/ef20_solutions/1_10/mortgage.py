#!/usr/bin/env python
# mortgage.py

# 定义贷款金额
principal = 500000.0
# 定义年利率
rate = 0.05
# 定义每月还款额
payment = 2684.11
# 定义已还金额
total_paid = 0.0
# 定义月份
month = 0

# 定义额外还款金额
extra_payment = 1000.0
# 定义额外还款开始月份
extra_payment_start_month = 61
# 定义额外还款结束月份
extra_payment_end_month = 108

# 当贷款金额大于0时
while principal > 0:
    # 月份加1
    month = month + 1
    # 计算每月还款额
    principal = principal * (1 + rate / 12) - payment
    # 累加已还金额
    total_paid = total_paid + payment

    # 当月份在额外还款开始月份和结束月份之间时
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        # 计算额外还款额
        principal = principal - extra_payment
        # 累加已还金额
        total_paid = total_paid + extra_payment

    # 打印月份,已还金额,贷款金额
    print(month, round(total_paid, 2), round(principal, 2))

# 打印已还金额
print("Total paid", round(total_paid, 2))
# 打印月份
print("Months", month)
