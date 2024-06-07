#!/usr/bin/env python
# follow.py

# 导入所需模块
import time
import os


# 定义一个生成器函数,用于产生被写入文件末尾的行序列
def follow(filename):
    """
    生成器,产生一个被写入文件末尾的行序列.
    """
    # 打开文件
    with open(filename, "r") as f:
        # 将文件指针移动到文件末尾
        f.seek(0, os.SEEK_END)
        # 无限循环,直到手动停止程序
        while True:
            # 读取一行内容
            line = f.readline()
            # 如果读取到的行不为空,则返回这一行
            if line != "":
                yield line
            else:
                # 如果读取到的行为空,则短暂休眠以避免忙等待
                time.sleep(0.1)
