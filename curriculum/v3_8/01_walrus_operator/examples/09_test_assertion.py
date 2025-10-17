"""
场景 9：测试断言中的中间值检查

应用：需要同时断言中间值和最终结果，错误消息更详细
"""

def calculate_discount(price: float, discount_rate: float) -> float:
    """计算折扣后价格"""
    if not 0 <= discount_rate <= 1:
        raise ValueError("折扣率必须在 0-1 之间")
    return price * (1 - discount_rate)

def process_order(items: list, tax_rate: float) -> float:
    """处理订单，返回总价"""
    subtotal = sum(item['price'] * item['quantity'] for item in items)
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total

print("=" * 60)
print("测试断言中使用 Walrus Operator")
print("=" * 60)

# ❌ 传统方式 - 错误消息不够详细
print("\n[传统方式] 简单断言：\n")

try:
    price = 100
    discount = 0.2
    result = calculate_discount(price, discount)
    assert result == 80, f"期望 80，得到 {result}"
    print(f"  ✅ 测试通过: 价格 {price}，折扣 {discount} → {result}")
except AssertionError as e:
    print(f"  ❌ 测试失败: {e}")

# ✅ 使用 walrus operator - 错误消息包含实际值
print("\n[Walrus Operator] 详细的错误消息：\n")

try:
    price = 100
    discount = 0.3  # 故意设置错误的值
    expected = 80
    assert (result := calculate_discount(price, discount)) == expected, \
        f"折扣计算错误：期望 {expected}，实际 {result}（价格={price}, 折扣={discount}）"
    print(f"  ✅ 测试通过")
except AssertionError as e:
    print(f"  ❌ 测试失败: {e}")

print("\n" + "=" * 60)
print("复杂测试：多步骤验证")
print("=" * 60)

# 测试订单处理
orders = [
    {'name': '商品A', 'price': 50, 'quantity': 2},
    {'name': '商品B', 'price': 30, 'quantity': 3},
]
tax_rate = 0.1

print("\n测试订单处理流程：\n")

try:
    # 使用 walrus operator 在断言中捕获中间值
    assert (total := process_order(orders, tax_rate)) > 0, \
        f"总价必须大于0，实际: {total}"
    
    expected_total = 209.0  # (50*2 + 30*3) * 1.1
    assert abs(total - expected_total) < 0.01, \
        f"总价计算错误：期望 {expected_total}，实际 {total}"
    
    print(f"  ✅ 订单测试通过")
    print(f"     商品总价: {total/1.1:.2f}")
    print(f"     税费: {total - total/1.1:.2f}")
    print(f"     应付总额: {total:.2f}")
    
except AssertionError as e:
    print(f"  ❌ 测试失败: {e}")

print("\n" + "=" * 60)
print("范围检查")
print("=" * 60)

def analyze_data(values: list) -> dict:
    """分析数据"""
    return {
        'count': len(values),
        'sum': sum(values),
        'avg': sum(values) / len(values) if values else 0
    }

data = [10, 20, 30, 40, 50]

print("\n测试数据分析：\n")

try:
    result = analyze_data(data)
    
    # 检查平均值在合理范围内
    assert 0 < (avg := result['avg']) < 100, \
        f"平均值 {avg} 超出预期范围 (0, 100)"
    
    # 检查总和
    assert (total := result['sum']) == 150, \
        f"总和错误：期望 150，实际 {total}"
    
    print(f"  ✅ 数据分析测试通过")
    print(f"     数据点: {result['count']}")
    print(f"     总和: {total}")
    print(f"     平均值: {avg}")
    
except AssertionError as e:
    print(f"  ❌ 测试失败: {e}")

print("\n" + "=" * 60)
print("pytest 风格的应用")
print("=" * 60)

print("""
在 pytest 中使用 walrus operator:

def test_discount_calculation():
    price = 100
    discount_rate = 0.2
    
    assert (result := calculate_discount(price, discount_rate)) == 80, \\
        f"折扣计算失败: {price} * (1-{discount_rate}) = {result}, 期望 80"
    
    # result 可以在后续断言中使用
    assert result > 0, f"价格必须为正数: {result}"
    assert result < price, f"折扣后价格必须小于原价: {result} >= {price}"

优势：
✅ 错误消息更详细，包含实际计算值
✅ 减少重复计算
✅ 代码更紧凑
""")

print("\n💡 总结：让测试失败消息更有用，快速定位问题")

