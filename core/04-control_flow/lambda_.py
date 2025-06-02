# map() 示例
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # 输出: [1, 4, 9, 16]

# filter() 示例
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # 输出: [2, 4]

# sorted() 示例
pairs = [(1, "one"), (2, "two"), (3, "three")]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])

# 输出: [(1, "one"), (3, "three"), (2, "two")]
print(sorted_pairs)
