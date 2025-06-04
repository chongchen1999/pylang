import sys

def demo_std_file():
    print(sys.stdout)
    print("Hello, World!", file=sys.stderr)

def demo_file_write():
    with open('test.txt', 'w') as f:
        f.write("Hello, World!\n")
        print(f.tell(), file=f)

        f.write("This is a test file.\n")
        print(f.tell(), file=f)


if __name__ == "__main__":
    demo_file_write()