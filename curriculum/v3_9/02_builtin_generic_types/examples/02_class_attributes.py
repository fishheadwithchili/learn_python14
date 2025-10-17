"""
场景 2：类属性类型注解

应用：在类定义中声明属性类型，提升代码可维护性
"""

# ✅ Python 3.9+ 方式：直接使用内置类型

class ShoppingCart:
    """购物车类"""
    
    # 类属性类型注解
    items: dict[str, int]  # 商品ID -> 数量
    prices: dict[str, float]  # 商品ID -> 价格
    discounts: list[tuple[str, float]]  # (商品ID, 折扣率)
    
    def __init__(self):
        self.items = {}
        self.prices = {}
        self.discounts = []
    
    def add_item(self, item_id: str, quantity: int, price: float) -> None:
        """添加商品"""
        self.items[item_id] = self.items.get(item_id, 0) + quantity
        self.prices[item_id] = price
    
    def add_discount(self, item_id: str, discount: float) -> None:
        """添加折扣"""
        self.discounts.append((item_id, discount))
    
    def calculate_total(self) -> dict[str, float]:
        """计算总价"""
        subtotal = sum(
            self.items[item_id] * self.prices[item_id]
            for item_id in self.items
        )
        
        # 应用折扣
        discount_amount = sum(
            self.items.get(item_id, 0) * self.prices.get(item_id, 0) * discount
            for item_id, discount in self.discounts
        )
        
        return {
            'subtotal': subtotal,
            'discount': discount_amount,
            'total': subtotal - discount_amount
        }


class UserDatabase:
    """用户数据库类"""
    
    users: dict[int, dict[str, str]]  # 用户ID -> 用户信息
    email_index: dict[str, int]  # 邮箱 -> 用户ID
    active_sessions: set[int]  # 活跃会话的用户ID集合
    
    def __init__(self):
        self.users = {}
        self.email_index = {}
        self.active_sessions = set()
    
    def add_user(self, user_id: int, email: str, name: str) -> None:
        """添加用户"""
        self.users[user_id] = {"email": email, "name": name}
        self.email_index[email] = user_id
    
    def get_user_by_email(self, email: str) -> dict[str, str] | None:
        """通过邮箱查找用户"""
        user_id = self.email_index.get(email)
        return self.users.get(user_id) if user_id else None
    
    def login(self, user_id: int) -> None:
        """用户登录"""
        self.active_sessions.add(user_id)
    
    def get_active_users(self) -> list[dict[str, str]]:
        """获取所有活跃用户"""
        return [self.users[uid] for uid in self.active_sessions if uid in self.users]


print("=" * 60)
print("场景 2：类属性类型注解")
print("=" * 60)

# 测试购物车
print("\n[示例 1] 购物车系统：\n")

cart = ShoppingCart()
cart.add_item("apple", 3, 10.0)
cart.add_item("banana", 5, 5.0)
cart.add_item("orange", 2, 8.0)
cart.add_discount("apple", 0.1)  # 10% 折扣

print(f"购物车商品: {cart.items}")
print(f"商品价格: {cart.prices}")
print(f"折扣信息: {cart.discounts}")

total_info = cart.calculate_total()
print(f"\n总价信息:")
print(f"  小计: {total_info['subtotal']:.2f}")
print(f"  折扣: {total_info['discount']:.2f}")
print(f"  合计: {total_info['total']:.2f}")

# 测试用户数据库
print("\n[示例 2] 用户数据库：\n")

db = UserDatabase()
db.add_user(1, "alice@example.com", "Alice")
db.add_user(2, "bob@example.com", "Bob")
db.add_user(3, "charlie@example.com", "Charlie")

print(f"总用户数: {len(db.users)}")

# 用户登录
db.login(1)
db.login(3)

print(f"活跃会话: {db.active_sessions}")

# 查询用户
user = db.get_user_by_email("alice@example.com")
print(f"通过邮箱查询用户: {user}")

# 获取活跃用户
active_users = db.get_active_users()
print(f"活跃用户: {[u['name'] for u in active_users]}")

print("\n[类型注解的优势]")
print("  ✅ IDE 自动补全更准确")
print("  ✅ 静态类型检查发现错误")
print("  ✅ 代码可读性更高")
print("  ✅ 重构更安全")

print("\n💡 总结：类属性类型注解让类的数据结构一目了然")

