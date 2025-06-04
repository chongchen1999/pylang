# 3.1. Python 用作计算器

# 3.1.1. 数字
print("=== 数字运算 ===")
# 基本算术运算
print("加法:", 2 + 3)  # 输出: 5
print("减法:", 10 - 4)  # 输出: 6
print("乘法:", 5 * 6)  # 输出: 30
print("除法:", 15 / 4)  # 输出: 3.75 (浮点除法)
print("整数除法:", 15 // 4)  # 输出: 3 (整数除法)
print("取余:", 15 % 4)  # 输出: 3 (取余)
print("幂运算:", 2**8)  # 输出: 256

# 数学函数
import math

print("平方根:", math.sqrt(16))  # 输出: 4.0
print("圆周率:", math.pi)  # 输出: 3.141592653589793

# 3.1.2. 文本
print("\n=== 文本处理 ===")
# 字符串操作
greeting = "Hello"
name = "World"
message = greeting + " " + name + "!"
print(message)  # 输出: Hello World!
print("重复字符串:", "ha" * 3)  # 输出: hahaha
print("字符串长度:", len(message))  # 输出: 13

# 字符串索引和切片
text = "Python"
print("第一个字符:", text[0])  # 输出: P
print("最后一个字符:", text[-1])  # 输出: n
print("切片:", text[1:4])  # 输出: yth

# 字符串方法
print("大写:", text.upper())  # 输出: PYTHON
print("替换:", text.replace("P", "J"))  # 输出: Jython

# 3.1.3. 列表
print("\n=== 列表操作 ===")
# 列表创建和操作
fruits = ["apple", "banana", "cherry", "date"]
print("原始列表:", fruits)
print("第二个水果:", fruits[1])  # 输出: banana
print("最后两个水果:", fruits[-2:])  # 输出: ['cherry', 'date']

# 修改列表
fruits[0] = "avocado"  # 修改第一个元素
fruits.append("elderberry")  # 添加元素
print("修改后的列表:", fruits)

# 列表操作
numbers = [1, 2, 3, 4, 5]
print("数字列表:", numbers)
print("列表长度:", len(numbers))  # 输出: 5
print("列表求和:", sum(numbers))  # 输出: 15
print("最大数:", max(numbers))  # 输出: 5
print("最小数:", min(numbers))  # 输出: 1

# 列表嵌套
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("矩阵:", matrix)
print("矩阵第二行:", matrix[1])  # 输出: [4, 5, 6]
print("矩阵中心元素:", matrix[1][1])  # 输出: 5

# 3.2. 走向编程的第一步
print("\n=== 编程基础 ===")
# 条件语句
age = 18
if age < 18:
    print("未成年人")
elif age == 18:
    print("刚成年")
else:
    print("成年人")

# 循环语句
print("\n数字平方:")
for num in numbers:
    print(f"{num}的平方是{num**2}")


# 函数定义
def calculate_area(radius):
    """计算圆的面积"""
    return math.pi * radius**2


circle_radius = 5
print(f"半径为{circle_radius}的圆面积是: {calculate_area(circle_radius):.2f}")

# 列表推导式
squares = [x**2 for x in range(1, 6)]
print("1-5的平方列表:", squares)  # 输出: [1, 4, 9, 16, 25]
