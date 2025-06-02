"""
calculator.py - 一个简单的计算器模块

这个模块提供了基本的数学运算功能，包括加法、减法、乘法和除法。
"""

class Calculator:
    """一个简单的计算器类
    
    这个类封装了基本的数学运算方法，可以用于执行简单的计算。
    
    Attributes:
        version (str): 当前计算器的版本号
    """
    
    version = "1.0"
    
    def add(self, a, b):
        """返回两个数的和
        
        Args:
            a (int or float): 第一个加数
            b (int or float): 第二个加数
            
        Returns:
            int or float: 两个数的和
            
        Examples:
            >>> calc = Calculator()
            >>> calc.add(2, 3)
            5
        """
        return a + b
    
    def subtract(self, a, b):
        """返回两个数的差
        
        Args:
            a (int or float): 被减数
            b (int or float): 减数
            
        Returns:
            int or float: 两个数的差
        """
        return a - b
    
    def multiply(self, a, b):
        """返回两个数的乘积
        
        参数:
            a (int or float): 第一个因数
            b (int or float): 第二个因数
            
        返回:
            int or float: 两个数的乘积
        """
        return a * b
    
    def divide(self, a, b):
        """返回两个数的商
        
        参数:
            a (int or float): 被除数
            b (int or float): 除数
            
        返回:
            float: 两个数的商
            
        异常:
            ValueError: 如果除数为0
            
        Examples:
            >>> calc = Calculator()
            >>> calc.divide(6, 3)
            2.0
            >>> calc.divide(5, 0)
            Traceback (most recent call last):
                ...
            ValueError: 除数不能为0
        """
        if b == 0:
            raise ValueError("除数不能为0")
        return a / b


def main():
    """主函数，演示计算器的使用"""
    calc = Calculator()
    print(f"计算器版本: {calc.version}")
    
    # 加法演示
    result = calc.add(10, 5)
    print(f"10 + 5 = {result}")
    
    # 除法演示
    try:
        result = calc.divide(10, 2)
        print(f"10 / 2 = {result}")
        result = calc.divide(10, 0)  # 这会引发异常
    except ValueError as e:
        print(f"错误: {e}")


if __name__ == "__main__":
    main()
    print(Calculator.__doc__)
    print(Calculator.add.__doc__)