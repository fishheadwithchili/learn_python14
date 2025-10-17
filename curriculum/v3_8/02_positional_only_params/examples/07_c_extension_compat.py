"""
场景 7: C 扩展的 Python 接口对齐

应用：为 C 扩展编写 Python wrapper 时保持一致的调用方式
"""

print("=" * 60)
print("模拟 C 扩展接口")
print("=" * 60)

# 模拟 C 扩展函数（实际是 C 实现，这里用 Python 模拟）
def _c_add(a, b, /):
    """C 实现的加法（仅支持位置参数）"""
    return a + b

def _c_multiply(a, b, /):
    """C 实现的乘法（仅支持位置参数）"""
    return a * b

# Python wrapper 保持一致
def add(a, b, /):
    """Python wrapper for C add function"""
    return _c_add(a, b)

def multiply(a, b, /):
    """Python wrapper for C multiply function"""
    return _c_multiply(a, b)

print("\n使用 C 扩展接口：\n")

result1 = add(10, 20)
print(f"  add(10, 20) = {result1}")

result2 = multiply(5, 6)
print(f"  multiply(5, 6) = {result2}")

# 不能用关键字（与 C 行为一致）
try:
    add(a=10, b=20)
except TypeError:
    print(f"  ✅ 正确阻止关键字参数（与 C 扩展行为一致）")

print("\n" + "=" * 60)
print("内置函数的签名")
print("=" * 60)

print("""
Python 内置函数（C 实现）的签名：

  abs(x, /)
  len(obj, /)
  pow(base, exp, /, mod=None)
  divmod(a, b, /)
  max(arg1, arg2, *args, /, key=None)
  min(arg1, arg2, *args, /, key=None)

这些都是 C 实现的函数，使用仅位置参数。
""")

import inspect

print("检查内置函数签名：\n")
for func in [abs, len, pow, divmod]:
    try:
        sig = inspect.signature(func)
        print(f"  {func.__name__}{sig}")
    except ValueError:
        print(f"  {func.__name__}(..., /) - C 实现，无法获取完整签名")

print("\n💡 总结：Python wrapper 使用仅位置参数，与 C 扩展行为保持一致")

