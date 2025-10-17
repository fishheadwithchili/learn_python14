"""
场景 4：API 文档生成

应用：使用 Annotated 为 API 参数添加描述，自动生成 API 文档
"""

from typing import Annotated, get_type_hints
from dataclasses import dataclass

# 定义文档元数据类
class APIParam:
    """API 参数文档"""
    def __init__(self, description, example=None, required=True):
        self.description = description
        self.example = example
        self.required = required

# ✅ 使用 Annotated 定义 API 参数

@dataclass
class CreateUserRequest:
    """创建用户请求"""
    username: Annotated[str, APIParam("用户名，3-50个字符", example="alice")]
    email: Annotated[str, APIParam("邮箱地址", example="alice@example.com")]
    password: Annotated[str, APIParam("密码，至少8位", example="SecurePass123")]
    age: Annotated[int, APIParam("年龄，0-150", example=25, required=False)]

@dataclass
class SearchRequest:
    """搜索请求"""
    query: Annotated[str, APIParam("搜索关键词", example="Python")]
    page: Annotated[int, APIParam("页码，从1开始", example=1)]
    page_size: Annotated[int, APIParam("每页记录数，最大100", example=20)]
    sort_by: Annotated[str, APIParam("排序字段", example="created_at", required=False)]

def generate_api_doc(request_class) -> dict:
    """生成 API 文档"""
    hints = get_type_hints(request_class, include_extras=True)
    
    params = {}
    for field_name, field_type in hints.items():
        param_info = {"type": str(field_type.__origin__ if hasattr(field_type, '__origin__') else field_type.__name__)}
        
        if hasattr(field_type, '__metadata__'):
            for metadata in field_type.__metadata__:
                if isinstance(metadata, APIParam):
                    param_info.update({
                        "description": metadata.description,
                        "required": metadata.required,
                        "example": metadata.example
                    })
        
        params[field_name] = param_info
    
    return {
        "endpoint": f"/api/{request_class.__name__.lower()}",
        "parameters": params
    }

print("=" * 60)
print("场景 4：API 文档生成")
print("=" * 60)

# 示例 1：创建用户 API 文档
print("\n[示例 1] 创建用户 API 文档：\n")

create_user_doc = generate_api_doc(CreateUserRequest)
print(f"接口: {create_user_doc['endpoint']}")
print("\n参数:")
for param_name, param_info in create_user_doc['parameters'].items():
    required_tag = "必填" if param_info.get('required', True) else "选填"
    print(f"  {param_name} ({param_info['type']}) - {required_tag}")
    print(f"    说明: {param_info.get('description')}")
    print(f"    示例: {param_info.get('example')}")

# 示例 2：搜索 API 文档
print("\n[示例 2] 搜索 API 文档：\n")

search_doc = generate_api_doc(SearchRequest)
print(f"接口: {search_doc['endpoint']}")
print("\n参数:")
for param_name, param_info in search_doc['parameters'].items():
    required_tag = "必填" if param_info.get('required', True) else "选填"
    print(f"  {param_name} - {required_tag}")
    print(f"    {param_info.get('description')}")
    if param_info.get('example'):
        print(f"    示例值: {param_info.get('example')}")

print("\n💡 总结：Annotated 让 API 文档自动生成，保持代码和文档同步")

