"""
场景 6：数据验证

应用：验证用户输入、表单数据、API 请求体等
运行要求：Python >= 3.10
"""

print("=" * 60)
print("场景 6：数据验证")
print("=" * 60)

# 示例 1：用户注册数据验证
print("\n[示例 1] 用户注册数据验证：\n")

def validate_user_registration(data):
    """验证用户注册数据"""
    match data:
        case {
            "username": str(u),
            "email": str(e),
            "password": str(p),
            "age": int(age)
        } if (
            len(u) >= 3 and
            "@" in e and
            len(p) >= 8 and
            age >= 18
        ):
            return {
                "valid": True,
                "message": f"✅ 用户 {u} 注册数据有效"
            }
        case {"username": str(u)} if len(u) < 3:
            return {
                "valid": False,
                "message": "❌ 用户名至少 3 个字符"
            }
        case {"email": str(e)} if "@" not in e:
            return {
                "valid": False,
                "message": "❌ 无效的邮箱地址"
            }
        case {"password": str(p)} if len(p) < 8:
            return {
                "valid": False,
                "message": "❌ 密码至少 8 个字符"
            }
        case {"age": int(age)} if age < 18:
            return {
                "valid": False,
                "message": "❌ 年龄必须大于等于 18"
            }
        case {"username": _, "email": _, "password": _, "age": _}:
            return {
                "valid": False,
                "message": "❌ 数据类型错误"
            }
        case _:
            return {
                "valid": False,
                "message": "❌ 缺少必填字段"
            }

# 测试注册数据
registration_data = [
    {"username": "alice", "email": "alice@example.com", "password": "secure123", "age": 25},
    {"username": "ab", "email": "bob@example.com", "password": "12345678", "age": 30},
    {"username": "charlie", "email": "invalid-email", "password": "password", "age": 22},
    {"username": "david", "email": "david@example.com", "password": "short", "age": 28},
    {"username": "eve", "email": "eve@example.com", "password": "longpassword", "age": 16},
    {"username": "frank", "email": "frank@example.com"}
]

for i, data in enumerate(registration_data, 1):
    result = validate_user_registration(data)
    print(f"{i}. {result['message']}")

# 示例 2：支付信息验证
print("\n[示例 2] 支付信息验证：\n")

def validate_payment_info(payment):
    """验证支付信息"""
    match payment:
        case {"method": "credit_card", "card_number": str(num), "cvv": str(cvv), "expiry": str(exp)} \
                if len(num) == 16 and num.isdigit() and len(cvv) == 3:
            return f"✅ 信用卡信息有效（末尾 {num[-4:]}）"
        case {"method": "paypal", "email": str(email)} if "@" in email:
            return f"✅ PayPal 账户: {email}"
        case {"method": "bank_transfer", "account": str(acc), "routing": str(rout)}:
            return f"✅ 银行转账信息有效"
        case {"method": "crypto", "currency": str(curr), "wallet": str(wallet)}:
            return f"✅ 加密货币支付: {curr}"
        case {"method": method}:
            return f"❌ 不支持的支付方式: {method}"
        case _:
            return "❌ 无效的支付信息"

# 测试支付信息
payments = [
    {
        "method": "credit_card",
        "card_number": "4532123456789012",
        "cvv": "123",
        "expiry": "12/25"
    },
    {
        "method": "paypal",
        "email": "user@paypal.com"
    },
    {
        "method": "bank_transfer",
        "account": "123456789",
        "routing": "987654321"
    },
    {
        "method": "crypto",
        "currency": "BTC",
        "wallet": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
    },
    {
        "method": "cash"
    }
]

for payment in payments:
    print(validate_payment_info(payment))

# 示例 3：产品数据验证
print("\n[示例 3] 产品数据验证：\n")

def validate_product(product):
    """验证产品数据"""
    match product:
        case {
            "name": str(name),
            "price": int(price) | float(price),
            "stock": int(stock),
            "category": str(cat)
        } if price > 0 and stock >= 0:
            status = "有货" if stock > 0 else "缺货"
            return f"✅ 产品 '{name}' 有效（${price:.2f}，{status}）"
        case {"price": price} if price <= 0:
            return "❌ 价格必须大于 0"
        case {"stock": stock} if stock < 0:
            return "❌ 库存不能为负数"
        case _:
            return "❌ 产品数据不完整"

# 测试产品数据
products = [
    {"name": "Laptop", "price": 999.99, "stock": 10, "category": "Electronics"},
    {"name": "Book", "price": 19, "stock": 0, "category": "Books"},
    {"name": "Invalid", "price": -10, "stock": 5, "category": "Other"},
    {"name": "Incomplete", "price": 50}
]

for product in products:
    print(validate_product(product))

# 示例 4：地址数据验证
print("\n[示例 4] 地址数据验证：\n")

def validate_address(address):
    """验证地址数据"""
    match address:
        case {
            "street": str(s),
            "city": str(c),
            "state": str(st),
            "zip": str(z),
            "country": "USA"
        } if len(z) == 5 and z.isdigit():
            return f"✅ 美国地址: {s}, {c}, {st} {z}"
        case {
            "street": str(s),
            "city": str(c),
            "postal_code": str(pc),
            "country": "UK"
        }:
            return f"✅ 英国地址: {s}, {c}, {pc}"
        case {
            "street": str(s),
            "city": str(c),
            "province": str(prov),
            "postal_code": str(pc),
            "country": "Canada"
        }:
            return f"✅ 加拿大地址: {s}, {c}, {prov} {pc}"
        case {"country": country}:
            return f"⚠️  国家 {country} 需要特定格式"
        case _:
            return "❌ 无效的地址格式"

# 测试地址数据
addresses = [
    {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY",
        "zip": "10001",
        "country": "USA"
    },
    {
        "street": "10 Downing St",
        "city": "London",
        "postal_code": "SW1A 2AA",
        "country": "UK"
    },
    {
        "street": "100 Queen St",
        "city": "Toronto",
        "province": "ON",
        "postal_code": "M5H 2N2",
        "country": "Canada"
    },
    {
        "country": "France"
    }
]

for addr in addresses:
    print(validate_address(addr))

# 示例 5：API 请求参数验证
print("\n[示例 5] API 请求参数验证：\n")

def validate_api_request(params):
    """验证 API 请求参数"""
    match params:
        case {"action": "list", "page": int(p), "limit": int(l)} if p > 0 and 0 < l <= 100:
            return f"✅ 列表请求: 第 {p} 页，每页 {l} 条"
        case {"action": "get", "id": int(id)} if id > 0:
            return f"✅ 获取资源 ID: {id}"
        case {"action": "create", "data": dict(data)} if data:
            return f"✅ 创建请求: {len(data)} 个字段"
        case {"action": "update", "id": int(id), "data": dict(data)} if id > 0 and data:
            return f"✅ 更新资源 {id}: {len(data)} 个字段"
        case {"action": "delete", "id": int(id)} if id > 0:
            return f"⚠️  删除资源 ID: {id}"
        case {"action": "search", "query": str(q)} if len(q) >= 2:
            return f"✅ 搜索: '{q}'"
        case {"action": action}:
            return f"❌ 操作 '{action}' 的参数无效"
        case _:
            return "❌ 无效的 API 请求"

# 测试 API 请求
api_requests = [
    {"action": "list", "page": 1, "limit": 20},
    {"action": "get", "id": 123},
    {"action": "create", "data": {"name": "New Item", "price": 99}},
    {"action": "update", "id": 456, "data": {"price": 109}},
    {"action": "delete", "id": 789},
    {"action": "search", "query": "Python"},
    {"action": "list", "page": 0, "limit": 200}
]

for req in api_requests:
    print(validate_api_request(req))

# 示例 6：表单字段验证（带自定义规则）
print("\n[示例 6] 表单字段验证（复杂规则）：\n")

def validate_form_field(field_name, value, rules):
    """验证单个表单字段"""
    match (field_name, value, rules):
        case ("email", str(v), {"required": True}) if "@" in v and "." in v:
            return f"✅ 邮箱有效: {v}"
        case ("email", "", {"required": True}):
            return "❌ 邮箱为必填项"
        case ("email", str(v), _):
            return "❌ 邮箱格式无效"
        
        case ("phone", str(v), {"pattern": pattern}) if len(v) == 10 and v.isdigit():
            return f"✅ 电话号码有效: {v}"
        case ("phone", str(v), _):
            return f"❌ 电话号码格式错误: {v}"
        
        case ("age", int(v), {"min": min_val, "max": max_val}) if min_val <= v <= max_val:
            return f"✅ 年龄有效: {v}"
        case ("age", int(v), {"min": min_val}) if v < min_val:
            return f"❌ 年龄不能小于 {min_val}"
        case ("age", int(v), {"max": max_val}) if v > max_val:
            return f"❌ 年龄不能大于 {max_val}"
        
        case (name, str(v), {"minLength": min_len}) if len(v) >= min_len:
            return f"✅ {name} 长度有效"
        case (name, str(v), {"minLength": min_len}):
            return f"❌ {name} 长度至少 {min_len} 个字符"
        
        case _:
            return f"⚠️  未定义的验证规则: {field_name}"

# 测试表单字段验证
field_tests = [
    ("email", "user@example.com", {"required": True}),
    ("email", "", {"required": True}),
    ("email", "invalid-email", {"required": True}),
    ("phone", "1234567890", {"pattern": "^\\d{10}$"}),
    ("phone", "123", {"pattern": "^\\d{10}$"}),
    ("age", 25, {"min": 18, "max": 100}),
    ("age", 15, {"min": 18, "max": 100}),
    ("username", "john_doe", {"minLength": 3}),
    ("username", "ab", {"minLength": 3})
]

for field_name, value, rules in field_tests:
    result = validate_form_field(field_name, value, rules)
    print(f"{field_name:10s} = {str(value):20s} -> {result}")

print("\n💡 总结：match/case 结合守卫条件，是数据验证的强大工具")

