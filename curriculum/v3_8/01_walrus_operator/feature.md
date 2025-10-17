# 赋值表达式 (Walrus Operator `:=`)

## 一句话总结

在表达式内部直接赋值并返回值，避免重复计算和临时变量污染作用域。

## 功能详解

### 是什么？

Walrus Operator（海象运算符）`:=` 是 Python 3.8 引入的赋值表达式语法（PEP 572）。它允许你在表达式中同时完成赋值和求值操作，类似于 C 语言的 `=` 在条件判断中的用法。

**语法格式**:
```python
# 传统方式
temp = expensive_function()
if temp > threshold:
    process(temp)

# 使用 walrus operator
if (result := expensive_function()) > threshold:
    process(result)
```

### 解决什么问题？

**问题 1: 重复计算**
```python
# 旧代码 - len() 被调用两次
if len(data) > 10:
    print(f"数据量: {len(data)}")
```

**问题 2: 临时变量污染作用域**
```python
# 旧代码 - temp 在整个函数作用域内可见
temp = compute_something()
if temp is not None:
    process(temp)
# temp 依然存在，可能被误用
```

**问题 3: 列表推导式中无法先过滤后使用中间结果**
```python
# 旧代码 - 需要调用两次 transform()
[transform(x) for x in data if transform(x) is not None]
```

### 语法要点

1. **必须使用括号**（避免优先级混淆）
   ```python
   # 正确
   if (n := len(data)) > 10:
       pass
   
   # 错误 - 语法错误
   if n := len(data) > 10:
       pass
   ```

2. **返回值是赋值的值**
   ```python
   print(result := 42)  # 输出 42，同时 result = 42
   ```

3. **作用域规则**
   - 在推导式中赋值的变量会泄漏到外层作用域（与循环变量不同）
   - 在 lambda 中可以使用（但要注意可读性）

## 核心应用场景

### 1. **循环条件中避免重复调用**
从文件或输入流逐行读取数据时，传统写法需要先读一次判断，再在循环内读取：
```python
# 使用 walrus operator
while (line := file.readline()) != "":
    process(line)
```
**收益**: 代码减少 2-3 行，逻辑更紧凑

### 2. **列表推导式中复用计算结果**
数据转换后需要同时用于过滤和结果构造：
```python
# 传统需要两次调用 heavy_transform
results = [y for x in data if (y := heavy_transform(x)) is not None]
```
**收益**: 性能提升可达 50%（避免重复计算）

### 3. **正则匹配后直接使用结果**
正则匹配成功后需要提取分组内容：
```python
import re
if (match := re.search(r'(\d+)', text)):
    number = int(match.group(1))
```
**收益**: 避免二次匹配，代码更清晰

### 4. **条件判断中减少重复函数调用**
API 调用或数据库查询结果需要同时用于判断和后续处理：
```python
if (user := get_user_from_db(user_id)) and user.is_active:
    send_notification(user)
```
**收益**: 减少数据库查询次数

### 5. **日志过滤与统计**
需要同时判断长度并记录长度值：
```python
long_lines = [line for line in lines if (n := len(line)) > 80 and log_length(n)]
```
**收益**: 避免在 lambda 或辅助函数中传递额外参数

### 6. **命令行输入验证**
交互式程序中验证输入并存储：
```python
while (choice := input("选择操作: ")) not in ["1", "2", "3"]:
    print("无效选择，请重新输入")
handle_choice(choice)
```
**收益**: 输入逻辑集中在循环条件

### 7. **数据流处理中的状态追踪**
在生成器或管道中追踪中间状态：
```python
def process_stream(stream):
    while (batch := stream.read(1024)) and (size := len(batch)) > 0:
        yield process_chunk(batch, size)
```
**收益**: 避免多次计算 len()

### 8. **配置加载中的回退逻辑**
尝试多个配置源，使用第一个成功的：
```python
config = (
    (cfg := load_from_env()) or
    (cfg := load_from_file()) or
    default_config()
)
```
**收益**: 链式回退逻辑更紧凑（但要注意可读性）

### 9. **测试断言中的中间值检查**
需要同时断言中间值和最终结果：
```python
assert (result := calculate()) > 0, f"期望正数，得到 {result}"
```
**收益**: 错误消息中直接包含实际值

### 10. **递归数据结构的深度遍历**
遍历树或图时需要同时赋值和判断：
```python
if (node := tree.get_child(key)) and node.is_valid():
    process(node)
```
**收益**: 短路求值与赋值结合，避免 None 检查

## 示例代码说明

本目录的 `example.py` 演示了一个**日志分析工具**的实际应用场景：

- **业务背景**: 分析 Web 服务器访问日志，提取超长请求和异常 IP
- **技术点**:
  - 使用 walrus operator 在循环中避免重复正则匹配
  - 在列表推导式中复用长度计算结果
  - 条件链中减少重复的字典查询
- **代码规模**: 约 45 行，包含完整的输入数据和输出

运行示例：
```bash
python 01_walrus_operator/example.py
```

## 注意事项

### ⚠️ 常见陷阱

1. **可读性优先**
   ```python
   # ❌ 过度使用导致难以理解
   if (a := foo()) and (b := bar(a)) and (c := baz(b)) > 10:
       pass
   
   # ✅ 复杂逻辑拆分为多行
   a = foo()
   b = bar(a)
   c = baz(b)
   if c > 10:
       pass
   ```

2. **避免在复杂表达式中嵌套**
   ```python
   # ❌ 难以定位赋值发生的时机
   result = [y + (z := transform(y)) for x in data if (y := process(x)) > 0]
   
   # ✅ 嵌套不超过一层
   result = [(y, transform(y)) for x in data if (y := process(x)) > 0]
   ```

3. **作用域泄漏注意**
   ```python
   # n 在推导式外部依然可访问
   squares = [n**2 for i in range(10) if (n := i * 2) > 5]
   print(n)  # 输出最后一个 n 的值 (18)
   ```

4. **不能用于普通赋值语句**
   ```python
   # ❌ 语法错误 - := 必须在表达式中
   (x := 10)
   
   # ✅ 正确的普通赋值
   x = 10
   ```

### ✅ 最佳实践

1. **优先用于简单的条件判断和循环**
2. **避免在 lambda 中使用（除非逻辑极简单）**
3. **团队代码规范明确使用边界**（如限制嵌套层数）
4. **配合类型提示使用**（mypy 3.8+ 支持 walrus operator 类型推断）

## 与其他版本的关系

- **Python 3.7**: 不支持，需要重构为传统写法
- **Python 3.9+**: 配合结构化模式匹配使用更强大
- **Python 3.10+**: 在 match/case 语句中可以使用 walrus operator

## 扩展阅读

- [PEP 572 – Assignment Expressions](https://peps.python.org/pep-0572/)
- [Real Python: The Walrus Operator](https://realpython.com/python-walrus-operator/)
- 争议点：社区曾对此特性有较大争议（Guido 为此短暂退出决策层），阅读 PEP 可了解设计权衡

## 快速检查清单

学完本特性后，你应该能回答：

- [ ] `:=` 和 `=` 的核心区别是什么？
- [ ] 哪些场景下使用 walrus operator 能显著提升代码质量？
- [ ] 什么情况下应该避免使用 walrus operator？
- [ ] 如何在列表推导式中正确使用 `:=`？
- [ ] walrus operator 的作用域规则是什么？

