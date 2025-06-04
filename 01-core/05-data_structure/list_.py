# 5.1 列表详解


def stack_demo():
    """
    5.1.1 用列表实现堆栈
    堆栈是后进先出(LIFO)的数据结构
    """
    print("\n=== 5.1.1 用列表实现堆栈 ===")
    stack = []

    # 入栈操作 (push)
    stack.append("a")
    stack.append("b")
    stack.append("c")
    print("入栈后:", stack)  # 输出: ['a', 'b', 'c']

    # 出栈操作 (pop)
    print("出栈:", stack.pop())  # 输出: 'c'
    print("出栈:", stack.pop())  # 输出: 'b'
    print("栈剩余:", stack)  # 输出: ['a']


def queue_demo():
    """
    5.1.2 用列表实现队列
    队列是先进先出(FIFO)的数据结构
    注意: 用列表实现队列效率不高，对于频繁的队列操作建议使用collections.deque
    """
    print("\n=== 5.1.2 用列表实现队列 ===")
    queue = []

    # 入队操作 (enqueue)
    queue.append("a")
    queue.append("b")
    queue.append("c")
    print("入队后:", queue)  # 输出: ['a', 'b', 'c']

    # 出队操作 (dequeue)
    print("出队:", queue.pop(0))  # 输出: 'a'
    print("出队:", queue.pop(0))  # 输出: 'b'
    print("队列剩余:", queue)  # 输出: ['c']


def list_comprehension_demo():
    """
    5.1.3 列表推导式
    提供简洁的方式来创建列表
    """
    print("\n=== 5.1.3 列表推导式 ===")

    # 普通方式创建平方列表
    squares = []
    for x in range(10):
        squares.append(x**2)
    print("普通方式:", squares)

    # 使用列表推导式
    squares = [x**2 for x in range(10)]
    print("列表推导式:", squares)

    # 带条件的列表推导式
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    print("偶数平方:", even_squares)

    # 多个变量的列表推导式
    pairs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    print("组合对:", pairs)


def nested_list_comprehension_demo():
    """
    5.1.4 嵌套的列表推导式
    可以处理嵌套的数据结构
    """
    print("\n=== 5.1.4 嵌套的列表推导式 ===")

    # 3x4矩阵
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    print("原始矩阵:", matrix)

    # 转置矩阵
    transposed = [[row[i] for row in matrix] for i in range(4)]
    print("转置矩阵:", transposed)

    # 等价于以下代码:
    transposed = []
    for i in range(4):
        transposed.append([row[i] for row in matrix])

    # 更简单的方式是使用zip函数
    transposed_zip = list(zip(*matrix))
    print("使用zip转置:", transposed_zip)

    # 展平嵌套列表
    flattened = [num for row in matrix for num in row]
    print("展平矩阵:", flattened)


if __name__ == "__main__":
    stack_demo()
    queue_demo()
    list_comprehension_demo()
    nested_list_comprehension_demo()
