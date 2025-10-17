"""
场景 8：权限和访问控制

应用：为字段附加权限要求，实现字段级访问控制
"""

from typing import Annotated, get_type_hints
from dataclasses import dataclass

class Requires:
    """权限要求"""
    def __init__(self, *roles):
        self.roles = set(roles)
    
    def check(self, user_roles):
        """检查权限"""
        return bool(self.roles & set(user_roles))

# ✅ 定义带权限的数据模型
@dataclass
class Employee:
    """员工信息"""
    id: int
    name: str
    email: Annotated[str, Requires("self", "hr", "admin")]
    salary: Annotated[float, Requires("hr", "admin")]
    ssn: Annotated[str, Requires("admin")]
    performance_review: Annotated[str, Requires("manager", "admin")]

def filter_fields_by_permission(obj, user_roles):
    """根据权限过滤字段"""
    hints = get_type_hints(obj.__class__, include_extras=True)
    visible_fields = {}
    
    for field_name, field_type in hints.items():
        can_access = True
        
        if hasattr(field_type, '__metadata__'):
            for metadata in field_type.__metadata__:
                if isinstance(metadata, Requires):
                    can_access = metadata.check(user_roles)
                    break
        
        if can_access:
            visible_fields[field_name] = getattr(obj, field_name)
        else:
            visible_fields[field_name] = "[受限]"
    
    return visible_fields

print("=" * 60)
print("场景 8：权限和访问控制")
print("=" * 60)

employee = Employee(
    id=1001,
    name="Alice",
    email="alice@company.com",
    salary=80000.0,
    ssn="123-45-6789",
    performance_review="优秀"
)

# 示例 1：普通员工查看
print("\n[示例 1] 普通员工视图：\n")
employee_view = filter_fields_by_permission(employee, ["employee"])
for field, value in employee_view.items():
    print(f"  {field}: {value}")

# 示例 2：HR 查看
print("\n[示例 2] HR 视图：\n")
hr_view = filter_fields_by_permission(employee, ["hr"])
for field, value in hr_view.items():
    print(f"  {field}: {value}")

# 示例 3：管理员查看
print("\n[示例 3] 管理员视图：\n")
admin_view = filter_fields_by_permission(employee, ["admin"])
for field, value in admin_view.items():
    print(f"  {field}: {value}")

print("\n💡 总结：Annotated 实现字段级权限控制，保护敏感数据")

