"""
场景 2：数学/算法函数参数无语义价值

应用：函数参数位置本身就是约定，名称不重要
"""

import math

print("=" * 60)
print("数学函数：位置有明确语义")
print("=" * 60)

# ✅ 使用仅位置参数
def clamp(value, /, min_val, max_val):
    """
    将值限制在范围内
    
    参数:
        value: 要限制的值（仅位置）
        min_val: 最小值
        max_val: 最大值
    """
    return max(min_val, min(value, max_val))

print("\n使用示例：\n")

# 清晰的调用
result1 = clamp(15, 0, 10)
print(f"  clamp(15, 0, 10) = {result1}")

result2 = clamp(-5, min_val=0, max_val=100)
print(f"  clamp(-5, min_val=0, max_val=100) = {result2}")

# value 不能用关键字
try:
    clamp(value=15, min_val=0, max_val=10)
except TypeError:
    print(f"  ✅ 正确阻止: clamp(value=15, ...) - value 必须位置传递")

print("\n" + "=" * 60)
print("更多数学函数示例")
print("=" * 60)

def lerp(a, b, /, t):
    """线性插值：在 a 和 b 之间按 t 比例插值"""
    return a + (b - a) * t

def distance(x1, y1, x2, y2, /):
    """计算两点间距离"""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def mix_colors(r1, g1, b1, r2, g2, b2, /, ratio=0.5):
    """混合两个 RGB 颜色"""
    return (
        int(lerp(r1, r2, ratio)),
        int(lerp(g1, g2, ratio)),
        int(lerp(b1, b2, ratio))
    )

print("\n线性插值：\n")
print(f"  lerp(0, 100, 0.5) = {lerp(0, 100, 0.5)}")
print(f"  lerp(0, 100, 0.25) = {lerp(0, 100, 0.25)}")

print("\n两点距离：\n")
dist = distance(0, 0, 3, 4)
print(f"  distance(0, 0, 3, 4) = {dist}")

print("\n颜色混合：\n")
red = (255, 0, 0)
blue = (0, 0, 255)
purple = mix_colors(*red, *blue, ratio=0.5)
print(f"  红色 {red} + 蓝色 {blue} = 紫色 {purple}")

print("\n" + "=" * 60)
print("与内置函数保持一致")
print("=" * 60)

print("""
Python 内置函数也使用仅位置参数：

  abs(x, /)              # 绝对值
  len(obj, /)            # 长度
  pow(base, exp, /, mod=None)  # 幂运算
  divmod(a, b, /)        # 除法和取模

这些函数的参数位置有明确含义，不需要关键字传递。
""")

print("💡 总结：数学函数参数位置固定，强制用户按正确顺序调用")

