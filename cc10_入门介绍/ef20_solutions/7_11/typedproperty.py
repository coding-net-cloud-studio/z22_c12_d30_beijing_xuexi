#!/usr/bin/env python
# typedproperty.py


# 定义一个装饰器函数typedproperty,用于创建类型受限的属性
def typedproperty(name, expected_type):
    # 创建私有属性名
    private_name = "_" + name

    # 使用@property装饰器定义getter方法
    @property
    def prop(self):
        # 返回私有属性的值
        return getattr(self, private_name)

    # 使用@prop.setter装饰器定义setter方法
    @prop.setter
    def prop(self, value):
        # 检查传入的值是否为期望的类型,如果不是则抛出TypeError异常
        if not isinstance(value, expected_type):
            raise TypeError(f"期望的类型是 {expected_type}")
        # 设置私有属性的值
        setattr(self, private_name, value)

    # 返回属性装饰器
    return prop


# 定义三个lambda函数,分别用于创建字符串,整数和浮点数类型的属性
String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)

# 示例:使用typedproperty定义一个Stock类
if __name__ == "__main__":

    class Stock:
        # 使用typedproperty定义name属性为字符串类型
        name = typedproperty("name", str)
        # 使用typedproperty定义shares属性为整数类型
        shares = typedproperty("shares", int)
        # 使用typedproperty定义price属性为浮点数类型
        price = typedproperty("price", float)

        # 构造函数初始化实例属性
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price

    # 示例:使用lambda函数定义一个Stock2类,效果与Stock类相同
    class Stock2:
        name = String("name")
        shares = Integer("shares")
        price = Float("price")

        # 构造函数初始化实例属性
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price
