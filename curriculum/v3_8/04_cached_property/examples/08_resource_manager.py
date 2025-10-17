"""场景 8：资源管理器单例"""
from functools import cached_property

class ResourceManager:
    @cached_property
    def thread_pool(self):
        print(f"  [创建线程池]...")
        return "ThreadPool(10)"
    
    @cached_property
    def connection_pool(self):
        print(f"  [创建连接池]...")
        return "ConnectionPool(20)"

print("=" * 60)
rm = ResourceManager()
print(f"线程池: {rm.thread_pool}")
print(f"连接池: {rm.connection_pool}")
print(f"再次: {rm.thread_pool}")
print("💡 资源只初始化一次")

