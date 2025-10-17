"""
场景 1：基本模式匹配

应用：理解 match/case 的基础用法，包括字面量、序列、映射模式
运行要求：Python >= 3.10
"""

print("=" * 60)
print("场景 1：match/case 基本模式匹配")
print("=" * 60)

# 示例 1：字面量模式（类似传统 switch/case）
print("\n[示例 1] 字面量模式 - HTTP 状态码处理：\n")

def handle_http_status(status_code):
    """根据 HTTP 状态码返回描述"""
    match status_code:
        case 200:
            return "✅ 成功"
        case 201:
            return "✅ 已创建"
        case 400:
            return "❌ 错误的请求"
        case 404:
            return "❌ 未找到"
        case 500:
            return "❌ 服务器错误"
        case _:
            return "❓ 未知状态"

# 测试不同状态码
statuses = [200, 404, 500, 999]
for status in statuses:
    result = handle_http_status(status)
    print(f"状态码 {status}: {result}")

# 示例 2：序列模式（解构列表/元组）
print("\n[示例 2] 序列模式 - 坐标点处理：\n")

def describe_point(point):
    """描述不同维度的点"""
    match point:
        case []:
            return "空点"
        case [x]:
            return f"一维点: x={x}"
        case [x, y]:
            return f"二维点: ({x}, {y})"
        case [x, y, z]:
            return f"三维点: ({x}, {y}, {z})"
        case _:
            return f"高维点: {len(point)} 维"

# 测试不同维度的点
points = [
    [],
    [5],
    [3, 4],
    [1, 2, 3],
    [1, 2, 3, 4, 5]
]

for point in points:
    print(f"{str(point):20s} -> {describe_point(point)}")

# 示例 3：序列模式 - 特定位置匹配
print("\n[示例 3] 序列模式 - 原点和轴上的点：\n")

def classify_point(point):
    """分类二维点的位置"""
    match point:
        case [0, 0]:
            return "原点"
        case [x, 0]:
            return f"X轴上的点: x={x}"
        case [0, y]:
            return f"Y轴上的点: y={y}"
        case [x, y]:
            return f"普通点: ({x}, {y})"

# 测试特殊点
special_points = [
    [0, 0],
    [5, 0],
    [0, 3],
    [2, 4]
]

for point in special_points:
    print(f"{str(point):10s} -> {classify_point(point)}")

# 示例 4：映射模式（字典匹配）
print("\n[示例 4] 映射模式 - 用户信息处理：\n")

def greet_user(user):
    """根据用户信息生成问候语"""
    match user:
        case {"name": name, "role": "admin"}:
            return f"👑 管理员 {name}，欢迎回来！"
        case {"name": name, "role": "user"}:
            return f"👤 用户 {name}，你好！"
        case {"name": name}:
            return f"👋 {name}，欢迎！"
        case {"id": user_id}:
            return f"🆔 用户 ID: {user_id}"
        case _:
            return "👻 匿名用户"

# 测试不同的用户数据
users = [
    {"name": "Alice", "role": "admin"},
    {"name": "Bob", "role": "user"},
    {"name": "Charlie"},
    {"id": 12345},
    {"email": "test@example.com"}
]

for user in users:
    print(f"{str(user):45s} -> {greet_user(user)}")

# 示例 5：OR 模式（多个模式匹配同一分支）
print("\n[示例 5] OR 模式 - 命令别名：\n")

def execute_command(cmd):
    """执行命令（支持别名）"""
    match cmd.lower():
        case "quit" | "exit" | "q":
            return "🚪 退出程序"
        case "help" | "h" | "?":
            return "❓ 显示帮助"
        case "save" | "s":
            return "💾 保存文件"
        case "load" | "l":
            return "📂 加载文件"
        case _:
            return f"❌ 未知命令: {cmd}"

# 测试命令别名
commands = ["quit", "q", "help", "?", "save", "unknown"]
for cmd in commands:
    print(f"{cmd:10s} -> {execute_command(cmd)}")

# 示例 6：通配符模式（捕获剩余元素）
print("\n[示例 6] 通配符模式 - 列表头尾分离：\n")

def analyze_list(items):
    """分析列表结构"""
    match items:
        case []:
            return "空列表"
        case [single]:
            return f"单元素列表: {single}"
        case [first, second]:
            return f"两元素列表: {first}, {second}"
        case [first, *rest]:
            return f"首元素: {first}, 剩余: {rest} ({len(rest)}个)"

# 测试不同长度的列表
test_lists = [
    [],
    [1],
    [1, 2],
    [1, 2, 3],
    [1, 2, 3, 4, 5]
]

for lst in test_lists:
    print(f"{str(lst):25s} -> {analyze_list(lst)}")

# 示例 7：守卫条件（case 后加 if）
print("\n[示例 7] 守卫条件 - 数值分类：\n")

def classify_number(n):
    """分类数值"""
    match n:
        case x if x > 100:
            return f"{x} 是大数（>100）"
        case x if x > 10:
            return f"{x} 是中数（10-100）"
        case x if x > 0:
            return f"{x} 是小数（0-10）"
        case 0:
            return "零"
        case x if x < 0:
            return f"{x} 是负数"

# 测试不同数值
numbers = [150, 50, 5, 0, -10]
for num in numbers:
    print(f"{num:5d} -> {classify_number(num)}")

# 示例 8：AS 模式（捕获整个匹配值）
print("\n[示例 8] AS 模式 - 捕获和解构：\n")

def process_coordinate(coord):
    """处理坐标，既使用整体又使用部分"""
    match coord:
        case [x, y] as point:
            return f"点 {point} 的坐标是 x={x}, y={y}"
        case [x, y, z] as point:
            return f"3D点 {point} 的坐标是 x={x}, y={y}, z={z}"
        case other:
            return f"无效坐标: {other}"

# 测试坐标
coordinates = [[1, 2], [3, 4, 5], [1]]
for coord in coordinates:
    print(process_coordinate(coord))

print("\n💡 总结：match/case 支持多种模式，比传统 if/elif 更强大和优雅")

