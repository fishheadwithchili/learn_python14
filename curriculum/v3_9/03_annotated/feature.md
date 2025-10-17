# typing.Annotated - 类型注解增强

## 一句话总结

为类型注解附加元数据（如验证规则、文档说明、单位信息），不影响类型检查器，但可被运行时工具使用。

## 功能详解

### 是什么？

`typing.Annotated` 是 Python 3.9 引入的类型注解增强机制（PEP 593），允许在类型注解中附加任意元数据。

**语法格式**:
```python
from typing import Annotated

# 基本语法
Annotated[类型, 元数据1, 元数据2, ...]

# 示例
age: Annotated[int, "年龄必须大于0"] = 25
price: Annotated[float, "美元", "含税"] = 99.99
```

### 解决什么问题？

**问题 1: 类型注解缺少额外信息**
```python
# 旧代码 - 只有类型，没有约束信息
def create_user(age: int, email: str) -> None:
    # 年龄范围？邮箱格式？无法从类型注解得知
    pass
```

**问题 2: 验证规则与类型分离**
```python
# 旧代码 - 验证逻辑分散
def validate_age(age: int) -> bool:
    return 0 < age < 150

# 规则和类型定义不在一起
```

**问题 3: 单位和含义不明确**
```python
# 旧代码 - 不知道单位
def calculate_distance(time: float, speed: float) -> float:
    # time 是秒还是小时？speed 是 km/h 还是 m/s？
    return time * speed
```

### 语法要点

1. **基本语法**
   ```python
   from typing import Annotated
   
   # 附加单个元数据
   UserId = Annotated[int, "用户ID必须为正整数"]
   
   # 附加多个元数据
   Price = Annotated[float, "USD", "税后价格", lambda x: x >= 0]
   ```

2. **元数据可以是任意类型**
   ```python
   # 字符串
   Name = Annotated[str, "用户名"]
   
   # 数字
   MaxLength = Annotated[str, 100]
   
   # 函数
   PositiveInt = Annotated[int, lambda x: x > 0]
   
   # 自定义对象
   class Range:
       def __init__(self, min_val, max_val):
           self.min = min_val
           self.max = max_val
   
   Age = Annotated[int, Range(0, 150)]
   ```

3. **类型检查器忽略元数据**
   ```python
   # mypy 只检查 int 类型，忽略元数据
   age: Annotated[int, "必须大于0"] = 25
   age: int = 25  # 对于类型检查器，这两行等价
   ```

4. **运行时访问元数据**
   ```python
   from typing import get_type_hints, Annotated
   
   def func(x: Annotated[int, "metadata"]) -> None:
       pass
   
   # 获取类型提示
   hints = get_type_hints(func, include_extras=True)
   print(hints['x'].__metadata__)  # ('metadata',)
   ```

5. **与其他类型结合**
   ```python
   from typing import Annotated, Optional, List
   
   # 与 Optional 结合
   MaybeAge = Annotated[Optional[int], Range(0, 150)]
   
   # 与 List 结合
   Names = Annotated[list[str], "非空列表"]
   ```

## 核心应用场景

### 1. **数据验证规则**
在 API 参数、数据类字段中附加验证规则：
```python
from typing import Annotated

class Range:
    def __init__(self, min_val, max_val):
        self.min, self.max = min_val, max_val

Age = Annotated[int, Range(0, 150)]
Email = Annotated[str, "email_format"]
```
**收益**: 验证规则与类型定义在一起，便于自动验证

### 2. **单位和度量信息**
为数值类型附加单位信息：
```python
Meters = Annotated[float, "m"]
Seconds = Annotated[float, "s"]
KilometersPerHour = Annotated[float, "km/h"]
```
**收益**: 代码自文档化，减少单位混淆错误

### 3. **数据库字段定义**
ORM 模型中附加数据库约束：
```python
from typing import Annotated

class DBConstraint:
    def __init__(self, max_length=None, unique=False):
        self.max_length = max_length
        self.unique = unique

Username = Annotated[str, DBConstraint(max_length=50, unique=True)]
Bio = Annotated[str, DBConstraint(max_length=500)]
```
**收益**: 类型定义包含数据库约束，自动生成迁移

### 4. **API 文档生成**
为 API 参数附加描述信息：
```python
from typing import Annotated

UserId = Annotated[int, "用户的唯一标识符"]
PageSize = Annotated[int, "每页记录数，默认10，最大100"]
```
**收益**: 自动生成 OpenAPI/Swagger 文档

### 5. **配置参数说明**
为配置项附加说明和默认值：
```python
from typing import Annotated

class Config:
    timeout: Annotated[int, "请求超时时间（秒）", 30]
    retry: Annotated[int, "重试次数", 3]
```
**收益**: 配置项自带文档和默认值

### 6. **序列化/反序列化提示**
为字段附加序列化规则：
```python
from typing import Annotated
from datetime import datetime

class SerializeAs:
    def __init__(self, format_str):
        self.format = format_str

CreatedAt = Annotated[datetime, SerializeAs("iso8601")]
Price = Annotated[float, SerializeAs("currency_usd")]
```
**收益**: 序列化规则与类型绑定

### 7. **表单验证**
Web 表单字段验证：
```python
from typing import Annotated

class FormField:
    def __init__(self, label, placeholder=""):
        self.label = label
        self.placeholder = placeholder

Username = Annotated[str, FormField("用户名", "请输入用户名")]
Password = Annotated[str, FormField("密码", "至少8位")]
```
**收益**: 表单定义和验证一体化

### 8. **权限和访问控制**
为字段附加权限要求：
```python
from typing import Annotated

class Requires:
    def __init__(self, *roles):
        self.roles = roles

Salary = Annotated[float, Requires("admin", "hr")]
SSN = Annotated[str, Requires("admin")]
```
**收益**: 字段级别的访问控制

### 9. **数据类型转换提示**
为类型附加转换规则：
```python
from typing import Annotated

class ConvertFrom:
    def __init__(self, from_type, converter):
        self.from_type = from_type
        self.converter = converter

UserId = Annotated[int, ConvertFrom(str, int)]
Price = Annotated[float, ConvertFrom(str, lambda x: float(x.replace(',', '')))]
```
**收益**: 自动类型转换

### 10. **测试和 Mock 数据生成**
为类型附加测试数据生成提示：
```python
from typing import Annotated

class Example:
    def __init__(self, *examples):
        self.examples = examples

Email = Annotated[str, Example("test@example.com", "user@domain.com")]
Age = Annotated[int, Example(25, 30, 45)]
```
**收益**: 自动生成测试数据

## 示例代码说明

本目录的 `examples/` 包含 **10 个独立场景示例** 和 **1 个综合示例**：

- `01_validation_rules.py` - 数据验证规则
- `02_units_measurement.py` - 单位和度量信息
- `03_database_fields.py` - 数据库字段定义
- `04_api_documentation.py` - API 文档生成
- `05_config_params.py` - 配置参数说明
- `06_serialization.py` - 序列化/反序列化
- `07_form_validation.py` - 表单验证
- `08_access_control.py` - 权限和访问控制
- `09_type_conversion.py` - 数据类型转换
- `10_test_data.py` - 测试数据生成
- `comprehensive.py` - 综合示例：数据验证框架

运行示例：
```bash
cd curriculum/v3_9/03_annotated/examples
python 01_validation_rules.py
```

## 注意事项

### ⚠️ 常见陷阱

1. **类型检查器忽略元数据**
   ```python
   # ❌ 类型检查器不会验证元数据约束
   age: Annotated[int, Range(0, 150)] = 200  # mypy 不会报错
   
   # ✅ 需要运行时验证
   def validate_age(value, annotation):
       for metadata in annotation.__metadata__:
           if isinstance(metadata, Range):
               assert metadata.min <= value <= metadata.max
   ```

2. **元数据获取需要特殊方法**
   ```python
   from typing import get_type_hints
   
   def func(x: Annotated[int, "meta"]) -> None:
       pass
   
   # ❌ 默认不包含元数据
   hints = get_type_hints(func)
   print(hints['x'])  # <class 'int'>
   
   # ✅ 需要 include_extras=True
   hints = get_type_hints(func, include_extras=True)
   print(hints['x'].__metadata__)  # ('meta',)
   ```

3. **元数据顺序敏感**
   ```python
   # 元数据保持顺序
   T1 = Annotated[int, "a", "b"]
   T2 = Annotated[int, "b", "a"]
   # T1 和 T2 的元数据顺序不同
   ```

4. **嵌套 Annotated 会展平**
   ```python
   # 嵌套会被展平
   T1 = Annotated[int, "a"]
   T2 = Annotated[T1, "b"]
   # T2 等价于 Annotated[int, "a", "b"]
   ```

### ✅ 最佳实践

1. **使用有意义的元数据对象** - 而非简单字符串
2. **定义元数据的标准类** - 提升一致性
3. **编写元数据提取工具** - 简化访问
4. **配合 Pydantic/dataclasses 使用** - 自动验证
5. **文档化元数据含义** - 便于团队协作

## 与其他版本的关系

- **Python 3.8**: 不支持，需要使用 `typing_extensions`
  ```python
  from typing_extensions import Annotated  # Python 3.8
  ```
- **Python 3.9+**: 标准库支持
  ```python
  from typing import Annotated  # Python 3.9+
  ```
- **Python 3.11+**: 配合 `typing.Self` 使用更强大

**与其他库的集成**:
- **Pydantic**: 自动使用 Annotated 元数据进行验证
- **FastAPI**: 使用 Annotated 生成 API 文档
- **SQLModel**: 使用 Annotated 定义数据库约束

## 扩展阅读

- [PEP 593 – Flexible function and variable annotations](https://peps.python.org/pep-0593/)
- [Python 3.9 新特性文档](https://docs.python.org/3/whatsnew/3.9.html#type-hinting-generics-in-standard-collections)
- [Pydantic Annotated Validators](https://docs.pydantic.dev/latest/usage/validators/)

## 快速检查清单

学完本特性后，你应该能回答：

- [ ] `Annotated` 的基本语法是什么？
- [ ] 元数据可以是哪些类型？
- [ ] 类型检查器会验证元数据吗？
- [ ] 如何在运行时访问元数据？
- [ ] `Annotated` 有哪些实际应用场景？

