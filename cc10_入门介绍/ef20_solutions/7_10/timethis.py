#!/usr/bin/env python
# timethis.py

import time


# 定义一个装饰器函数timethis,用来计算函数执行时间
def timethis(func):
    def wrapper(*args, **kwargs):
        start = time.time()  # 记录开始时间
        try:
            return func(*args, **kwargs)  # 执行函数
        finally:
            end = time.time()  # 记录结束时间
            print(
                "%s.%s : %f" % (func.__module__, func.__name__, end - start)
            )  # 打印函数执行时间

    return wrapper


if __name__ == "__main__":

    @timethis  # 使用装饰器timethis装饰函数countdown
    def countdown(n):
        while n > 0:  # 倒计时代码
            n -= 1

    countdown(1000000)  # 执行countdown函数,参数为1000000
