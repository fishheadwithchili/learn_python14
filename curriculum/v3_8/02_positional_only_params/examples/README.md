# Positional-only Parameters (/) 示例代码目录

本目录包含 **10 个独立场景示例** + **1 个综合示例**，展示仅位置参数在 API 设计中的应用。

---

## 📚 示例列表

| 文件 | 场景 | 核心要点 |
|------|------|----------|
| `01_api_evolution.py` | API 参数重命名兼容性 | 保护参数名，安全演化 |
| `02_math_functions.py` | 数学函数参数固定 | 位置语义明确 |
| `03_kwargs_conflict.py` | 避免与 kwargs 冲突 | 参数名隔离 |
| `04_wrapper_decorator.py` | 装饰器参数隔离 | 避免命名冲突 |
| `05_factory_pattern.py` | 工厂函数类型参数 | 类型参数固定 |
| `06_callback_interface.py` | 回调接口标准化 | 框架 API 设计 |
| `07_c_extension_compat.py` | C 扩展接口对齐 | 保持一致性 |
| `08_parameter_ordering.py` | 参数重载模拟 | 多态函数设计 |
| `09_prevent_misuse.py` | 防止误用 | 安全设计 |
| `10_full_signature_control.py` | 完整参数分层 | 结合 / 和 * |
| `comprehensive.py` | 数据库 API 演化 | 综合应用 |

---

## 🎯 适用场景

### 库/框架开发
- `01_api_evolution.py` - API 演化
- `02_math_functions.py` - 数学库
- `06_callback_interface.py` - 事件系统
- `07_c_extension_compat.py` - C 扩展

### 安全设计
- `03_kwargs_conflict.py` - 避免冲突
- `09_prevent_misuse.py` - 防止错误

### 高级模式
- `04_wrapper_decorator.py` - 装饰器
- `05_factory_pattern.py` - 工厂模式
- `10_full_signature_control.py` - 完整设计

---

## 🚀 快速开始

```bash
# 按顺序学习
python 01_api_evolution.py
python 02_math_functions.py
...

# 或直接看综合示例
python comprehensive.py
```

---

## 💡 核心概念

仅位置参数的三大用途：
1. **保护 API 演化** - 参数名可以重构
2. **避免参数冲突** - 与 **kwargs 隔离
3. **提升 API 清晰度** - 强制正确调用方式

