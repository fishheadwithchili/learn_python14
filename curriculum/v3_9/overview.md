# Python 3.9 版本概览

## 版本背景

Python 3.9 于 2020 年 10 月发布，是一个注重开发体验优化和类型系统增强的版本。对于从 3.8 升级的开发者来说，3.9 引入的特性主要集中在简化字典操作、提升类型注解的可读性和实用性。

## 核心新特性速览

本版本包含 **5 个主要特性**，每个特性都有独立的详细文档：

### 1. 字典合并运算符 (`|` 和 `|=`)
- **目录**: `01_dict_merge_operators/`
- **重要性**: ⭐⭐⭐⭐⭐
- **一句话**: 使用直观的 `|` 运算符合并字典，替代繁琐的 `{**dict1, **dict2}` 语法
- **典型场景**: 配置合并、默认值覆盖、字典更新操作

### 2. 内置泛型类型 (`list[int]`, `dict[str, int]`)
- **目录**: `02_builtin_generic_types/`
- **重要性**: ⭐⭐⭐⭐⭐
- **一句话**: 直接使用 `list[int]` 而非 `typing.List[int]`，简化类型注解
- **典型场景**: 函数签名、类属性注解、数据类定义

### 3. `typing.Annotated` 类型注解增强
- **目录**: `03_annotated/`
- **重要性**: ⭐⭐⭐⭐
- **一句话**: 为类型注解附加元数据（如验证规则、文档说明）
- **典型场景**: API 参数验证、ORM 字段定义、数据验证框架

### 4. 字符串方法 (`removeprefix` / `removesuffix`)
- **目录**: `04_str_prefix_suffix/`
- **重要性**: ⭐⭐⭐⭐
- **一句话**: 安全地移除字符串的前缀或后缀，避免 `lstrip`/`rstrip` 的陷阱
- **典型场景**: 文件路径处理、URL 解析、字符串清理

### 5. `zoneinfo` 时区支持
- **目录**: `05_zoneinfo/`
- **重要性**: ⭐⭐⭐
- **一句话**: 标准库内置时区支持，替代第三方库 `pytz`
- **典型场景**: 跨时区时间转换、国际化应用、日志时间戳

## 学习路径建议

### 🎯 推荐学习顺序

1. **先学高频使用特性** (2-3 小时)
   - `01_dict_merge_operators/` - 立即提升字典操作体验
   - `04_str_prefix_suffix/` - 简单但极其实用
   - `02_builtin_generic_types/` - 类型注解的未来趋势

2. **再学进阶特性** (1-2 小时)
   - `03_annotated/` - 类型系统深度应用
   - `05_zoneinfo/` - 时区处理专题

### 📚 依赖关系

- `02_builtin_generic_types/` 是 `03_annotated/` 的前置知识
- 其他特性相互独立，可按任意顺序学习
- 如果你主要做**Web 开发**，优先学习 1、3、4、5
- 如果你主要做**库开发**，优先学习 2、3

## 与其他版本的关系

- **前置知识**: Python 3.8（特别是 walrus operator 和 f-string debug）
- **后续版本**:
  - Python 3.10 会在类型系统基础上引入联合类型简写 `X | Y`
  - Python 3.10 的 `match/case` 可以与字典合并运算符配合使用
  - Python 3.11 的 `typing.Self` 建立在内置泛型的基础上

## 运行环境

所有示例代码要求 **Python >= 3.9**。建议使用虚拟环境：

```bash
# 创建 3.9 虚拟环境
python3.9 -m venv venv39
source venv39/bin/activate  # Windows: venv39\Scripts\activate

# 运行示例
python 01_dict_merge_operators/examples/01_basic_merge.py
```

## 快速验证环境

运行以下命令确认你的 Python 版本支持这些特性：

```bash
python -c "import sys; print(f'{sys.version_info=}'); assert sys.version_info >= (3, 9)"
```

## 预计学习时间

- **快速浏览**: 1-2 小时（阅读所有 feature.md）
- **深入学习**: 5-7 小时（运行所有示例、理解场景）
- **实践掌握**: 1-2 周（在实际项目中应用）

## 核心改进亮点

### 🎯 开发体验提升
- 字典操作更直观（`|` 运算符）
- 类型注解更简洁（内置泛型）
- 字符串处理更安全（prefix/suffix 方法）

### 🎯 标准库增强
- 时区支持内置化（不再依赖 pytz）
- 类型系统元数据支持（Annotated）

### 🎯 向后兼容性
- 所有新特性都是可选的增强
- 旧代码无需修改即可运行
- 逐步迁移策略友好

---

**下一步**: 进入 `01_dict_merge_operators/` 开始学习第一个特性！

