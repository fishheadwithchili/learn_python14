# 字典合并运算符 (`|` 和 `|=`) 示例代码目录

本目录包含 **10 个独立场景示例** + **1 个综合示例**，全面展示字典合并运算符的实际应用。

---

## 📚 示例列表

### 独立场景示例（按场景编号）

每个示例专注于一个具体应用场景，代码简洁（20-50 行），可直接运行。

| 文件 | 场景 | 代码行数 | 核心要点 |
|------|------|----------|----------|
| `01_config_merge.py` | 配置文件合并 | ~40 | 多层配置优先级 |
| `02_api_defaults.py` | API 参数默认值 | ~60 | 避免可变默认参数陷阱 |
| `03_batch_update.py` | 批量字典更新 | ~70 | 使用 `|=` 替代多次赋值 |
| `04_conditional_merge.py` | 条件合并 | ~65 | 根据条件添加键值对 |
| `05_override_keys.py` | 覆盖特定键 | ~80 | 不可变更新模式 |
| `06_multi_source.py` | 多数据源聚合 | ~85 | 数据库+缓存+API |
| `07_template_context.py` | 模板渲染上下文 | ~100 | Web 框架上下文合并 |
| `08_test_data.py` | 测试数据构造 | ~105 | 基于基准数据创建变体 |
| `09_log_context.py` | 日志上下文 | ~115 | 结构化日志多层上下文 |
| `10_feature_flags.py` | 特性开关 | ~150 | A/B 测试、用户分层 |

### 综合示例

| 文件 | 说明 | 代码行数 |
|------|------|----------|
| `comprehensive.py` | 完整的配置管理系统 | ~230 | 多场景综合应用 |

---

## 🚀 快速开始

### 方式 1：按顺序学习（推荐）

```bash
# 从简单到复杂，逐个运行
cd curriculum/v3_9/01_dict_merge_operators/examples

python 01_config_merge.py
python 02_api_defaults.py
python 03_batch_update.py
# ... 继续后面的示例
```

### 方式 2：按需查找

根据你的实际需求，直接跳到对应场景：

- **配置管理** → `01_config_merge.py`, `comprehensive.py`
- **函数参数** → `02_api_defaults.py`
- **数据更新** → `03_batch_update.py`, `05_override_keys.py`
- **条件逻辑** → `04_conditional_merge.py`
- **数据聚合** → `06_multi_source.py`
- **Web 开发** → `07_template_context.py`
- **测试编写** → `08_test_data.py`
- **日志记录** → `09_log_context.py`
- **特性管理** → `10_feature_flags.py`

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

# 1. 导入和数据准备
import ...

# 2. 传统方式示例（对比）
print("[传统方式]")
# ❌ 展示没有 | 运算符的写法

# 3. Python 3.9+ 方式
print("[Python 3.9+]")
# ✅ 展示使用 | 运算符的写法

# 4. 总结
print("💡 总结：...")
```

---

## 🎯 场景分类

### 基础应用类
- `01_config_merge.py` - 配置合并
- `02_api_defaults.py` - 默认参数
- `03_batch_update.py` - 批量更新

### 高级模式类
- `04_conditional_merge.py` - 条件合并
- `05_override_keys.py` - 不可变更新
- `06_multi_source.py` - 多源聚合

### 实战应用类
- `07_template_context.py` - Web 模板
- `08_test_data.py` - 测试数据
- `09_log_context.py` - 日志系统
- `10_feature_flags.py` - 特性开关

---

## ⚠️ 注意事项

### 适合使用的场景
✅ 合并多个配置源  
✅ 设置参数默认值  
✅ 批量更新字典  
✅ 创建字典变体  

### 不适合使用的场景
❌ 深度合并嵌套字典（会完全覆盖）  
❌ 需要自定义合并逻辑  
❌ 非字典类型合并  

### 深度合并问题
```python
a = {"nested": {"x": 1}}
b = {"nested": {"y": 2}}
c = a | b
# 结果: {"nested": {"y": 2}}  ← b 的 nested 完全覆盖 a 的

# 如需深度合并，考虑使用专门的库：
# from deepmerge import always_merger
# c = always_merger.merge(a, b)
```

---

## 📊 运行环境

- **Python 版本**: >= 3.9
- **依赖**: 无（所有示例使用标准库）
- **运行时间**: 每个示例 < 1 秒

---

## 🔗 相关资源

- **功能详解**: 参考上级目录的 `feature.md`
- **PEP 584**: https://peps.python.org/pep-0584/
- **Python 3.9 新特性**: https://docs.python.org/3/whatsnew/3.9.html

---

## 💬 快速参考

### `|` 运算符（合并）
```python
# 创建新字典
result = dict1 | dict2  # dict2 的值覆盖 dict1

# 链式合并
result = default | env | user  # 优先级递增
```

### `|=` 运算符（更新）
```python
# 就地修改
config |= updates  # 等价于 config.update(updates)
```

### 对比传统方式
```python
# 传统：解包语法
merged = {**dict1, **dict2}

# 传统：update 方法
result = dict1.copy()
result.update(dict2)

# 新方式：| 运算符
merged = dict1 | dict2
```

---

## 🎓 学习检查清单

完成所有示例后，你应该能够：

- [ ] 使用 `|` 合并两个或多个字典
- [ ] 使用 `|=` 就地更新字典
- [ ] 理解合并时的优先级规则（右侧覆盖左侧）
- [ ] 在实际项目中应用字典合并运算符
- [ ] 知道何时不应该使用 `|`（如深度合并场景）

---

## 💡 提示

如果你发现：
- 示例代码有问题
- 想要添加新的场景
- 有更好的实现方式

欢迎提出改进建议！

