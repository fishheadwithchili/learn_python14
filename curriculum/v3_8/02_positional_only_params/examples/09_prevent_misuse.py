"""
场景 9: 防止误用的安全设计

应用：某些参数如果用关键字传递可能导致逻辑错误
"""

from typing import Optional

print("=" * 60)
print("防止参数顺序混淆")
print("=" * 60)

def transfer(from_account, to_account, /, amount, memo=None):
    """
    转账（仅位置参数避免顺序混淆）
    
    参数:
        from_account: 源账户（仅位置）
        to_account: 目标账户（仅位置）
        amount: 金额
        memo: 备注
    """
    print(f"  转账:")
    print(f"    从: {from_account}")
    print(f"    到: {to_account}")
    print(f"    金额: ${amount}")
    if memo:
        print(f"    备注: {memo}")

print("\n正确使用：\n")

transfer("Alice", "Bob", amount=100, memo="Dinner")

print("\n防止误用：\n")

# ❌ 如果允许关键字，可能写错顺序
try:
    # 这会被阻止（好事！）
    transfer(to_account="Alice", from_account="Bob", amount=100)
except TypeError:
    print("  ✅ 阻止了可能的参数顺序错误")

print("\n" + "=" * 60)
print("子字符串操作")
print("=" * 60)

def substring(text, start, end, /):
    """
    提取子字符串
    
    参数:
        text: 源字符串（仅位置）
        start: 起始索引（仅位置）
        end: 结束索引（仅位置）
    
    仅位置避免混淆 start 和 end
    """
    return text[start:end]

print("\n提取子字符串：\n")

text = "Hello, World!"
result = substring(text, 0, 5)
print(f"  substring('{text}', 0, 5) = '{result}'")

result = substring(text, 7, 12)
print(f"  substring('{text}', 7, 12) = '{result}'")

print("\n防止混淆：\n")
try:
    # 如果允许关键字，可能写成：
    # substring(text, end=5, start=0)  # 顺序反了！
    substring(text, end=5, start=0)
except TypeError:
    print("  ✅ 阻止了 start 和 end 的顺序混淆")

print("\n" + "=" * 60)
print("范围检查")
print("=" * 60)

def in_range(value, min_val, max_val, /, inclusive=True):
    """
    检查值是否在范围内
    
    参数:
        value: 要检查的值（仅位置）
        min_val: 最小值（仅位置）
        max_val: 最大值（仅位置）
        inclusive: 是否包含边界
    """
    if inclusive:
        result = min_val <= value <= max_val
    else:
        result = min_val < value < max_val
    
    op = "<=" if inclusive else "<"
    print(f"  {min_val} {op} {value} {op} {max_val}: {result}")
    return result

print("\n范围检查：\n")

in_range(5, 0, 10)
in_range(10, 0, 10, inclusive=False)
in_range(15, 0, 10)

print("\n💡 总结：仅位置参数强制正确的参数顺序，减少逻辑错误")

