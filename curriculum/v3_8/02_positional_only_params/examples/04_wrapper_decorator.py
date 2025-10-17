"""
场景 4：包装函数/装饰器设计

应用：装饰器需要自己的参数但不想与被包装函数冲突
"""

import time
import functools

print("=" * 60)
print("装饰器中的参数隔离")
print("=" * 60)

# ✅ 使用仅位置参数设计装饰器
def retry(func, /, max_attempts=3, delay=1.0, backoff=2.0):
    """
    重试装饰器
    
    参数:
        func: 要包装的函数（仅位置，避免冲突）
        max_attempts: 最大尝试次数
        delay: 初始延迟（秒）
        backoff: 延迟倍增因子
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        current_delay = delay
        last_exception = None
        
        for attempt in range(max_attempts):
            try:
                result = func(*args, **kwargs)
                if attempt > 0:
                    print(f"  ✅ 第 {attempt + 1} 次尝试成功")
                return result
            except Exception as e:
                last_exception = e
                if attempt < max_attempts - 1:
                    print(f"  ⚠️  第 {attempt + 1} 次失败: {e}")
                    print(f"  等待 {current_delay:.1f}s 后重试...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        
        print(f"  ❌ 所有 {max_attempts} 次尝试都失败")
        raise last_exception
    
    return wrapper

# 模拟不稳定的函数
attempt_count = 0

def unstable_api_call():
    """模拟不稳定的 API 调用"""
    global attempt_count
    attempt_count += 1
    if attempt_count < 2:
        raise ConnectionError("网络不稳定")
    return {"status": "success", "data": [1, 2, 3]}

print("\n使用重试装饰器：\n")

# 应用装饰器
retryable_call = retry(unstable_api_call, max_attempts=3, delay=0.1, backoff=1.5)

try:
    result = retryable_call()
    print(f"  最终结果: {result}")
except Exception as e:
    print(f"  失败: {e}")

print("\n" + "=" * 60)
print("缓存装饰器")
print("=" * 60)

def cached(func, /, cache_size=128, ttl=None):
    """
    简单的缓存装饰器
    
    参数:
        func: 要缓存的函数（仅位置）
        cache_size: 缓存大小
        ttl: 缓存过期时间（秒）
    """
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            cached_result, cached_time = cache[args]
            if ttl is None or (time.time() - cached_time) < ttl:
                print(f"  💾 缓存命中: {args}")
                return cached_result
        
        print(f"  🔄 计算中: {args}")
        result = func(*args)
        cache[args] = (result, time.time())
        
        # 简单的 LRU：超过大小就清空
        if len(cache) > cache_size:
            cache.clear()
        
        return result
    
    return wrapper

@cached
def expensive_calculation(n):
    """耗时计算"""
    time.sleep(0.1)  # 模拟耗时
    return n ** 2

print("\n测试缓存：\n")

result1 = expensive_calculation(5)
print(f"  结果: {result1}")

result2 = expensive_calculation(5)  # 应该从缓存读取
print(f"  结果: {result2}")

result3 = expensive_calculation(10)
print(f"  结果: {result3}")

print("\n" + "=" * 60)
print("日志装饰器")
print("=" * 60)

def log_calls(func, /, prefix="CALL", include_result=True):
    """
    记录函数调用
    
    参数:
        func: 要记录的函数（仅位置）
        prefix: 日志前缀
        include_result: 是否记录返回值
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ', '.join(map(repr, args))
        kwargs_str = ', '.join(f'{k}={v!r}' for k, v in kwargs.items())
        all_args = ', '.join(filter(None, [args_str, kwargs_str]))
        
        print(f"  [{prefix}] {func.__name__}({all_args})")
        
        result = func(*args, **kwargs)
        
        if include_result:
            print(f"  [{prefix}] {func.__name__} → {result!r}")
        
        return result
    
    return wrapper

@log_calls
def add(a, b):
    """简单的加法"""
    return a + b

@log_calls
def greet(name, greeting="Hello"):
    """问候函数"""
    return f"{greeting}, {name}!"

print("\n测试日志记录：\n")

result = add(3, 5)
result = greet("Alice")
result = greet("Bob", greeting="Hi")

print("\n" + "=" * 60)
print("组合多个装饰器")
print("=" * 60)

print("""
仅位置参数让装饰器可以安全组合：

@log_calls
@cached
@retry
def complex_function():
    pass

每个装饰器的 'func' 参数都是仅位置的，
不会与被装饰函数的参数或其他装饰器的参数冲突。
""")

print("💡 总结：仅位置参数让装饰器设计更安全，避免参数命名冲突")

