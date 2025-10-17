"""
场景 1：数据验证规则

应用：在数据类或API参数中附加验证规则，实现自动数据验证
"""

from typing import Annotated, get_type_hints
from dataclasses import dataclass

# 定义验证规则类
class Range:
    """数值范围验证"""
    def __init__(self, min_val, max_val):
        self.min = min_val
        self.max = max_val
    
    def validate(self, value):
        return self.min <= value <= self.max

class MinLength:
    """最小长度验证"""
    def __init__(self, length):
        self.length = length
    
    def validate(self, value):
        return len(value) >= self.length

class Pattern:
    """正则表达式验证"""
    def __init__(self, pattern):
        self.pattern = pattern
    
    def validate(self, value):
        import re
        return bool(re.match(self.pattern, value))

# ✅ 使用 Annotated 附加验证规则

@dataclass
class User:
    name: Annotated[str, MinLength(3), "用户名至少3个字符"]
    age: Annotated[int, Range(0, 150), "年龄必须在0-150之间"]
    email: Annotated[str, Pattern(r'^[\w\.-]+@[\w\.-]+\.\w+$'), "有效的邮箱格式"]
    score: Annotated[float, Range(0.0, 100.0), "分数0-100"]

def validate_field(value, field_type):
    """验证单个字段"""
    errors = []
    
    # 获取元数据
    if hasattr(field_type, '__metadata__'):
        for metadata in field_type.__metadata__:
            if isinstance(metadata, (Range, MinLength, Pattern)):
                if not metadata.validate(value):
                    errors.append(f"验证失败: {metadata}")
    
    return errors

def validate_dataclass(obj):
    """验证整个数据类"""
    hints = get_type_hints(obj.__class__, include_extras=True)
    all_errors = {}
    
    for field_name, field_type in hints.items():
        value = getattr(obj, field_name)
        errors = validate_field(value, field_type)
        if errors:
            all_errors[field_name] = errors
    
    return all_errors

print("=" * 60)
print("场景 1：数据验证规则")
print("=" * 60)

# 示例 1：有效数据
print("\n[示例 1] 有效数据：\n")

valid_user = User(
    name="Alice",
    age=30,
    email="alice@example.com",
    score=95.5
)

print(f"用户数据: {valid_user}")

errors = validate_dataclass(valid_user)
if errors:
    print(f"❌ 验证失败: {errors}")
else:
    print("✅ 验证通过")

# 示例 2：无效的用户名（太短）
print("\n[示例 2] 无效的用户名（太短）：\n")

try:
    invalid_user1 = User(
        name="Al",  # 只有2个字符
        age=25,
        email="al@example.com",
        score=80.0
    )
    
    errors = validate_dataclass(invalid_user1)
    print(f"用户数据: name='{invalid_user1.name}'")
    if errors:
        print(f"❌ 验证失败:")
        for field, field_errors in errors.items():
            print(f"  {field}: 长度不足（最少3个字符）")
except Exception as e:
    print(f"错误: {e}")

# 示例 3：无效的年龄（超出范围）
print("\n[示例 3] 无效的年龄（超出范围）：\n")

invalid_user2 = User(
    name="Bob",
    age=200,  # 超出范围
    email="bob@example.com",
    score=75.0
)

errors = validate_dataclass(invalid_user2)
print(f"用户数据: age={invalid_user2.age}")
if errors:
    print(f"❌ 验证失败:")
    for field, field_errors in errors.items():
        print(f"  {field}: 年龄超出范围（0-150）")

# 示例 4：无效的邮箱格式
print("\n[示例 4] 无效的邮箱格式：\n")

invalid_user3 = User(
    name="Charlie",
    age=28,
    email="invalid-email",  # 格式错误
    score=88.0
)

errors = validate_dataclass(invalid_user3)
print(f"用户数据: email='{invalid_user3.email}'")
if errors:
    print(f"❌ 验证失败:")
    for field, field_errors in errors.items():
        print(f"  {field}: 邮箱格式无效")

# 示例 5：多个字段无效
print("\n[示例 5] 多个字段同时无效：\n")

invalid_user4 = User(
    name="Ed",  # 太短
    age=-5,  # 负数
    email="bad-email",  # 格式错误
    score=105.0  # 超出范围
)

errors = validate_dataclass(invalid_user4)
print(f"用户数据: {invalid_user4}")
if errors:
    print(f"❌ 验证失败 ({len(errors)} 个字段):")
    for field in errors.keys():
        print(f"  - {field}")

print("\n💡 总结：Annotated 让验证规则与类型定义结合，便于自动验证")

