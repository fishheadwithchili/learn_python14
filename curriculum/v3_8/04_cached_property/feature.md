# `functools.cached_property`

## 一句话总结

将计算密集型或 I/O 密集型的属性转换为惰性求值并缓存结果，提升对象访问性能。

## 功能详解

### 是什么？

`cached_property` 是 Python 3.8 在 `functools` 模块中新增的装饰器。它结合了 `@property` 的特性和缓存机制，首次访问时计算属性值并缓存，后续访问直接返回缓存值。

**语法格式**:
```python
from functools import cached_property

class MyClass:
    @cached_property
    def expensive_calculation(self):
        # 只在首次访问时执行
        print("Computing...")
        return sum(range(1000000))

obj = MyClass()
obj.expensive_calculation  # 输出 "Computing..."，返回结果
obj.expensive_calculation  # 直接返回缓存值，不输出
```

### 解决什么问题？

**问题 1: 重复计算浪费资源**
```python
# 旧方式 - 每次访问都重新计算
class DataProcessor:
    @property
    def summary(self):
        return self._compute_summary()  # 每次调用都计算！
    
    def _compute_summary(self):
        # 耗时 5 秒的计算
        return expensive_operation(self.data)

# 多次访问会重复计算
processor = DataProcessor()
processor.summary  # 耗时 5 秒
processor.summary  # 又耗时 5 秒！
```

**问题 2: 手动缓存代码冗长**
```python
# 旧方式 - 手动实现缓存
class MyClass:
    def __init__(self):
        self._cache = {}
    
    @property
    def result(self):
        if 'result' not in self._cache:
            self._cache['result'] = expensive_computation()
        return self._cache['result']

# 需要为每个属性重复这种模式
```

**问题 3: 与实例生命周期绑定**
```python
# 某些属性在对象创建后就不会变化
class User:
    def __init__(self, user_id):
        self.user_id = user_id
    
    @property
    def profile(self):
        # 从数据库加载，用户信息不会变化
        return db.query_user_profile(self.user_id)  # 每次都查询！
```

### 语法要点

1. **基本用法**
   ```python
   from functools import cached_property
   
   class Example:
       @cached_property
       def value(self):
           return expensive_operation()
   ```

2. **访问方式与 property 相同**
   ```python
   obj = Example()
   result = obj.value  # 不需要括号，像普通属性一样访问
   ```

3. **缓存存储位置**
   ```python
   # 缓存存储在实例的 __dict__ 中
   obj = Example()
   obj.value           # 首次计算
   print(obj.__dict__)  # {'value': <cached_result>}
   ```

4. **清除缓存**
   ```python
   # 方法 1: 删除属性
   del obj.value
   obj.value  # 重新计算
   
   # 方法 2: 删除 __dict__ 键
   del obj.__dict__['value']
   ```

5. **不支持设置值**
   ```python
   obj = Example()
   obj.value = 100  # 会覆盖缓存，但不推荐这样做
   ```

6. **线程安全**
   ```python
   # ⚠️ 非线程安全！多线程环境需要额外保护
   # 如果多个线程同时首次访问，可能会重复计算
   ```

## 核心应用场景

### 1. **配置对象的惰性解析**
应用启动时加载配置，某些配置项可能不会被使用：
```python
class AppConfig:
    @cached_property
    def database_url(self):
        # 只在需要时解析环境变量和连接字符串
        return parse_complex_db_url(os.getenv('DATABASE_URL'))
    
    @cached_property
    def redis_client(self):
        # 只在需要时建立 Redis 连接
        return redis.Redis.from_url(self.redis_url)
```
**收益**: 启动速度提升，按需加载

### 2. **ORM 模型的关联查询**
数据库模型的关联对象不总是需要加载：
```python
class User:
    def __init__(self, user_id):
        self.user_id = user_id
    
    @cached_property
    def orders(self):
        # 延迟加载订单列表，只查询一次
        return db.query("SELECT * FROM orders WHERE user_id = ?", self.user_id)
    
    @cached_property
    def total_spent(self):
        return sum(order.amount for order in self.orders)
```
**收益**: 减少数据库查询次数

### 3. **文档解析和元数据提取**
解析大型文件时提取多个派生属性：
```python
class Document:
    def __init__(self, filepath):
        self.filepath = filepath
    
    @cached_property
    def content(self):
        # 读取文件只发生一次
        with open(self.filepath) as f:
            return f.read()
    
    @cached_property
    def word_count(self):
        return len(self.content.split())
    
    @cached_property
    def summary(self):
        # 基于 content 的复杂处理
        return generate_summary(self.content)
```
**收益**: 文件只读取一次，多个属性共享

### 4. **数据集统计信息**
机器学习或数据分析中的统计属性：
```python
class Dataset:
    def __init__(self, data):
        self.data = data
    
    @cached_property
    def mean(self):
        return sum(self.data) / len(self.data)
    
    @cached_property
    def std_dev(self):
        mean = self.mean
        variance = sum((x - mean) ** 2 for x in self.data) / len(self.data)
        return variance ** 0.5
    
    @cached_property
    def normalized(self):
        return [(x - self.mean) / self.std_dev for x in self.data]
```
**收益**: 避免重复遍历大数据集

### 5. **Web 应用的请求上下文**
HTTP 请求对象的派生属性：
```python
class Request:
    def __init__(self, environ):
        self.environ = environ
    
    @cached_property
    def json_body(self):
        # 解析 JSON body 只发生一次
        return json.loads(self.environ['wsgi.input'].read())
    
    @cached_property
    def user_agent(self):
        return parse_user_agent(self.environ.get('HTTP_USER_AGENT', ''))
```
**收益**: 请求处理期间多次访问不重复解析

### 6. **图像处理的派生数据**
图像对象的多个计算属性：
```python
class Image:
    def __init__(self, path):
        self.path = path
    
    @cached_property
    def pixels(self):
        # 加载图像数据
        return load_image(self.path)
    
    @cached_property
    def histogram(self):
        return calculate_histogram(self.pixels)
    
    @cached_property
    def thumbnail(self):
        return resize(self.pixels, (128, 128))
```
**收益**: 图像只加载一次

### 7. **复杂对象的序列化**
对象需要多次序列化但内容不变：
```python
class APIResponse:
    def __init__(self, data):
        self.data = data
    
    @cached_property
    def json_str(self):
        # 序列化是昂贵操作，缓存结果
        return json.dumps(self.data, ensure_ascii=False, indent=2)
    
    @cached_property
    def hash(self):
        return hashlib.sha256(self.json_str.encode()).hexdigest()
```
**收益**: 避免重复序列化

### 8. **单例模式的资源句柄**
全局配置或资源管理器：
```python
class ResourceManager:
    @cached_property
    def thread_pool(self):
        # 线程池只创建一次
        return ThreadPoolExecutor(max_workers=10)
    
    @cached_property
    def connection_pool(self):
        return create_connection_pool(size=20)
```
**收益**: 资源初始化只执行一次

### 9. **科学计算的中间结果**
数值计算中的矩阵分解等：
```python
class Matrix:
    def __init__(self, data):
        self.data = data
    
    @cached_property
    def inverse(self):
        # 矩阵求逆是昂贵操作
        return numpy.linalg.inv(self.data)
    
    @cached_property
    def eigenvalues(self):
        return numpy.linalg.eigvals(self.data)
```
**收益**: 复杂计算只执行一次

### 10. **API 客户端的认证令牌**
需要刷新但在有效期内可复用：
```python
class APIClient:
    @cached_property
    def auth_token(self):
        # 获取认证令牌（有效期 1 小时）
        return self._fetch_auth_token()
    
    def _fetch_auth_token(self):
        response = requests.post(self.auth_url, data=self.credentials)
        return response.json()['token']
    
    def request(self, endpoint):
        # 所有请求复用同一个 token
        return requests.get(endpoint, headers={'Authorization': self.auth_token})
```
**收益**: 减少认证请求次数（需要配合定期清除缓存）

## 示例代码说明

本目录的 `example.py` 演示了一个**文档分析器**的实际应用场景：

- **业务背景**: 构建一个 Markdown 文档分析工具，提取元数据和生成摘要
- **技术点**:
  - 使用 `cached_property` 避免重复读取文件
  - 多个派生属性共享基础数据
  - 展示缓存清除机制
- **代码规模**: 约 50 行，模拟真实文档处理场景

运行示例：
```bash
python 04_cached_property/example.py
```

## 注意事项

### ⚠️ 常见陷阱

1. **不适用于可变数据**
   ```python
   # ❌ 错误用法 - 依赖可变数据
   class Counter:
       def __init__(self):
           self.count = 0
       
       @cached_property
       def double(self):
           return self.count * 2  # 只计算一次！
   
   c = Counter()
   print(c.double)  # 0
   c.count = 5
   print(c.double)  # 仍然是 0！缓存没有更新
   
   # ✅ 正确：使用普通方法或 property
   @property
   def double(self):
       return self.count * 2
   ```

2. **非线程安全**
   ```python
   # ⚠️ 多线程同时首次访问可能重复计算
   import threading
   
   class Example:
       @cached_property
       def value(self):
           print(f"Computing in {threading.current_thread().name}")
           return expensive_operation()
   
   # 解决方案：使用锁保护
   from threading import Lock
   
   class ThreadSafeExample:
       def __init__(self):
           self._lock = Lock()
       
       @cached_property
       def value(self):
           with self._lock:
               # 双重检查锁定
               if 'value' not in self.__dict__:
                   return expensive_operation()
   ```

3. **内存占用**
   ```python
   # ⚠️ 缓存大对象可能导致内存问题
   class DataLoader:
       @cached_property
       def huge_dataset(self):
           return load_10gb_data()  # 缓存会占用大量内存
   
   # 解决方案：提供清除机制
   def clear_cache(self):
       if 'huge_dataset' in self.__dict__:
           del self.__dict__['huge_dataset']
   ```

4. **与继承的交互**
   ```python
   class Base:
       @cached_property
       def value(self):
           return "base"
   
   class Derived(Base):
       @cached_property
       def value(self):
           return "derived"
   
   # ✅ 正常工作，子类会覆盖
   d = Derived()
   print(d.value)  # "derived"
   ```

5. **序列化问题**
   ```python
   import pickle
   
   class Example:
       @cached_property
       def data(self):
           return expensive_computation()
   
   obj = Example()
   obj.data  # 触发计算和缓存
   
   # pickle 会序列化缓存值（存储在 __dict__ 中）
   pickled = pickle.dumps(obj)  # 缓存会被保存
   ```

### ✅ 最佳实践

1. **用于不可变或生命周期内不变的数据**
2. **提供清除缓存的方法**
   ```python
   class MyClass:
       @cached_property
       def data(self):
           return load_data()
       
       def refresh(self):
           # 清除所有缓存
           for key in ['data', 'processed']:
               self.__dict__.pop(key, None)
   ```

3. **文档中说明缓存行为**
4. **多线程环境谨慎使用或添加保护**
5. **大对象考虑弱引用或手动管理**

## 与其他版本的关系

- **Python 3.7**: 不存在，需要手动实现或使用第三方库
- **Python 3.8+**: 标准库支持
- **替代方案**: Django 的 `@cached_property` (功能类似但实现略有不同)

## 性能对比

```python
import time

class WithoutCache:
    @property
    def value(self):
        time.sleep(0.1)  # 模拟耗时操作
        return 42

class WithCache:
    @cached_property
    def value(self):
        time.sleep(0.1)
        return 42

# 测试
obj1 = WithoutCache()
start = time.time()
for _ in range(100):
    _ = obj1.value
print(f"Without cache: {time.time() - start:.2f}s")  # ~10 秒

obj2 = WithCache()
start = time.time()
for _ in range(100):
    _ = obj2.value
print(f"With cache: {time.time() - start:.2f}s")  # ~0.1 秒
```

## 扩展阅读

- [PEP 非官方提案讨论](https://bugs.python.org/issue21145)
- [functools 官方文档](https://docs.python.org/3/library/functools.html#functools.cached_property)
- [Django cached_property 对比](https://docs.djangoproject.com/en/stable/ref/utils/#django.utils.functional.cached_property)

## 快速检查清单

学完本特性后，你应该能回答：

- [ ] `@cached_property` 和 `@property` 的区别是什么？
- [ ] 缓存的值存储在哪里？
- [ ] 如何清除已缓存的属性？
- [ ] 什么场景适合使用 `cached_property`？
- [ ] 使用 `cached_property` 的主要注意事项有哪些？

