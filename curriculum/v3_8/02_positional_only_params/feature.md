# 仅位置参数 (Positional-only Parameters)

## 一句话总结

通过 `/` 标记将函数参数限定为只能按位置传递，保护公共 API 的稳定性并避免关键字参数命名冲突。

## 功能详解

### 是什么？

Positional-only parameters 是 Python 3.8 引入的参数声明语法（PEP 570）。在函数签名中使用 `/` 作为分隔符，`/` 左侧的所有参数只能通过位置传递，不能使用关键字参数形式。

**语法格式**:
```python
def function(pos_only1, pos_only2, /, pos_or_kwd, *, kwd_only):
    #            ^                 ^            ^
    #            |                 |            |
    #      仅位置参数          普通参数     仅关键字参数
    pass

# 调用方式
function(1, 2, 3, kwd_only=4)              # ✅ 正确
function(1, 2, pos_or_kwd=3, kwd_only=4)   # ✅ 正确
function(pos_only1=1, ...)                  # ❌ TypeError
```

### 解决什么问题？

**问题 1: API 演化时的向后兼容**
```python
# 旧版本库
def connect(host, port):
    pass

# 用户代码
connect(host="localhost", port=8080)

# 新版本想重命名参数为 hostname
def connect(hostname, port):  # 💥 破坏用户代码！
    pass
```

**问题 2: 参数名称不具有语义价值**
```python
# divmod(a, b) 的参数名称不重要，只有位置有意义
divmod(dividend=10, divisor=3)  # 过于冗长且无价值
```

**问题 3: 内部参数名称与 kwargs 冲突**
```python
def process(name, **kwargs):
    # 如果 kwargs 中有 'name' 键，会与参数冲突
    pass

# 使用 / 避免冲突
def process(name, /, **kwargs):
    # 现在 kwargs 可以安全地包含 'name' 键
    pass
```

### 语法要点

1. **`/` 的位置**
   - 必须在参数列表中，不能在开头或结尾
   - `/` 后面可以是普通参数、默认参数或 `*args`
   
2. **与 `*` 组合使用**
   ```python
   def func(a, b, /, c, d, *, e, f):
       #   a, b: 仅位置
       #   c, d: 位置或关键字
       #   e, f: 仅关键字
       pass
   ```

3. **默认值依然有效**
   ```python
   def func(a, b=10, /):
       pass
   
   func(1)        # ✅ b 使用默认值 10
   func(1, 20)    # ✅ 位置传递
   func(1, b=20)  # ❌ TypeError
   ```

4. **与 C 扩展对齐**
   - 许多 C 实现的内置函数本身就只接受位置参数
   - 现在 Python 函数可以有相同的行为

## 核心应用场景

### 1. **保护公共 API 的参数名称重构**
库的公共接口需要重命名参数但不想破坏用户代码：
```python
# v1.0 - 参数名可能不理想
def authenticate(u, p, /):  # 用户无法用关键字传递
    pass

# v2.0 - 可以安全地改进参数名
def authenticate(username, password, /):
    pass  # 不会影响现有用户的 authenticate('admin', '123')
```
**收益**: API 演化不破坏兼容性

### 2. **数学/算法函数参数无语义价值**
函数参数位置本身就是约定，名称不重要：
```python
def clamp(value, /, min_val, max_val):
    # value 必须是第一个参数，位置有明确语义
    return max(min_val, min(value, max_val))
```
**收益**: 强制用户按文档顺序调用

### 3. **避免参数名与 kwargs 冲突**
函数接受任意关键字参数，但自身参数名可能与之冲突：
```python
def create_user(name, /, **attributes):
    # attributes 可以包含 'name' 字段而不冲突
    user = {'username': name}
    user.update(attributes)
    return user

create_user('alice', name='Alice Cooper', age=30)  # ✅ 正常工作
```
**收益**: 灵活的 API 设计

### 4. **包装函数/装饰器设计**
装饰器需要自己的参数但不想与被包装函数冲突：
```python
def retry(func, /, max_attempts=3, delay=1.0):
    # func 不会与被装饰函数的参数名冲突
    def wrapper(*args, **kwargs):
        for attempt in range(max_attempts):
            try:
                return func(*args, **kwargs)
            except Exception:
                time.sleep(delay)
        raise
    return wrapper
```
**收益**: 减少命名冲突风险

### 5. **模拟内置函数行为**
自定义函数需要与内置函数保持一致的调用风格：
```python
# 模仿 len(), abs() 等内置函数的行为
def custom_len(obj, /):
    # 用户不能写 custom_len(obj=mylist)
    return sum(1 for _ in obj)
```
**收益**: API 风格一致性

### 6. **工厂函数/构造器模式**
对象构造函数第一个参数通常是类型或标识符：
```python
def create_connection(conn_type, /, host, port, **options):
    # conn_type 强制位置传递，避免 create_connection(conn_type='mysql', ...)
    if conn_type == 'mysql':
        return MySQLConnection(host, port, **options)
    elif conn_type == 'postgres':
        return PostgresConnection(host, port, **options)
```
**收益**: 类型参数位置固定

### 7. **回调函数接口标准化**
框架定义回调接口时固定前几个参数：
```python
def register_handler(event, callback, /, priority=0, **metadata):
    # event 和 callback 必须按位置传递
    # 用户的 callback 可以有任意参数名而不冲突
    pass
```
**收益**: 框架 API 清晰

### 8. **多态函数参数重载**
根据位置参数个数决定行为（类似函数重载）：
```python
def format_date(timestamp, /, fmt=None):
    # 第一个参数始终是时间戳，位置明确
    if fmt is None:
        return default_format(timestamp)
    return custom_format(timestamp, fmt)
```
**收益**: 参数语义明确

### 9. **C 扩展的 Python 接口**
为 C 扩展编写 Python wrapper 时保持一致：
```python
# C 函数 int add(int a, int b) 不支持关键字参数
def add(a, b, /):
    return _c_extension.add(a, b)
```
**收益**: Python 和 C 接口对齐

### 10. **防止误用的安全设计**
某些参数如果用关键字传递可能导致逻辑错误：
```python
def transfer(from_account, to_account, /, amount):
    # 强制位置避免 transfer(to_account=A, from_account=B, ...) 的混淆
    pass
```
**收益**: 减少调用错误

## 示例代码说明

本目录的 `example.py` 演示了一个**数据库连接池 API** 的设计场景：

- **业务背景**: 设计一个通用的数据库连接池库，需要支持多种数据库类型
- **技术点**:
  - 使用 `/` 保护核心参数不被关键字传递
  - 演示 API 参数重命名时的向后兼容性
  - 展示与 `**kwargs` 的配合使用
- **代码规模**: 约 50 行，包含多个版本的 API 演化示例

运行示例：
```bash
python 02_positional_only_params/example.py
```

## 注意事项

### ⚠️ 常见陷阱

1. **过度使用降低可读性**
   ```python
   # ❌ 所有参数都仅位置传递会降低代码可读性
   def process_data(a, b, c, d, e, /):
       pass
   
   # ✅ 只对需要保护的参数使用
   def process_data(data, /, method='average', threshold=0.5):
       pass
   ```

2. **文档必须明确说明**
   ```python
   def func(x, y, /):
       """
       重要：x 和 y 必须按位置传递！
       
       Args:
           x: 第一个参数（仅位置）
           y: 第二个参数（仅位置）
       """
       pass
   ```

3. **与类型提示的结合**
   ```python
   # ✅ 类型提示依然有效
   def add(a: int, b: int, /) -> int:
       return a + b
   ```

4. **不影响内部实现**
   ```python
   def func(a, b, /):
       # 函数内部依然可以用参数名 a 和 b
       return a + b
   ```

### ✅ 最佳实践

1. **库开发者应优先考虑使用**
   - 公共 API 尽可能使用 `/` 保护核心参数
   - 内部 API 可以更自由

2. **文档中明确标注**
   - 在 docstring 中说明哪些参数是仅位置的
   - 给出正确和错误的调用示例

3. **渐进式引入**
   - 新 API 设计时就考虑 `/`
   - 旧 API 升级需要评估影响

4. **与 `*` 配合使用**
   ```python
   def func(pos_only, /, pos_or_kwd, *, kwd_only):
       # 参数层次清晰
       pass
   ```

## 与其他版本的关系

- **Python 3.7**: 不支持 `/` 语法，会报 SyntaxError
- **Python 3.8+**: 完全支持
- **向后兼容**: 如果需要支持 3.7，不能使用此特性

## 内置函数示例

许多 Python 内置函数本身就使用了仅位置参数：

```python
# 这些调用会失败
abs(x=-5)           # ❌ TypeError
len(obj=[1,2,3])    # ❌ TypeError
pow(base=2, exp=3)  # ❌ TypeError

# 必须使用位置传递
abs(-5)             # ✅
len([1,2,3])        # ✅
pow(2, 3)           # ✅
```

查看函数签名：
```python
import inspect
print(inspect.signature(abs))   # (x, /)
print(inspect.signature(pow))   # (base, exp, mod=None, /)
```

## 扩展阅读

- [PEP 570 – Python Positional-Only Parameters](https://peps.python.org/pep-0570/)
- [Python 官方文档：函数定义](https://docs.python.org/3/reference/compound_stmts.html#function-definitions)
- Guido 的设计理念：参数传递方式应该由 API 设计者决定，而非调用者

## 快速检查清单

学完本特性后，你应该能回答：

- [ ] `/` 在函数签名中的作用是什么？
- [ ] 为什么要限制某些参数只能按位置传递？
- [ ] 如何在函数中同时使用 `/` 和 `*`？
- [ ] 仅位置参数如何帮助 API 演化？
- [ ] 什么情况下应该使用仅位置参数？

