def create_user(name, age, email, country="China", role="member"):
    print(f"创建用户: {name}")
    print(f"年龄: {age}")
    print(f"邮箱: {email}")
    print(f"国家: {country}")
    print(f"角色: {role}")
    print("-" * 30)


# 直接传递参数
create_user("张三", 25, "zhangsan@example.com")
create_user("李四", 30, "lisi@example.com", "USA", "admin")

# 参数存储在元组中
user1 = ("王五", 28, "wangwu@example.com")
create_user(*user1)  # 等价于 create_user("王五", 28, "wangwu@example.com")

# 参数存储在列表中
user2 = ["赵六", 35, "zhaoliu@example.com", "UK"]

# 等价于 create_user("赵六", 35, "zhaoliu@example.com", "UK")
create_user(*user2)

# 参数存储在字典中
user3 = {
    "name": "钱七",
    "age": 40,
    "email": "qianqi@example.com",
    "role": "manager",
}
create_user(**user3)
# 等价于 create_user(name="钱七", age=40, email="qianqi@example.com", role="manager")

# 混合使用位置参数和字典参数
user4 = {"age": 22, "email": "sunba@example.com", "country": "Japan"}
create_user("孙八", **user4)
# 等价于 create_user("孙八", age=22, email="sunba@example.com", country="Japan")


def wrapper_function(*args, **kwargs):
    print("正在处理用户创建请求...")
    create_user(*args, **kwargs)
    print("用户创建完成")


# 使用元组和字典传递参数
args = ("周九", 45)
kwargs = {"email": "zhoujiu@example.com", "role": "vip"}
wrapper_function(*args, **kwargs)
