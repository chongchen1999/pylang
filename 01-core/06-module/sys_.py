import sys
from fibo.fibo import fib

if __name__ == "__main__":
    print(sys.argv)
    print(sys.path)

    print(fib(100))
    print(dir(fib))