"""
场景 7：数学计算验证

应用：科学计算或算法实现时验证中间步骤
"""

import math

print("=" * 60)
print("数学计算验证")
print("=" * 60)

def solve_quadratic(a, b, c):
    """解一元二次方程"""
    print(f"\n解方程: {a}x² + {b}x + {c} = 0\n")
    
    # 判别式
    discriminant = b**2 - 4*a*c
    print(f"{discriminant=}")
    
    if discriminant < 0:
        print("  无实数解")
        return None
    
    # 求解
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    
    print(f"{x1=:.3f}")
    print(f"{x2=:.3f}")
    
    # 验证
    check1 = a*x1**2 + b*x1 + c
    check2 = a*x2**2 + b*x2 + c
    print(f"\n验证: {check1=:.6f}, {check2=:.6f}")
    
    return x1, x2

solve_quadratic(1, -3, 2)
solve_quadratic(1, 0, -4)

print("\n💡 总结：数学公式与输出对应清晰")

