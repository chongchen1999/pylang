from enum import Enum
from dataclasses import dataclass

# 示例1: 匹配字面值和通配符
def handle_http_status(status: int) -> str:
    match status:
        case 200:
            return "OK"
        case 400 | 404:
            return "Bad request or Not found"
        case 500:
            return "Server error"
        case _:
            return "Unknown status"

# 示例2: 解构元组/列表
def analyze_point(point: tuple) -> str:
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"On Y axis at {y}"
        case (x, 0):
            return f"On X axis at {x}"
        case (x, y) if x == y:
            return f"On diagonal ({x}, {y})"
        case (x, y):
            return f"Regular point ({x}, {y})"
        case _:
            return "Not a point"

# 示例3: 匹配类对象
@dataclass
class Point:
    x: int
    y: int

def describe_point(p: Point) -> str:
    match p:
        case Point(0, 0):
            return "Origin"
        case Point(0, y):
            return f"Y={y}"
        case Point(x, 0):
            return f"X={x}"
        case Point(x, y) if abs(x) == abs(y):
            return f"Diagonal point ({x}, {y})"
        case Point():
            return "Somewhere else"

# 示例4: 嵌套模式和序列解包
def process_points(points: list[Point]) -> str:
    match points:
        case []:
            return "No points"
        case [Point(0, 0)]:
            return "Only the origin"
        case [Point(x1, y1), Point(x2, y2)] if x1 == x2:
            return f"Vertical line at x={x1}"
        case [first, *rest]:
            return f"First point is {first}, then {len(rest)} more"

# 示例5: 匹配字典和枚举
class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

def describe_color(color: Color) -> str:
    match color:
        case Color.RED:
            return "Hot red"
        case Color.GREEN:
            return "Natural green"
        case Color.BLUE:
            return "Cool blue"

def extract_config(config: dict) -> str:
    match config:
        case {"type": "server", "port": int(port)}:
            return f"Server on port {port}"
        case {"type": "client", "id": id}:
            return f"Client #{id}"
        case _:
            return "Unknown config"

# 测试所有示例
if __name__ == "__main__":
    print("HTTP Status Examples:")
    print(handle_http_status(200))      # OK
    print(handle_http_status(404))      # Bad request or Not found
    print(handle_http_status(999))      # Unknown status

    print("\nPoint Analysis Examples:")
    print(analyze_point((0, 0)))        # Origin
    print(analyze_point((0, 5)))        # On Y axis at 5
    print(analyze_point((3, 3)))        # On diagonal (3, 3)

    print("\nClass Matching Examples:")
    print(describe_point(Point(0, 0)))  # Origin
    print(describe_point(Point(3, -3))) # Diagonal point (3, -3)

    print("\nNested Patterns Examples:")
    print(process_points([]))                                   # No points
    print(process_points([Point(0, 0), Point(0, 5)]))          # Vertical line at x=0

    print("\nEnum and Dict Examples:")
    print(describe_color(Color.GREEN))                         # Natural green
    print(extract_config({"type": "server", "port": 8080}))    # Server on port 8080