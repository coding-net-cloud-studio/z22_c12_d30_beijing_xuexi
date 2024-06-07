#!/usr/bin/env python
# tableformat.py


# 定义一个基础的表格格式化类
class TableFormatter:
    # 输出表头的方法,具体实现在子类中
    def headings(self, headers):
        """
        输出表格的表头
        """
        raise NotImplementedError()

    # 输出单行数据的方法,具体实现在子类中
    def row(self, rowdata):
        """
        输出表格的单行数据
        """
        raise NotImplementedError()


# 定义一个文本格式的表格格式化类,继承自基础类
class TextTableFormatter(TableFormatter):
    """
    以纯文本格式输出数据.
    """

    # 实现表头输出方法
    def headings(self, headers):
        for h in headers:
            print(f"{h:>10s}", end=" ")  # 格式化输出每个表头,右对齐
        print()  # 换行
        print(("-" * 10 + " ") * len(headers))  # 输出分隔线

    # 实现单行数据输出方法
    def row(self, rowdata):
        for d in rowdata:
            print(f"{d:>10s}", end=" ")  # 格式化输出每行数据,右对齐
        print()  # 换行


# 定义一个CSV格式的表格格式化类,继承自基础类
class CSVTableFormatter(TableFormatter):
    """
    以CSV格式输出数据.
    """

    # 实现表头输出方法
    def headings(self, headers):
        print(",".join(headers))  # 使用逗号连接表头并输出

    # 实现单行数据输出方法
    def row(self, rowdata):
        print(",".join(rowdata))  # 使用逗号连接每行数据并输出


# 定义一个HTML格式的表格格式化类,继承自基础类
class HTMLTableFormatter(TableFormatter):
    """
    以HTML格式输出数据.
    """

    # 实现表头输出方法
    def headings(self, headers):
        print("<tr>", end="")  # 开始一个表格行
        for h in headers:
            print(f"<th>{h}</th>", end="")  # 输出表头单元格
        print("</tr>")  # 结束表格行

    # 实现单行数据输出方法
    def row(self, rowdata):
        print("<tr>", end="")  # 开始一个表格行
        for d in rowdata:
            print(f"<td>{d}</td>", end="")  # 输出行数据单元格
        print("</tr>")  # 结束表格行


# 定义一个自定义异常类,用于处理未知的表格格式
class FormatError(Exception):
    pass


# 根据指定的格式名称创建相应的格式化对象
def create_formatter(name):
    """
    根据给定的输出格式名称创建适当的格式化程序
    """
    if name == "txt":
        return TextTableFormatter()
    elif name == "csv":
        return CSVTableFormatter()
    elif name == "html":
        return HTMLTableFormatter()
    else:
        raise FormatError(f"未知的表格格式 {name}")


# 打印表格的主函数,接收对象列表,列名和格式化对象作为参数
def print_table(objects, columns, formatter):
    """
    从对象列表和属性名称列表制作格式化的表格.
    """
    formatter.headings(columns)  # 输出表头
    for obj in objects:
        rowdata = [str(getattr(obj, name)) for name in columns]  # 获取每行数据
        formatter.row(rowdata)  # 输出每行数据
