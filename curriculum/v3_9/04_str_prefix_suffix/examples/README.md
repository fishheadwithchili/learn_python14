# 字符串方法 (removeprefix/removesuffix) 示例代码目录

本目录包含 **10 个独立场景示例** + **1 个综合示例**，全面展示 `str.removeprefix()` 和 `str.removesuffix()` 的实际应用。

---

## 📚 示例列表

| 文件 | 场景 | 核心要点 |
|------|------|----------|
| `01_file_paths.py` | 文件路径处理 | 相对路径转换、扩展名移除 |
| `02_url_handling.py` | URL 路由处理 | 协议移除、路径提取 |
| `03_naming_conventions.py` | 命名约定处理 | 前缀/后缀移除、名称转换 |
| `04_data_cleaning.py` | 数据清洗 | 标记移除、单位提取 |
| `05_log_parsing.py` | 日志解析 | 日志级别提取、消息解析 |
| `06_template_processing.py` | 模板字符串处理 | 模板变量提取、标记移除 |
| `07_protocol_handling.py` | 协议处理 | 多协议支持、协议转换 |
| `08_config_processing.py` | 配置文件处理 | 环境变量、INI 解析 |
| `09_unit_conversion.py` | 单位转换 | 数值提取、单位识别 |
| `10_code_generation.py` | 代码生成 | 注释处理、代码解析 |
| `comprehensive.py` | 文本处理工具集 | 综合应用 |

---

## 🚀 快速开始

```bash
cd curriculum/v3_9/04_str_prefix_suffix/examples
python 01_file_paths.py
```

---

## 💡 核心概念

### removeprefix() - 移除前缀
```python
# 只删除完整前缀
"test.py".removeprefix("test")  # ".py"

# 前缀不存在时返回原字符串
"test.py".removeprefix("hello")  # "test.py"
```

### removesuffix() - 移除后缀
```python
# 只删除完整后缀
"test.py".removesuffix(".py")  # "test"

# 后缀不存在时返回原字符串
"test.py".removesuffix(".txt")  # "test.py"
```

### 与 lstrip/rstrip 的区别
```python
# ❌ lstrip 逐字符删除
"test.py".lstrip("test")  # ".py" (删除所有 t, e, s 字符)

# ✅ removeprefix 只删除完整前缀
"test.py".removeprefix("test")  # ".py"
```

---

## ⚠️ 注意事项

### 大小写敏感
```python
"Hello".removeprefix("hello")  # "Hello" (不匹配)
"Hello".removeprefix("H")  # "ello" (匹配)
```

### 链式调用
```python
# 可以链式调用
text = "[[value]]"
result = text.removeprefix("[").removesuffix("]")  # "[value]"
```

### 不匹配时的行为
```python
# 不匹配时返回原字符串，不会报错
"test".removeprefix("abc")  # "test"
```

---

## 📖 学习检查清单

- [ ] 理解 removeprefix/removesuffix 和 lstrip/rstrip 的区别
- [ ] 知道不匹配时会返回原字符串
- [ ] 能够使用链式调用处理多个前缀/后缀
- [ ] 了解在实际项目中的应用场景

---

## 🎯 适用场景

✅ **适合使用**：
- 文件路径处理
- URL 解析
- 配置文件处理
- 日志解析
- 数据清洗

❌ **不适合使用**：
- 需要逐字符删除（使用 lstrip/rstrip）
- 需要正则表达式（使用 re 模块）
- 大小写不敏感（先 .lower() 再处理）

---

## 🔄 迁移指南

### Python 3.8 → 3.9 迁移

```python
# Python 3.8
if text.startswith(prefix):
    text = text[len(prefix):]

# Python 3.9+
text = text.removeprefix(prefix)
```

---

💡 **提示**：removeprefix/removesuffix 让代码更简洁安全，避免手动切片错误！

