# 定义 __all__ 来控制 `from math_utils import *` 的行为
__all__ = ["areas", "volumes"]

from . import areas
from . import volumes

# 包级别的初始化代码（可选）
print("math_utils 包已加载")