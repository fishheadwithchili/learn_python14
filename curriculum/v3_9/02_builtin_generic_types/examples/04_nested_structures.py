"""
场景 4：嵌套数据结构

应用：表示复杂的嵌套数据结构，如 JSON、树结构、图结构等
"""

# ✅ Python 3.9+ 方式：使用内置泛型表示嵌套结构

# 类型别名
JsonValue = str | int | float | bool | None | list['JsonValue'] | dict[str, 'JsonValue']
JsonDict = dict[str, JsonValue]

def parse_api_response(data: JsonDict) -> dict[str, list[dict[str, str]]]:
    """解析 API 响应（嵌套结构）"""
    result: dict[str, list[dict[str, str]]] = {}
    
    # 假设 API 返回格式：{"users": [{"name": "...", "email": "..."}]}
    if "users" in data and isinstance(data["users"], list):
        result["users"] = [
            {
                "name": str(user.get("name", "")),
                "email": str(user.get("email", ""))
            }
            for user in data["users"]
            if isinstance(user, dict)
        ]
    
    return result


# 树结构类型
TreeNode = dict[str, str | list['TreeNode']]

def print_tree(node: TreeNode, indent: int = 0) -> None:
    """打印树结构"""
    name = node.get("name", "unknown")
    print("  " * indent + f"- {name}")
    
    children = node.get("children")
    if isinstance(children, list):
        for child in children:
            if isinstance(child, dict):
                print_tree(child, indent + 1)


# 图结构类型（邻接表）
Graph = dict[str, list[tuple[str, int]]]  # 节点 -> [(邻居, 权重)]

def find_neighbors(graph: Graph, node: str) -> list[str]:
    """查找邻居节点"""
    return [neighbor for neighbor, _ in graph.get(node, [])]


# 多层嵌套配置
Config = dict[str, dict[str, list[dict[str, str | int]]]]

def validate_config(config: Config) -> list[str]:
    """验证配置结构"""
    errors: list[str] = []
    
    for section, settings in config.items():
        if not isinstance(settings, dict):
            errors.append(f"Section '{section}' must be a dict")
            continue
        
        for key, value in settings.items():
            if not isinstance(value, list):
                errors.append(f"Setting '{section}.{key}' must be a list")
    
    return errors


print("=" * 60)
print("场景 4：嵌套数据结构")
print("=" * 60)

# 示例 1：JSON 数据
print("\n[示例 1] 解析 JSON 响应：\n")

api_response: JsonDict = {
    "users": [
        {"name": "Alice", "email": "alice@example.com", "age": 30},
        {"name": "Bob", "email": "bob@example.com", "age": 25}
    ],
    "metadata": {
        "total": 2,
        "page": 1
    }
}

print(f"原始响应: {api_response}")
parsed = parse_api_response(api_response)
print(f"解析结果: {parsed}")

# 示例 2：树结构
print("\n[示例 2] 树结构：\n")

file_tree: TreeNode = {
    "name": "root",
    "children": [
        {
            "name": "src",
            "children": [
                {"name": "main.py"},
                {"name": "utils.py"}
            ]
        },
        {
            "name": "tests",
            "children": [
                {"name": "test_main.py"}
            ]
        },
        {"name": "README.md"}
    ]
}

print("文件树结构:")
print_tree(file_tree)

# 示例 3：图结构（邻接表）
print("\n[示例 3] 图结构（加权图）：\n")

city_graph: Graph = {
    "北京": [("上海", 1200), ("广州", 2000)],
    "上海": [("北京", 1200), ("深圳", 1500)],
    "广州": [("北京", 2000), ("深圳", 140)],
    "深圳": [("上海", 1500), ("广州", 140)]
}

print("城市交通图:")
for city, connections in city_graph.items():
    print(f"  {city} 连接到: {[f'{n}({w}km)' for n, w in connections]}")

beijing_neighbors = find_neighbors(city_graph, "北京")
print(f"\n北京的邻居城市: {beijing_neighbors}")

# 示例 4：多层嵌套配置
print("\n[示例 4] 多层嵌套配置：\n")

app_config: Config = {
    "database": {
        "connections": [
            {"host": "localhost", "port": 5432},
            {"host": "backup.local", "port": 5432}
        ]
    },
    "cache": {
        "servers": [
            {"host": "redis1", "port": 6379},
            {"host": "redis2", "port": 6379}
        ]
    }
}

print("应用配置:")
for section, settings in app_config.items():
    print(f"  {section}:")
    for key, items in settings.items():
        print(f"    {key}: {len(items)} 项")

errors = validate_config(app_config)
print(f"\n配置验证: {'✅ 通过' if not errors else f'❌ 错误: {errors}'}")

# 示例 5：复杂嵌套查询
print("\n[示例 5] 复杂嵌套数据查询：\n")

# 电商订单数据结构
Order = dict[str, str | int | list[dict[str, str | int | float]]]

orders: list[Order] = [
    {
        "order_id": "ORD001",
        "customer_id": 123,
        "items": [
            {"product": "laptop", "quantity": 1, "price": 999.99},
            {"product": "mouse", "quantity": 2, "price": 29.99}
        ]
    },
    {
        "order_id": "ORD002",
        "customer_id": 456,
        "items": [
            {"product": "keyboard", "quantity": 1, "price": 79.99}
        ]
    }
]

# 计算总金额
for order in orders:
    order_id = order["order_id"]
    items = order["items"]
    
    if isinstance(items, list):
        total = sum(
            float(item.get("quantity", 0)) * float(item.get("price", 0))
            for item in items
            if isinstance(item, dict)
        )
        print(f"订单 {order_id}: {total:.2f} 元")

print("\n[类型注解的优势]")
print("  ✅ 清晰表达复杂数据结构")
print("  ✅ IDE 提供准确的类型提示")
print("  ✅ 静态分析发现结构错误")
print("  ✅ 便于文档生成")

print("\n💡 总结：内置泛型支持任意深度的嵌套类型注解")

