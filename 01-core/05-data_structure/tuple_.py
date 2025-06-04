import sys
import timeit

# ============================================
# 元组基础特性和不可变性演示
# ============================================

# 1. 元组的创建
empty_tuple = ()  # 空元组
single_element_tuple = (42,)  # 单元素元组(注意逗号)
multiple_elements = (1, "Python", 3.14, True)  # 多类型元素
nested_tuple = ((1, 2), [3, 4], {"name": "Alice"})  # 嵌套其他容器

print("创建的元组:")
print(f"空元组: {empty_tuple}")
print(f"单元素元组: {single_element_tuple}")
print(f"多元素元组: {multiple_elements}")
print(f"嵌套元组: {nested_tuple}")
print("-" * 50)

# 2. 元组的不可变性演示
try:
    multiple_elements[1] = "Java"  # 尝试修改元组元素
except TypeError as e:
    print(f"尝试修改元组出错: {e}")

# 但元组中的可变对象(如列表)可以修改
nested_tuple[1].append(5)
print(f"修改嵌套元组中的列表后: {nested_tuple}")
print("-" * 50)

# ============================================
# 元组的优势和使用场景
# ============================================

# 3. 作为字典键(因为不可变)
locations = {(35.6895, 139.6917): "Tokyo", (40.7128, -74.0060): "New York"}
print("使用元组作为字典键:")
print(f"东京坐标: {locations[(35.6895, 139.6917)]}")
print("-" * 50)


# 4. 函数返回多个值
def get_user_info():
    return ("Alice", 30, "alice@example.com")  # 返回元组


name, age, email = get_user_info()  # 元组解包
print("函数返回元组并解包:")
print(f"姓名: {name}, 年龄: {age}, 邮箱: {email}")
print("-" * 50)

# 5. 保护数据不被修改
CONFIG = (
    "localhost",  # 主机
    8080,  # 端口
    True,  # 调试模式
)

# 尝试"修改"配置实际上会创建新元组
new_config = CONFIG + ("/api",)  # 拼接操作返回新元组
print("配置保护演示:")
print(f"原始配置: {CONFIG}")
print(f"新配置: {new_config}")
print("-" * 50)

# 6. 性能比较: 元组 vs 列表

list_data = [1, 2, 3, 4, 5]
tuple_data = (1, 2, 3, 4, 5)

print("元组与列表性能比较:")
print(f"列表占用内存: {sys.getsizeof(list_data)} 字节")
print(f"元组占用内存: {sys.getsizeof(tuple_data)} 字节")

list_time = timeit.timeit("x[2]", "x=[1,2,3,4,5]", number=1000000)
tuple_time = timeit.timeit("x[2]", "x=(1,2,3,4,5)", number=1000000)
print(f"100万次元素访问 - 列表: {list_time:.6f} 秒")
print(f"100万次元素访问 - 元组: {tuple_time:.6f} 秒")
print("-" * 50)

# 7. 元组方法演示
sample_tuple = (1, 2, 2, 3, 4, 2)
print("元组方法演示:")
print(f"元素2出现的次数: {sample_tuple.count(2)}")
print(f"元素3的索引位置: {sample_tuple.index(3)}")
print("-" * 50)


# 8. 不可变性的实际意义
def process_data(data):
    # 假设这是一个复杂的处理函数
    # 使用元组可以确保输入数据不会被意外修改
    return sum(data) / len(data)


data_points = (10, 20, 30, 40)
print("不可变性保证数据安全:")
print(f"平均值: {process_data(data_points)}")
print(f"原始数据未被修改: {data_points}")

# ============================================
# 何时使用元组 vs 列表
# ============================================

"""
选择元组当:
- 数据不应该被修改
- 需要作为字典键
- 作为函数参数或返回值
- 需要性能优化

选择列表当:
- 数据需要频繁修改
- 需要动态添加/删除元素
- 需要使用丰富的方法(sort, append等)
"""
