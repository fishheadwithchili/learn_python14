"""
场景 10：测试和 Mock 数据生成

应用：为类型附加示例值，自动生成测试数据
"""

from typing import Annotated, get_type_hints
from dataclasses import dataclass
import random

class Example:
    """示例值"""
    def __init__(self, *examples):
        self.examples = examples
    
    def random(self):
        """随机选择一个示例"""
        return random.choice(self.examples)

# ✅ 定义带示例的类型
@dataclass
class User:
    """用户"""
    name: Annotated[str, Example("Alice", "Bob", "Charlie", "David")]
    age: Annotated[int, Example(25, 30, 35, 40)]
    email: Annotated[str, Example("alice@test.com", "bob@test.com")]
    city: Annotated[str, Example("北京", "上海", "深圳", "杭州")]

def generate_mock_data(model_class, count=5):
    """生成 Mock 数据"""
    hints = get_type_hints(model_class, include_extras=True)
    data_list = []
    
    for _ in range(count):
        mock_obj = {}
        for field_name, field_type in hints.items():
            if hasattr(field_type, '__metadata__'):
                for metadata in field_type.__metadata__:
                    if isinstance(metadata, Example):
                        mock_obj[field_name] = metadata.random()
                        break
        data_list.append(model_class(**mock_obj))
    
    return data_list

print("=" * 60)
print("场景 10：测试数据生成")
print("=" * 60)

print("\n[生成5个 Mock 用户]:\n")
mock_users = generate_mock_data(User, 5)

for i, user in enumerate(mock_users, 1):
    print(f"{i}. {user.name}, {user.age}岁, {user.email}, {user.city}")

print("\n💡 总结：Annotated 附加示例值，自动生成测试数据")

