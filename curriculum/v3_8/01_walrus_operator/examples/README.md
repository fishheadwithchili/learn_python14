# Walrus Operator (:=) 示例代码目录

本目录包含 **10 个独立场景示例** + **1 个综合示例**，全面展示赋值表达式的实际应用。

---

## 📚 示例列表

### 独立场景示例（按场景编号）

每个示例专注于一个具体应用场景，代码简洁（10-30 行），可直接运行。

| 文件 | 场景 | 代码行数 | 核心要点 |
|------|------|----------|----------|
| `01_loop_condition.py` | 循环条件避免重复调用 | ~30 | 文件读取、while 循环 |
| `02_list_comprehension.py` | 列表推导式复用计算 | ~35 | 性能优化、避免重复计算 |
| `03_regex_matching.py` | 正则匹配后使用结果 | ~40 | 避免二次匹配 |
| `04_api_call_reuse.py` | API/数据库查询复用 | ~45 | 减少查询次数 |
| `05_log_filter.py` | 日志过滤与统计 | ~50 | len() 复用 |
| `06_cli_input.py` | 命令行输入验证 | ~50 | 交互式程序 |
| `07_stream_processing.py` | 数据流处理 | ~55 | 生成器、流式处理 |
| `08_config_fallback.py` | 配置加载回退 | ~60 | 链式 or 操作 |
| `09_test_assertion.py` | 测试断言中间值 | ~70 | 详细错误消息 |
| `10_tree_traversal.py` | 树/图结构遍历 | ~100 | 递归、深度访问 |

### 综合示例

| 文件 | 说明 | 代码行数 |
|------|------|----------|
| `comprehensive.py` | 完整的日志分析工具 | ~90 | 多场景综合应用 |

---

## 🚀 快速开始

### 方式 1：按顺序学习（推荐）

```bash
# 从简单到复杂，逐个运行
python 01_loop_condition.py
python 02_list_comprehension.py
python 03_regex_matching.py
# ... 继续后面的示例
```

### 方式 2：按需查找

根据你的实际需求，直接跳到对应场景：

- **处理文件/流** → `01_loop_condition.py`, `07_stream_processing.py`
- **性能优化** → `02_list_comprehension.py`, `05_log_filter.py`
- **字符串处理** → `03_regex_matching.py`
- **数据库/API** → `04_api_call_reuse.py`
- **用户交互** → `06_cli_input.py`
- **配置管理** → `08_config_fallback.py`
- **测试编写** → `09_test_assertion.py`
- **数据结构** → `10_tree_traversal.py`

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
阅读 feature.md（了解基本语法）
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
# ❌ 展示没有 walrus operator 的写法

# 3. Walrus operator 方式
print("[Walrus Operator]")
# ✅ 展示改进后的写法

# 4. 总结
print("💡 总结：...")
```

---

## 🎯 场景分类

### 性能优化类
- `02_list_comprehension.py` - 避免重复计算
- `04_api_call_reuse.py` - 减少网络/IO 调用
- `05_log_filter.py` - 复用计算结果

### 代码简化类
- `01_loop_condition.py` - 简化循环逻辑
- `03_regex_matching.py` - 避免重复匹配
- `08_config_fallback.py` - 简化回退逻辑

### 数据处理类
- `07_stream_processing.py` - 流式数据处理
- `10_tree_traversal.py` - 递归结构遍历

### 实用工具类
- `06_cli_input.py` - 用户交互
- `09_test_assertion.py` - 测试代码

---

## ⚠️ 注意事项

### 适合使用的场景
✅ 避免重复计算  
✅ 简化条件判断  
✅ 减少临时变量  
✅ 循环中的赋值+判断  

### 不适合使用的场景
❌ 过度嵌套（超过2层）  
❌ 复杂表达式（影响可读性）  
❌ 团队成员不熟悉的代码库  

---

## 📊 运行环境

- **Python 版本**: >= 3.8
- **依赖**: 无（所有示例使用标准库）
- **运行时间**: 每个示例 < 1 秒

---

## 🔗 相关资源

- **功能详解**: 参考上级目录的 `feature.md`
- **PEP 572**: https://peps.python.org/pep-0572/
- **Python 3.8 新特性**: https://docs.python.org/3/whatsnew/3.8.html

---

## 💬 反馈

如果你发现：
- 示例代码有问题
- 想要添加新的场景
- 有更好的实现方式

欢迎提出改进建议！

