# typing.Annotated 示例代码目录

本目录包含 **10 个独立场景示例** + **1 个综合示例**，全面展示 `typing.Annotated` 的实际应用。

---

## 📚 示例列表

| 文件 | 场景 | 核心要点 |
|------|------|----------|
| `01_validation_rules.py` | 数据验证规则 | 验证规则与类型绑定 |
| `02_units_measurement.py` | 单位和度量信息 | 物理量单位标注 |
| `03_database_fields.py` | 数据库字段定义 | ORM 约束定义 |
| `04_api_documentation.py` | API 文档生成 | 自动生成文档 |
| `05_config_params.py` | 配置参数说明 | 配置自文档化 |
| `06_serialization.py` | 序列化/反序列化 | 格式化规则 |
| `07_form_validation.py` | 表单验证 | 表单字段元数据 |
| `08_access_control.py` | 权限和访问控制 | 字段级权限 |
| `09_type_conversion.py` | 数据类型转换 | 自动类型转换 |
| `10_test_data.py` | 测试数据生成 | Mock 数据自动生成 |
| `comprehensive.py` | 数据验证框架 | 综合应用 |

---

## 🚀 快速开始

```bash
cd curriculum/v3_9/03_annotated/examples
python 01_validation_rules.py
```

---

## 💡 核心概念

### Annotated 语法
```python
from typing import Annotated

# 基本语法
Annotated[类型, 元数据1, 元数据2, ...]

# 示例
Age = Annotated[int, Range(0, 150), "年龄"]
```

### 运行时访问元数据
```python
from typing import get_type_hints

hints = get_type_hints(MyClass, include_extras=True)
metadata = hints['field'].__metadata__
```

---

## ⚠️ 注意事项

- **类型检查器忽略元数据** - mypy 只检查类型，不验证元数据
- **需要运行时验证** - 元数据约束需要自己实现验证逻辑
- **元数据获取需要 `include_extras=True`**

---

## 📖 学习检查清单

- [ ] 理解 Annotated 的基本语法
- [ ] 知道如何在运行时访问元数据
- [ ] 能够定义自己的元数据类
- [ ] 了解 Annotated 的实际应用场景

---

💡 **提示**：Annotated 特别适合与 Pydantic、FastAPI 等库配合使用！

