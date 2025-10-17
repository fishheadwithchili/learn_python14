"""
场景 2：ORM 模型的关联查询

应用：数据库模型的关联对象延迟加载
"""

from functools import cached_property
import time

class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
    
    @cached_property
    def orders(self):
        """加载用户订单（数据库查询）"""
        print(f"  [DB查询] 加载用户 {self.name} 的订单...")
        time.sleep(0.1)
        return [
            {"id": 1, "total": 100},
            {"id": 2, "total": 200}
        ]
    
    @cached_property
    def total_spent(self):
        """计算总消费（依赖 orders）"""
        print(f"  [计算] 计算总消费...")
        return sum(order["total"] for order in self.orders)

print("=" * 60)
print("ORM 关联查询")
print("=" * 60)

print("\n创建用户对象：\n")
user = User(1, "Alice")

print(f"用户: {user.name}")

print("\n访问订单：\n")
orders = user.orders
print(f"  订单数: {len(orders)}")

print("\n计算总消费：\n")
total = user.total_spent
print(f"  总消费: ${total}")

print("\n再次访问（无查询）：\n")
print(f"  订单数: {len(user.orders)}")
print(f"  总消费: ${user.total_spent}")

print("\n💡 总结：关联查询只执行一次，减少数据库负载")

