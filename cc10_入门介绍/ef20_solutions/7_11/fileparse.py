#!/usr/bin/env python
# fileparse.py
import csv


# 定义一个函数 parse_csv,用于解析 CSV 文件
def parse_csv(
    lines,
    select=None,
    types=None,
    has_headers=True,
    delimiter=",",
    silence_errors=False,
):
    """
    解析 CSV 文件,将其转换为具有类型转换的记录列表.
    """
    # 如果选择了特定列,但没有列头,则引发运行时错误
    if select and not has_headers:
        raise RuntimeError("select 需要列头")

    # 使用指定的分隔符读取 CSV 行
    rows = csv.reader(lines, delimiter=delimiter)

    # 读取文件头(如果有)
    headers = next(rows) if has_headers else []

    # 如果选择了特定列,为过滤设置索引并设置输出列
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select

    # 初始化记录列表
    records = []
    # 遍历每一行数据
    for rowno, row in enumerate(rows, 1):
        # 跳过没有数据的行
        if not row:
            continue

        # 如果选择了特定列索引,选择它们
        if select:
            row = [row[index] for index in indices]

        # 对行应用类型转换
        if types:
            try:
                # 尝试将每行的值按照指定的类型进行转换
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                # 如果转换失败且不静默错误,打印错误信息
                if not silence_errors:
                    print(f"第 {rowno} 行:无法转换 {row}")
                    print(f"第 {rowno} 行:原因 {e}")
                continue

        # 根据是否有列头,创建字典或元组
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        # 将记录添加到记录列表中
        records.append(record)

    # 返回记录列表
    return records
