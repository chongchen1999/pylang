import math_utils

print(dir(math_utils))

print([attr for attr in dir(math_utils.areas.circle) if not attr.startswith('__')])
print([attr for attr in dir(math_utils.volumes.sphere) if not attr.startswith('__')])


print(math_utils.areas.circle.area(5))      # 输出: 78.53981633974483
print(math_utils.volumes.sphere.volume(3))    # 输出: 113.09733552923254
