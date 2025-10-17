# 内置泛型类型示例代码目录

本目录包含 **10 个独立场景示例** + **1 个综合示例**，全面展示 Python 3.9 内置泛型类型的实际应用。

---

## 📚 示例列表

### 独立场景示例（按场景编号）

每个示例专注于一个具体应用场景，代码简洁（30-60 行），可直接运行。

| 文件 | 场景 | 代码行数 | 核心要点 |
|------|------|----------|----------|
| `01_function_signature.py` | 函数签名类型注解 | ~70 | 无需导入 typing.List |
| `02_class_attributes.py` | 类属性类型注解 | ~130 | 类数据结构清晰 |
| `03_dataclass_fields.py` | 数据类字段定义 | ~140 | dataclass + 内置泛型 |
| `04_nested_structures.py` | 嵌套数据结构 | ~155 | JSON、树、图结构 |
| `05_generic_functions.py` | 泛型函数 | ~150 | TypeVar + 内置泛型 |
| `06_config_objects.py` | 配置对象 | ~160 | 配置类型安全 |
| `07_cache_lookup.py` | 缓存和查找表 | ~185 | LRU/TTL 缓存 |
| `08_api_responses.py` | API 响应类型 | ~170 | 数据契约清晰 |
| `09_algorithms.py` | 算法实现 | ~175 | 算法类型安全 |
| `10_test_data.py` | 测试数据类型 | ~200 | 测试数据规范 |

### 综合示例

| 文件 | 说明 | 代码行数 |
|------|------|----------|
| `comprehensive.py` | 完整的数据处理管道 | ~280 | 多场景综合应用 |

---

## 🚀 快速开始

### 方式 1：按顺序学习（推荐）

```bash
# 从简单到复杂，逐个运行
cd curriculum/v3_9/02_builtin_generic_types/examples

python 01_function_signature.py
python 02_class_attributes.py
python 03_dataclass_fields.py
# ... 继续后面的示例
```

### 方式 2：按需查找

根据你的实际需求，直接跳到对应场景：

- **函数类型注解** → `01_function_signature.py`
- **类设计** → `02_class_attributes.py`, `03_dataclass_fields.py`
- **复杂数据结构** → `04_nested_structures.py`
- **通用工具函数** → `05_generic_functions.py`
- **配置管理** → `06_config_objects.py`
- **缓存系统** → `07_cache_lookup.py`
- **API 开发** → `08_api_responses.py`
- **算法实现** → `09_algorithms.py`
- **测试开发** → `10_test_data.py`

### 方式 3：综合应用

先看综合示例了解整体效果：

```bash
python comprehensive.py
```

然后再深入学习各个场景的细节。

---

## 📖 学习建议

### 1. 初学者路径

```
阅读 ../feature.md（了解基本语法）
    ↓
运行 01-03（基础场景）
    ↓
运行 comprehensive.py（看整体效果）
    ↓
按需学习其他场景
```

### 2. 实践者路径

```
根据实际问题 → 找到对应场景 → 运行示例 → 应用到项目
```

### 3. 探索式学习

```
全部运行一遍 → 修改参数观察效果 → 编写自己的变体
```

---

## 💡 每个示例的结构

所有示例遵循统一的结构：

```python
"""
场景说明

应用：具体的业务场景描述
"""

# ✅ Python 3.9+ 方式：使用内置泛型

def process(data: list[int]) -> dict[str, float]:
    """函数实现"""
    ...

# 运行示例
print("场景演示")
# 展示具体使用
```

---

## 🎯 场景分类

### 基础应用类
- `01_function_signature.py` - 函数类型注解
- `02_class_attributes.py` - 类属性注解
- `03_dataclass_fields.py` - 数据类定义

### 数据结构类
- `04_nested_structures.py` - 嵌套结构
- `07_cache_lookup.py` - 缓存查找表
- `09_algorithms.py` - 算法数据结构

### 实战应用类
- `05_generic_functions.py` - 泛型工具
- `06_config_objects.py` - 配置管理
- `08_api_responses.py` - API 开发
- `10_test_data.py` - 测试开发

---

## ⚠️ 注意事项

### Python 版本要求

- **Python 3.9+**: 直接使用内置泛型
  ```python
  def process(data: list[int]) -> None:
      pass
  ```

- **Python 3.8 及以下**: 需要从 typing 导入
  ```python
  from typing import List
  
  def process(data: List[int]) -> None:
      pass
  ```

- **兼容方案**: 使用 `from __future__ import annotations`
  ```python
  from __future__ import annotations
  
  # 现在可以在 Python 3.7+ 中使用内置泛型语法
  def process(data: list[int]) -> None:
      pass
  ```

### 常见陷阱

1. **运行时类型检查**
   ```python
   # ❌ 错误 - 不能用于 isinstance
   isinstance([1, 2], list[int])  # TypeError
   
   # ✅ 正确 - 只检查容器类型
   isinstance([1, 2], list)  # True
   ```

2. **tuple 的特殊语法**
   ```python
   # 固定长度
   coords: tuple[float, float] = (1.0, 2.0)
   
   # 可变长度
   numbers: tuple[int, ...] = (1, 2, 3, 4)
   ```

3. **与 typing 模块混用**
   ```python
   # ❌ 不推荐 - 风格不一致
   from typing import List, Dict
   def f(a: List[int], b: dict[str, int]) -> None:
       pass
   
   # ✅ 推荐 - 统一使用内置泛型
   def f(a: list[int], b: dict[str, int]) -> None:
       pass
   ```

---

## 📊 运行环境

- **Python 版本**: >= 3.9（或 3.7+ 配合 `from __future__ import annotations`）
- **依赖**: 无（所有示例使用标准库）
- **运行时间**: 每个示例 < 1 秒

---

## 🔗 相关资源

- **功能详解**: 参考上级目录的 `feature.md`
- **PEP 585**: https://peps.python.org/pep-0585/
- **Python 3.9 新特性**: https://docs.python.org/3/whatsnew/3.9.html

---

## 💬 快速参考

### 常用内置泛型类型

```python
# 容器类型
list[int]
dict[str, int]
set[str]
frozenset[int]
tuple[int, str]      # 固定长度
tuple[int, ...]      # 可变长度

# collections 类型
from collections import deque, defaultdict
deque[int]
defaultdict[str, list[int]]

# 类型别名
Vector = list[float]
Matrix = list[list[float]]
```

### 迁移指南

```python
# Python 3.8 → 3.9 迁移

# 旧代码
from typing import List, Dict, Set, Tuple
def process(data: List[Dict[str, int]]) -> Set[Tuple[str, int]]:
    pass

# 新代码（Python 3.9+）
def process(data: list[dict[str, int]]) -> set[tuple[str, int]]:
    pass
```

---

## 🎓 学习检查清单

完成所有示例后，你应该能够：

- [ ] 使用 `list[int]` 而不是 `typing.List[int]`
- [ ] 为函数参数和返回值添加类型注解
- [ ] 在 dataclass 中使用内置泛型
- [ ] 表示嵌套数据结构的类型
- [ ] 编写类型安全的泛型函数
- [ ] 知道何时仍需使用 `typing` 模块（如 TypeVar）

---

## 💡 最佳实践

1. **Python 3.9+ 项目统一使用内置泛型**
2. **配合 mypy 或 pyright 进行类型检查**
3. **为公共 API 添加类型注解**
4. **使用类型别名提升复杂类型的可读性**
5. **逐步添加类型注解，不必一次性完成**

---

## 🔄 与 typing 模块的对照表

| typing 模块 | 内置泛型 (3.9+) |
|------------|----------------|
| `List[int]` | `list[int]` |
| `Dict[str, int]` | `dict[str, int]` |
| `Set[str]` | `set[str]` |
| `Tuple[int, str]` | `tuple[int, str]` |
| `FrozenSet[int]` | `frozenset[int]` |
| `Type[MyClass]` | `type[MyClass]` |

注意：`typing.Union`, `typing.Optional`, `typing.TypeVar` 等仍需从 typing 模块导入。

---

如果你发现示例有问题或有改进建议，欢迎提出反馈！

