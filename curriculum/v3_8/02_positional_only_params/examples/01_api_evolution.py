"""
场景 1：保护公共 API 的参数名称重构

应用：库的公共接口需要重命名参数但不想破坏用户代码
"""

# 模拟一个库的演化过程

print("=" * 60)
print("公共 API 参数重命名的兼容性问题")
print("=" * 60)

# ❌ v1.0 - 没有使用仅位置参数
print("\n[库 v1.0] 没有保护参数名：\n")

def connect_v1(h, p, timeout=30):
    """建立连接（v1.0）"""
    return f"连接到 {h}:{p} (超时: {timeout}s)"

# 用户可能这样使用
result1 = connect_v1("localhost", 8080)
result2 = connect_v1(h="db.example.com", p=5432, timeout=60)

print(f"  位置调用: {result1}")
print(f"  关键字调用: {result2}")

# 问题：如果在 v2.0 想改进参数名...
print("\n[库 v2.0] 想改进参数名（会破坏兼容性）：\n")

def connect_v2_broken(host, port, timeout=30):
    """改进的参数名，但破坏了兼容性！"""
    return f"连接到 {host}:{port} (超时: {timeout}s)"

# 旧的关键字调用会失败
try:
    result = connect_v2_broken(h="localhost", p=8080)
except TypeError as e:
    print(f"  ❌ 旧代码失败: {e}")

# ✅ 正确做法：v1.0 就使用仅位置参数
print("\n" + "=" * 60)
print("[正确做法] v1.0 使用仅位置参数：")
print("=" * 60)

def connect_v1_correct(h, p, /, timeout=30):
    """连接（保护参数名）"""
    return f"连接到 {h}:{p} (超时: {timeout}s)"

print("\n用户只能这样调用：\n")
result1 = connect_v1_correct("localhost", 8080)
result2 = connect_v1_correct("localhost", 8080, timeout=60)
print(f"  ✅ 位置调用: {result1}")
print(f"  ✅ 混合调用: {result2}")

# 不能用关键字传递 h 和 p
try:
    connect_v1_correct(h="localhost", p=8080)
except TypeError:
    print(f"  ✅ 正确阻止了关键字调用（这是好事！）")

# v2.0 可以安全地重命名
print("\n[库 v2.0] 安全的参数重命名：\n")

def connect_v2_correct(host, port, /, timeout=30):
    """改进的参数名，不破坏兼容性"""
    return f"连接到 {host}:{port} (超时: {timeout}s)"

# 旧代码依然正常工作
result = connect_v2_correct("localhost", 8080)
print(f"  ✅ 旧代码正常: {result}")

result = connect_v2_correct("localhost", 8080, timeout=60)
print(f"  ✅ 新代码正常: {result}")

print("\n💡 总结：仅位置参数让 API 演化更自由，不破坏用户代码")

