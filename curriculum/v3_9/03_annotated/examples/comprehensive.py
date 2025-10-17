"""
综合示例：数据验证框架

场景：构建一个完整的数据验证框架，支持各种验证规则、
自动验证、错误收集和文档生成。
"""

from typing import Annotated, get_type_hints
from dataclasses import dataclass
from datetime import datetime

# ============= 验证规则类 =============

class ValidationRule:
    """验证规则基类"""
    def validate(self, value) -> tuple[bool, str]:
        raise NotImplementedError

class Range:
    def __init__(self, min_val, max_val):
        self.min, self.max = min_val, max_val
    def validate(self, value):
        if not (self.min <= value <= self.max):
            return False, f"值必须在 {self.min}-{self.max} 之间"
        return True, ""

class MinLength:
    def __init__(self, length):
        self.length = length
    def validate(self, value):
        if len(value) < self.length:
            return False, f"长度至少 {self.length} 个字符"
        return True, ""

class Pattern:
    def __init__(self, pattern, message):
        self.pattern, self.message = pattern, message
    def validate(self, value):
        import re
        if not re.match(self.pattern, value):
            return False, self.message
        return True, ""

# ============= 数据模型 =============

@dataclass
class User:
    username: Annotated[str, MinLength(3), "用户名"]
    email: Annotated[str, Pattern(r'^[\w\.-]+@[\w\.-]+\.\w+$', "邮箱格式无效")]
    age: Annotated[int, Range(0, 150)]
    password: Annotated[str, MinLength(8), "密码至少8位"]

# ============= 验证框架 =============

class Validator:
    def validate(self, obj) -> dict[str, list[str]]:
        hints = get_type_hints(obj.__class__, include_extras=True)
        errors = {}
        
        for field_name, field_type in hints.items():
            value = getattr(obj, field_name)
            field_errors = []
            
            if hasattr(field_type, '__metadata__'):
                for metadata in field_type.__metadata__:
                    if hasattr(metadata, 'validate'):
                        is_valid, error_msg = metadata.validate(value)
                        if not is_valid:
                            field_errors.append(error_msg)
            
            if field_errors:
                errors[field_name] = field_errors
        
        return errors

# ============= 主程序 =============

def main():
    print("=" * 70)
    print("综合示例：数据验证框架")
    print("=" * 70)
    
    validator = Validator()
    
    # 测试1：有效数据
    print("\n[测试 1] 有效数据：")
    valid_user = User("alice", "alice@example.com", 25, "SecurePass123")
    errors = validator.validate(valid_user)
    print(f"结果: {'✅ 通过' if not errors else f'❌ 失败: {errors}'}")
    
    # 测试2：无效数据
    print("\n[测试 2] 无效数据：")
    invalid_user = User("ab", "bad-email", 200, "short")
    errors = validator.validate(invalid_user)
    if errors:
        print("验证错误:")
        for field, msgs in errors.items():
            print(f"  {field}: {msgs}")
    
    print("\n💡 总结：Annotated + 元数据 = 强大的数据验证框架")

if __name__ == "__main__":
    main()

