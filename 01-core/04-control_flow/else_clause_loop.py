for n in range(2, 10):
    x = 2
    while x < n:
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        x += 1
    else:
        # 循环到底未找到一个因数
        print(n, 'is a prime number')