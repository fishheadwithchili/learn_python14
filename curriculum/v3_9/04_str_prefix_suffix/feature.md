# 字符串方法：removeprefix() 和 removesuffix()

## 一句话总结

安全地移除字符串的前缀或后缀，避免 `lstrip()` 和 `rstrip()` 的字符逐个删除陷阱。

## 功能详解

### 是什么？

Python 3.9 引入了两个新的字符串方法（PEP 616）：
- `str.removeprefix(prefix)`: 移除字符串开头的指定前缀
- `str.removesuffix(suffix)`: 移除字符串末尾的指定后缀

**语法格式**:
```python
# 移除前缀
result = text.removeprefix("前缀")

# 移除后缀
result = text.removesuffix("后缀")
```

### 解决什么问题？

**问题 1: lstrip/rstrip 会逐字符删除**
```python
# ❌ 错误 - lstrip 逐字符删除，不是删除前缀
"test.py".lstrip("test")  # 结果: ".py" ❌
# "test" 中的每个字符都被删除

# ✅ 正确 - removeprefix 只删除完整前缀
"test.py".removeprefix("test")  # 结果: ".py" ✅
```

**问题 2: 手动前缀/后缀删除容易出错**
```python
# 旧代码 - 需要手动检查和切片
if filename.startswith("prefix_"):
    filename = filename[len("prefix_"):]  # 容易写错

# 新代码 - 一行搞定
filename = filename.removeprefix("prefix_")
```

### 语法要点

1. **只删除一次，从开头/结尾匹配**
   ```python
   "aaabbb".removeprefix("aa")  # "abbb" (只删除开头的 "aa")
   "aaabbb".removesuffix("bb")  # "aaab" (只删除结尾的 "bb")
   ```

2. **前缀/后缀不存在时返回原字符串**
   ```python
   "hello".removeprefix("hi")  # "hello" (没有改变)
   "hello".removesuffix("bye")  # "hello" (没有改变)
   ```

3. **大小写敏感**
   ```python
   "Hello".removeprefix("hello")  # "Hello" (大小写不匹配)
   "Hello".removeprefix("H")  # "ello" (匹配)
   ```

4. **空字符串也有效**
   ```python
   "test".removeprefix("")  # "test"
   "test".removesuffix("")  # "test"
   ```

5. **链式调用**
   ```python
   text = "[[value]]"
   result = text.removeprefix("[").removesuffix("]")  # "[value]"
   ```

## 核心应用场景

### 1. **文件路径处理**
移除路径前缀，提取相对路径：
```python
path = "/home/user/project/src/main.py"
relative = path.removeprefix("/home/user/project/")
# "src/main.py"
```
**收益**: 简化路径操作，代码更清晰

### 2. **URL 路由处理**
移除 URL 前缀，提取路由路径：
```python
url = "https://api.example.com/v1/users/123"
route = url.removeprefix("https://api.example.com")
# "/v1/users/123"
```
**收益**: 简化 URL 解析

### 3. **文件扩展名处理**
移除文件扩展名：
```python
filename = "document.pdf"
basename = filename.removesuffix(".pdf")  # "document"
```
**收益**: 比切片更安全

### 4. **命名约定处理**
移除命名前缀/后缀：
```python
class_name = "TestUserModel"
model_name = class_name.removeprefix("Test").removesuffix("Model")
# "User"
```
**收益**: 简化命名转换

### 5. **数据清洗**
移除数据中的固定标记：
```python
data = "ID:12345"
value = data.removeprefix("ID:")  # "12345"
```
**收益**: 数据提取更简洁

### 6. **日志解析**
移除日志前缀，提取消息：
```python
log = "[ERROR] Connection failed"
message = log.removeprefix("[ERROR] ")  # "Connection failed"
```
**收益**: 日志处理更清晰

### 7. **模板字符串处理**
移除模板标记：
```python
template = "{{ variable }}"
var = template.removeprefix("{{ ").removesuffix(" }}")  # "variable"
```
**收益**: 模板解析更简单

### 8. **协议处理**
移除协议前缀：
```python
url = "https://example.com"
domain = url.removeprefix("https://")  # "example.com"
```
**收益**: 协议无关处理

### 9. **环境变量处理**
移除环境变量前缀：
```python
env_var = "APP_DATABASE_URL"
var_name = env_var.removeprefix("APP_")  # "DATABASE_URL"
```
**收益**: 配置项命名简化

### 10. **单元转换**
移除单位后缀：
```python
value = "100px"
number = value.removesuffix("px")  # "100"
```
**收益**: 单位解析更简单

## 示例代码说明

本目录的 `examples/` 包含 **10 个独立场景示例** 和 **1 个综合示例**。

运行示例：
```bash
cd curriculum/v3_9/04_str_prefix_suffix/examples
python 01_file_paths.py
```

## 注意事项

### ⚠️ 常见陷阱

1. **与 lstrip/rstrip 的区别**
   ```python
   # ❌ lstrip 逐字符删除
   "mississippi".lstrip("mis")  # "ppi" (删除了所有 m, i, s)
   
   # ✅ removeprefix 只删除完整前缀
   "mississippi".removeprefix("mis")  # "sissippi"
   ```

2. **大小写敏感**
   ```python
   "Hello.TXT".removesuffix(".txt")  # "Hello.TXT" (不匹配)
   "Hello.TXT".removesuffix(".TXT")  # "Hello" (匹配)
   ```

3. **不匹配时返回原字符串**
   ```python
   result = "test".removeprefix("abc")
   # result 仍然是 "test"，不是空字符串
   ```

### ✅ 最佳实践

1. **优先使用 removeprefix/removesuffix** - 而非切片
2. **需要大小写不敏感时先转换** - 使用 `.lower()` 配合
3. **链式调用简洁** - 但不要过度嵌套
4. **配合条件检查** - 重要场景先验证前缀/后缀存在

## 与其他版本的关系

- **Python 3.8**: 不支持，需手动切片
  ```python
  # Python 3.8
  if text.startswith(prefix):
      text = text[len(prefix):]
  ```
- **Python 3.9+**: 推荐使用 removeprefix/removesuffix

## 扩展阅读

- [PEP 616 – String methods to remove prefixes and suffixes](https://peps.python.org/pep-0616/)
- [Python 3.9 新特性文档](https://docs.python.org/3/whatsnew/3.9.html#str-removeprefix-and-str-removesuffix)

## 快速检查清单

- [ ] removeprefix/removesuffix 和 lstrip/rstrip 的区别？
- [ ] 前缀/后缀不匹配时会发生什么？
- [ ] 如何移除多个前缀/后缀？
- [ ] 大小写敏感还是不敏感？

