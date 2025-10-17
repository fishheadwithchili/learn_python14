# 内置泛型类型（Builtin Generic Types）

## 一句话总结

直接使用 `list[int]`、`dict[str, int]` 等内置类型作为泛型，无需从 `typing` 模块导入 `List`、`Dict` 等类型。

## 功能详解

### 是什么？

Python 3.9 引入的内置泛型类型（PEP 585）允许直接使用标准容器类型作为泛型，而不再需要从 `typing` 模块导入对应的大写类型。

**语法对比**:
```python
# Python 3.8 及以前 - 需要从 typing 导入
from typing import List, Dict, Set, Tuple

def process(items: List[int]) -> Dict[str, int]:
    ...

# Python 3.9+ - 直接使用内置类型
def process(items: list[int]) -> dict[str, int]:
    ...
```

### 解决什么问题？

**问题 1: 导入繁琐**
```python
# 旧代码 - 需要导入多个类型
from typing import List, Dict, Set, Tuple, Optional
```

**问题 2: 类型名称不一致**
```python
# 运行时用 list，类型注解用 List，容易混淆
items = list()  # 运行时
items: List[int] = []  # 类型注解
```

**问题 3: 记忆负担**
```python
# 需要记住哪些类型在 typing 模块中
from typing import List, Dict, Set, Tuple, Deque, DefaultDict
# list, dict, set, tuple, deque, defaultdict
```

### 语法要点

1. **支持的内置泛型类型**
   ```python
   # 容器类型
   list[int]
   dict[str, int]
   set[str]
   frozenset[int]
   tuple[int, str, float]  # 固定长度
   tuple[int, ...]  # 可变长度
   
   # collections 模块
   from collections import deque, defaultdict
   deque[int]
   defaultdict[str, list[int]]
   ```

2. **嵌套泛型**
   ```python
   # 嵌套使用
   list[list[int]]
   dict[str, list[tuple[int, str]]]
   ```

3. **类型别名**
   ```python
   # 创建类型别名
   Vector = list[float]
   Matrix = list[list[float]]
   
   def scale(v: Vector, factor: float) -> Vector:
       return [x * factor for x in v]
   ```

4. **与 typing 模块的兼容性**
   ```python
   # 可以混用（但不推荐）
   from typing import Optional
   
   def process(data: list[int]) -> Optional[dict[str, int]]:
       ...
   ```

5. **运行时可用**
   ```python
   # 可以在运行时使用（仅限 Python 3.9+）
   T = list[int]
   isinstance([1, 2, 3], list)  # True
   # 注意：不能用于 isinstance 的类型检查
   # isinstance([1, 2, 3], list[int])  # TypeError
   ```

## 核心应用场景

### 1. **函数签名类型注解**
为函数参数和返回值添加类型提示，提升代码可读性和 IDE 支持：
```python
def filter_evens(numbers: list[int]) -> list[int]:
    return [n for n in numbers if n % 2 == 0]
```
**收益**: 无需导入 typing.List，代码更简洁

### 2. **类属性类型注解**
在类定义中声明属性类型：
```python
class UserManager:
    users: dict[int, str]
    active_sessions: set[str]
```
**收益**: 类型注解与运行时类型名称一致，减少认知负担

### 3. **数据类（dataclass）字段定义**
配合 `@dataclass` 定义结构化数据：
```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    grades: list[float]
    metadata: dict[str, str]
```
**收益**: 类型注解简洁，自动生成 `__init__` 等方法

### 4. **嵌套数据结构**
表示复杂的嵌套数据结构：
```python
# JSON 类型
JsonDict = dict[str, int | str | list | dict]

# 树结构
Tree = dict[str, list['Tree']]  # 递归类型（需要引号）
```
**收益**: 准确表达数据结构，便于静态分析

### 5. **泛型函数**
编写支持多种类型的通用函数：
```python
def first_or_none(items: list[T]) -> T | None:
    return items[0] if items else None
```
**收益**: 类型推断更准确

### 6. **配置和设置对象**
定义应用程序配置的类型：
```python
class AppConfig:
    database: dict[str, str]
    allowed_hosts: list[str]
    feature_flags: dict[str, bool]
```
**收益**: 配置类型清晰，便于验证

### 7. **缓存和查找表**
定义缓存数据结构的类型：
```python
class Cache:
    _data: dict[str, tuple[float, str]]  # (timestamp, value)
    _index: dict[str, list[str]]
```
**收益**: 明确缓存数据格式

### 8. **API 响应类型**
定义 API 返回的数据结构：
```python
def fetch_users() -> list[dict[str, str | int]]:
    return [
        {"id": 1, "name": "Alice", "age": 30},
        {"id": 2, "name": "Bob", "age": 25}
    ]
```
**收益**: API 契约清晰，便于文档生成

### 9. **算法和数据结构**
实现算法时指定数据类型：
```python
def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    result: list[int] = []
    # ... 实现
    return result
```
**收益**: 静态类型检查，减少运行时错误

### 10. **测试和 Mock 数据**
定义测试数据的类型：
```python
TEST_DATA: list[dict[str, int | str]] = [
    {"id": 1, "name": "test1"},
    {"id": 2, "name": "test2"}
]
```
**收益**: 测试数据类型明确，便于验证

## 示例代码说明

本目录的 `examples/` 包含 **10 个独立场景示例** 和 **1 个综合示例**：

- `01_function_signature.py` - 函数签名类型注解
- `02_class_attributes.py` - 类属性类型注解
- `03_dataclass_fields.py` - 数据类字段定义
- `04_nested_structures.py` - 嵌套数据结构
- `05_generic_functions.py` - 泛型函数
- `06_config_objects.py` - 配置对象
- `07_cache_lookup.py` - 缓存和查找表
- `08_api_responses.py` - API 响应类型
- `09_algorithms.py` - 算法实现
- `10_test_data.py` - 测试数据类型
- `comprehensive.py` - 综合示例：数据处理管道

运行示例：
```bash
cd curriculum/v3_9/02_builtin_generic_types/examples
python 01_function_signature.py
```

## 注意事项

### ⚠️ 常见陷阱

1. **不能用于运行时类型检查**
   ```python
   # ❌ 错误 - TypeError
   isinstance([1, 2], list[int])
   
   # ✅ 正确 - 只检查是否为 list
   isinstance([1, 2], list)
   ```

2. **向后兼容性问题**
   ```python
   # ❌ Python 3.8 及以下会报错
   def process(items: list[int]) -> None:
       pass
   
   # ✅ 兼容方案：使用 __future__ 注解（Python 3.7+）
   from __future__ import annotations
   
   def process(items: list[int]) -> None:
       pass
   ```

3. **tuple 的特殊语法**
   ```python
   # 固定长度 tuple（每个位置的类型）
   coords: tuple[float, float] = (1.0, 2.0)
   
   # 可变长度 tuple（所有元素相同类型）
   numbers: tuple[int, ...] = (1, 2, 3, 4, 5)
   ```

4. **混用 typing 和内置类型**
   ```python
   # ❌ 不推荐 - 风格不一致
   from typing import List
   def process(a: List[int], b: list[str]) -> None:
       pass
   
   # ✅ 推荐 - 统一使用内置类型（Python 3.9+）
   def process(a: list[int], b: list[str]) -> None:
       pass
   ```

### ✅ 最佳实践

1. **Python 3.9+ 项目优先使用内置泛型** - 简化代码
2. **需要支持旧版本时使用 `from __future__ import annotations`**
3. **类型别名提升可读性** - 为复杂类型创建别名
4. **配合 mypy/pyright 使用** - 静态类型检查
5. **从简单类型开始** - 逐步添加类型注解

## 与其他版本的关系

- **Python 3.8**: 不支持内置泛型，必须使用 `typing.List` 等
- **Python 3.9**: 引入内置泛型，但 `typing.List` 仍可用
- **Python 3.10+**: 进一步增强，支持联合类型 `X | Y`
- **Python 3.12+**: `typing.List` 等被标记为 deprecated

**迁移策略**:
```python
# Python 3.8
from typing import List, Dict
def process(data: List[Dict[str, int]]) -> None:
    pass

# Python 3.9+ (推荐)
def process(data: list[dict[str, int]]) -> None:
    pass
```

## 扩展阅读

- [PEP 585 – Type Hinting Generics In Standard Collections](https://peps.python.org/pep-0585/)
- [Python 3.9 新特性文档](https://docs.python.org/3/whatsnew/3.9.html#type-hinting-generics-in-standard-collections)
- [mypy 文档：内置泛型](https://mypy.readthedocs.io/en/stable/builtin_types.html)

## 快速检查清单

学完本特性后，你应该能回答：

- [ ] `list[int]` 和 `typing.List[int]` 的区别是什么？
- [ ] 哪些内置类型支持泛型语法？
- [ ] 如何表示可变长度的 tuple 类型？
- [ ] 内置泛型可以用于 `isinstance()` 检查吗？
- [ ] 如何在 Python 3.8 中使用内置泛型语法？

