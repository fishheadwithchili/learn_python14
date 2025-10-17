# Python 3.8 版本概览

## 版本背景

Python 3.8 于 2019 年 10 月发布，是一个包含多项重要语法和标准库改进的版本。对于从 3.7 升级的开发者来说，3.8 引入的特性主要集中在提升代码简洁性、API 设计灵活性和调试体验。

## 核心新特性速览

本版本包含 **5 个主要特性**，每个特性都有独立的详细文档：

### 1. 赋值表达式 (Walrus Operator `:=`)
- **目录**: `01_walrus_operator/`
- **重要性**: ⭐⭐⭐⭐⭐
- **一句话**: 在表达式中就地赋值，避免重复计算和临时变量污染
- **典型场景**: 循环条件判断、列表推导式过滤、正则匹配结果复用

### 2. 仅位置参数 (Positional-only Parameters `/`)
- **目录**: `02_positional_only_params/`
- **重要性**: ⭐⭐⭐⭐
- **一句话**: 通过 `/` 限定某些参数只能按位置传递，保护公共 API 稳定性
- **典型场景**: 库设计、API 演化、避免关键字参数命名冲突

### 3. f-string 调试语法 (`f"{var=}"`)
- **目录**: `03_fstring_debug/`
- **重要性**: ⭐⭐⭐⭐
- **一句话**: 快速打印变量名和值，提升调试和日志记录效率
- **典型场景**: 调试输出、数据管道追踪、测试断言消息

### 4. `functools.cached_property`
- **目录**: `04_cached_property/`
- **重要性**: ⭐⭐⭐⭐
- **一句话**: 将计算密集型属性转为惰性求值并缓存结果
- **典型场景**: 配置对象、ORM 模型、数据解析、文件系统访问

### 5. `importlib.metadata`
- **目录**: `05_importlib_metadata/`
- **重要性**: ⭐⭐⭐
- **一句话**: 标准库方式读取已安装包的元数据（版本、入口点等）
- **典型场景**: 依赖版本检查、插件系统、CLI 工具版本显示

## 学习路径建议

### 🎯 推荐学习顺序

1. **先学基础语法** (1-2 小时)
   - `03_fstring_debug/` - 最简单，立即提升调试体验
   - `01_walrus_operator/` - 语法简洁但应用广泛

2. **再学 API 设计** (1-2 小时)
   - `02_positional_only_params/` - 理解库设计的兼容性考量
   - `04_cached_property/` - 优化对象设计

3. **最后学工具类** (0.5-1 小时)
   - `05_importlib_metadata/` - 元数据查询工具

### 📚 依赖关系

- 各特性之间**相互独立**，可以按任意顺序学习
- 如果你主要做**应用开发**，优先学习 1、3、4
- 如果你主要做**库开发**，优先学习 2、4、5

## 与其他版本的关系

- **前置知识**: Python 3.7 基础语法（f-string、type hints、dataclass）
- **后续版本**:
  - Python 3.9 会在 f-string 基础上进一步增强字典操作
  - Python 3.10 引入的 pattern matching 可以与 walrus operator 配合使用
  - Python 3.11 的类型系统增强会扩展 cached_property 的使用场景

## 运行环境

所有示例代码要求 **Python >= 3.8**。建议使用虚拟环境：

```bash
# 创建 3.8 虚拟环境
python3.8 -m venv venv38
source venv38/bin/activate  # Windows: venv38\Scripts\activate

# 运行示例
python 01_walrus_operator/example.py
```

## 快速验证环境

运行以下命令确认你的 Python 版本支持这些特性：

```bash
python -c "import sys; print(f'{sys.version_info=}'); assert sys.version_info >= (3, 8)"
```

## 预计学习时间

- **快速浏览**: 1-2 小时（阅读所有 feature.md）
- **深入学习**: 4-6 小时（运行所有示例、理解场景）
- **实践掌握**: 1-2 周（在实际项目中应用）

---

**下一步**: 进入 `01_walrus_operator/` 开始学习第一个特性！

