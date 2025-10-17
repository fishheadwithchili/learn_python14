# 字典合并运算符 (`|` 和 `|=`)

## 一句话总结

使用直观的 `|` 运算符合并字典，使用 `|=` 更新字典，替代繁琐的 `{**dict1, **dict2}` 和 `dict.update()` 语法。

## 功能详解

### 是什么？

字典合并运算符是 Python 3.9 引入的新语法（PEP 584），为字典类型添加了两个运算符：
- `|` (合并运算符)：创建新字典，包含两个字典的所有键值对
- `|=` (更新运算符)：就地更新字典

**语法格式**:
```python
# 合并运算符 | - 创建新字典
dict3 = dict1 | dict2

# 更新运算符 |= - 就地修改
dict1 |= dict2
```

### 解决什么问题？

**问题 1: 字典合并语法不直观**
```python
# 旧代码 - 使用解包语法，不够直观
merged = {**defaults, **user_config}

# 新代码 - 使用 | 运算符，含义清晰
merged = defaults | user_config
```

**问题 2: 字典更新需要方法调用**
```python
# 旧代码 - update() 返回 None，无法链式调用
config = {}
config.update(defaults)
config.update(user_settings)

# 新代码 - 可以链式合并
config = {} | defaults | user_settings
```

**问题 3: 多字典合并代码冗长**
```python
# 旧代码 - 需要多次解包
result = {**dict1, **dict2, **dict3, **dict4}

# 新代码 - 链式运算符
result = dict1 | dict2 | dict3 | dict4
```

### 语法要点

1. **合并规则：右侧优先**
   ```python
   a = {"x": 1, "y": 2}
   b = {"y": 3, "z": 4}
   c = a | b
   # 结果: {"x": 1, "y": 3, "z": 4}
   # b 中的 "y" 覆盖了 a 中的 "y"
   ```

2. **运算符优先级**
   ```python
   # | 的优先级低于算术运算符
   result = base | {"count": total + offset}  # 正确
   ```

3. **类型要求**
   ```python
   # 两侧都必须是字典（或字典子类）
   a | b  # ✅ 正确
   a | []  # ❌ TypeError
   ```

4. **不修改原字典（`|` 运算符）**
   ```python
   original = {"a": 1}
   new = original | {"b": 2}
   # original 仍然是 {"a": 1}
   # new 是 {"a": 1, "b": 2}
   ```

5. **就地修改（`|=` 运算符）**
   ```python
   config = {"a": 1}
   config |= {"b": 2}
   # config 变成 {"a": 1, "b": 2}
   ```

## 核心应用场景

### 1. **配置文件合并**
应用程序通常需要合并默认配置、环境配置和用户配置，三者优先级递增：
```python
config = default_config | env_config | user_config
```
**收益**: 代码清晰表达优先级关系，一行完成三层合并

### 2. **API 参数默认值设置**
函数接收部分参数，需要与默认值合并：
```python
def process_data(data, options=None):
    opts = DEFAULT_OPTIONS | (options or {})
```
**收益**: 避免可变默认参数陷阱，逻辑简洁

### 3. **批量字典更新**
需要同时更新多个字段：
```python
# 更新用户资料
user_profile |= {"updated_at": now(), "version": version + 1}
```
**收益**: 代替多次 `user["key"] = value` 赋值

### 4. **字典的条件合并**
根据条件决定是否添加某些键值对：
```python
params = base_params | ({"auth": token} if authenticated else {})
```
**收益**: 避免 if-else 分支创建临时字典

### 5. **覆盖特定键**
保持大部分键值不变，只覆盖少量键：
```python
updated_record = original_record | {"status": "archived"}
```
**收益**: 不可变更新模式，适合函数式编程

### 6. **多数据源聚合**
从多个数据源收集数据（如不同 API、数据库）：
```python
aggregated = fetch_from_db() | fetch_from_cache() | fetch_from_api()
```
**收益**: 清晰表达数据优先级（后者覆盖前者）

### 7. **模板渲染上下文**
Web 框架中合并全局上下文和页面特定上下文：
```python
context = global_context | page_context | {"title": page_title}
```
**收益**: 模板变量来源一目了然

### 8. **测试数据构造**
基于基准数据创建测试用例的变体：
```python
test_cases = [
    base_data | {"name": "Alice"},
    base_data | {"name": "Bob", "age": 30}
]
```
**收益**: 避免重复定义共同字段

### 9. **日志记录上下文**
为日志添加上下文信息（用户 ID、请求 ID 等）：
```python
log_context = base_log | request_context | {"event": "user_login"}
```
**收益**: 结构化日志更易于聚合

### 10. **特性开关（Feature Flags）**
合并默认特性配置和用户特性配置：
```python
features = default_features | user_tier_features | user_custom_features
```
**收益**: 特性分层清晰，便于 A/B 测试

## 示例代码说明

本目录的 `examples/` 包含 **10 个独立场景示例** 和 **1 个综合示例**：

- `01_config_merge.py` - 配置文件合并（默认+用户）
- `02_api_defaults.py` - API 参数默认值设置
- `03_batch_update.py` - 批量更新字典字段
- `04_conditional_merge.py` - 条件合并（根据布尔值）
- `05_override_keys.py` - 覆盖特定键值对
- `06_multi_source.py` - 多数据源聚合
- `07_template_context.py` - 模板渲染上下文
- `08_test_data.py` - 测试数据构造
- `09_log_context.py` - 日志上下文
- `10_feature_flags.py` - 特性开关管理
- `comprehensive.py` - 综合示例：配置管理系统

运行示例：
```bash
cd curriculum/v3_9/01_dict_merge_operators/examples
python 01_config_merge.py
```

## 注意事项

### ⚠️ 常见陷阱

1. **顺序很重要（右侧覆盖左侧）**
   ```python
   user_config = {"debug": False}
   default_config = {"debug": True}
   
   # ❌ 错误 - 用户配置被默认配置覆盖
   config = user_config | default_config  # {"debug": True}
   
   # ✅ 正确 - 用户配置优先级更高
   config = default_config | user_config  # {"debug": False}
   ```

2. **不支持非字典类型**
   ```python
   # ❌ TypeError - 不能与列表合并
   {"a": 1} | [("b", 2)]
   
   # ✅ 正确 - 先转换为字典
   {"a": 1} | dict([("b", 2)])
   ```

3. **浅拷贝问题（嵌套字典）**
   ```python
   a = {"nested": {"x": 1}}
   b = {"nested": {"y": 2}}
   c = a | b
   # c = {"nested": {"y": 2}}  # b 的 nested 完全覆盖 a 的
   
   # 如果需要深度合并，使用专门的库（如 deepmerge）
   ```

4. **`|=` 返回 None（不能链式调用）**
   ```python
   # ❌ 错误 - |= 返回 None
   result = (config |= updates)  # result 是 None
   
   # ✅ 正确 - |= 修改原字典
   config |= updates
   result = config
   ```

### ✅ 最佳实践

1. **优先使用 `|` 而非解包语法** - 提升可读性
2. **用 `|=` 替代 `update()`** - 除非需要 update() 的返回值（None）
3. **合并超过 3 个字典时考虑分行** - 提升可读性
   ```python
   config = (
       defaults
       | env_settings
       | user_config
       | cli_overrides
   )
   ```
4. **注意性能** - 每次 `|` 都创建新字典，大字典频繁合并时使用 `|=`

## 与其他版本的关系

- **Python 3.8**: 不支持，需使用 `{**dict1, **dict2}` 或 `dict.update()`
- **Python 3.9+**: 推荐使用 `|` 和 `|=`
- **Python 3.10+**: 可与模式匹配结合使用

**向后兼容方案**:
```python
# 支持 Python 3.8
merged = {**dict1, **dict2}

# Python 3.9+
merged = dict1 | dict2
```

## 扩展阅读

- [PEP 584 – Add Union Operators To dict](https://peps.python.org/pep-0584/)
- [Python 3.9 新特性文档](https://docs.python.org/3/whatsnew/3.9.html#dictionary-merge-update-operators)
- 社区讨论：为什么选择 `|` 而不是 `+`（避免与列表加法混淆）

## 快速检查清单

学完本特性后，你应该能回答：

- [ ] `|` 和 `|=` 的区别是什么？
- [ ] 当两个字典有相同的键时，结果如何？
- [ ] `dict1 | dict2` 和 `{**dict1, **dict2}` 的效果是否相同？
- [ ] 何时应该使用 `|` 而非 `|=`？
- [ ] 嵌套字典合并时会发生什么？

