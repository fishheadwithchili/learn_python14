"""
场景 7：电商订单时间

应用：显示用户本地时区的订单时间，提升用户体验
"""

try:
    from zoneinfo import ZoneInfo
except ImportError:
    print("需要 Python 3.9+ 或 pip install tzdata")
    exit(1)

from datetime import datetime, timedelta

print("=" * 60)
print("场景 7：电商订单时间")
print("=" * 60)

# 示例订单数据（数据库存储 UTC）
orders_db = [
    {
        "order_id": "ORD001",
        "user": "alice",
        "user_timezone": "Asia/Shanghai",
        "created_at": datetime(2023, 6, 15, 2, 30, tzinfo=ZoneInfo("UTC")),
        "status": "已发货"
    },
    {
        "order_id": "ORD002",
        "user": "bob",
        "user_timezone": "America/Los_Angeles",
        "created_at": datetime(2023, 6, 15, 8, 15, tzinfo=ZoneInfo("UTC")),
        "status": "处理中"
    },
    {
        "order_id": "ORD003",
        "user": "charlie",
        "user_timezone": "Europe/Paris",
        "created_at": datetime(2023, 6, 15, 12, 45, tzinfo=ZoneInfo("UTC")),
        "status": "已完成"
    }
]

# ❌ 传统方式：直接显示 UTC 时间（用户体验差）
print("\n[传统方式] 显示 UTC 时间（用户难以理解）：\n")

for order in orders_db:
    print(f"订单 {order['order_id']} ({order['user']}):")
    print(f"  下单时间: {order['created_at'].strftime('%Y-%m-%d %H:%M %Z')}")
    print(f"  状态: {order['status']}")
    print()

# ✅ 使用 zoneinfo：转换为用户本地时区
print("[使用 zoneinfo] 显示用户本地时间：\n")

for order in orders_db:
    # 转换为用户时区
    user_tz = ZoneInfo(order['user_timezone'])
    local_time = order['created_at'].astimezone(user_tz)
    
    print(f"订单 {order['order_id']} ({order['user']}):")
    print(f"  下单时间: {local_time.strftime('%Y-%m-%d %H:%M %Z')} (本地时间)")
    print(f"  状态: {order['status']}")
    print()

# 示例 2：相对时间显示（"2小时前"）
print("[示例 2] 相对时间显示：\n")

def format_relative_time(order_time, user_timezone):
    """格式化为相对时间（如"2小时前"）"""
    # 转换为用户时区
    user_tz = ZoneInfo(user_timezone)
    local_time = order_time.astimezone(user_tz)
    now_local = datetime.now(user_tz)
    
    # 计算时间差
    delta = now_local - local_time
    
    if delta < timedelta(minutes=1):
        return "刚刚"
    elif delta < timedelta(hours=1):
        minutes = int(delta.total_seconds() / 60)
        return f"{minutes} 分钟前"
    elif delta < timedelta(days=1):
        hours = int(delta.total_seconds() / 3600)
        return f"{hours} 小时前"
    elif delta < timedelta(days=7):
        days = delta.days
        return f"{days} 天前"
    else:
        return local_time.strftime('%Y-%m-%d %H:%M')

# 模拟当前时间为 2023-06-15 14:00 UTC
mock_now = datetime(2023, 6, 15, 14, 0, tzinfo=ZoneInfo("UTC"))

for order in orders_db:
    user_tz = ZoneInfo(order['user_timezone'])
    local_time = order['created_at'].astimezone(user_tz)
    
    # 手动计算相对时间
    delta = mock_now - order['created_at']
    hours = int(delta.total_seconds() / 3600)
    
    print(f"订单 {order['order_id']} ({order['user']}):")
    print(f"  下单时间: {local_time.strftime('%m-%d %H:%M')} ({hours}小时前)")
    print(f"  状态: {order['status']}")
    print()

# 示例 3：预计送达时间
print("[示例 3] 预计送达时间（用户时区）：\n")

def calculate_delivery_time(order_time, user_timezone, delivery_hours=48):
    """计算预计送达时间"""
    user_tz = ZoneInfo(user_timezone)
    order_local = order_time.astimezone(user_tz)
    delivery_time = order_local + timedelta(hours=delivery_hours)
    
    return delivery_time

for order in orders_db:
    if order['status'] == '已发货':
        delivery_time = calculate_delivery_time(
            order['created_at'], 
            order['user_timezone']
        )
        
        print(f"订单 {order['order_id']} ({order['user']}):")
        print(f"  预计送达: {delivery_time.strftime('%Y-%m-%d %H:%M %Z')}")
        print()

# 示例 4：订单列表排序（按用户本地时间）
print("[示例 4] 按本地时间排序订单：\n")

# 为每个订单添加本地时间
for order in orders_db:
    user_tz = ZoneInfo(order['user_timezone'])
    order['local_time'] = order['created_at'].astimezone(user_tz)

# 按 UTC 时间排序
sorted_orders = sorted(orders_db, key=lambda x: x['created_at'])

print("按下单时间排序（UTC）：")
for order in sorted_orders:
    print(f"  {order['order_id']}: {order['local_time'].strftime('%m-%d %H:%M')} "
          f"({order['user_timezone'].split('/')[-1]})")

# 示例 5：多时区客服显示
print("\n[示例 5] 客服面板（查看所有订单）：\n")

print(f"{'订单号':<10} {'用户':^10} {'UTC时间':<20} {'用户本地时间':<20} {'状态':^10}")
print("-" * 80)

for order in orders_db:
    user_tz = ZoneInfo(order['user_timezone'])
    local_time = order['created_at'].astimezone(user_tz)
    
    print(f"{order['order_id']:<10} "
          f"{order['user']:^10} "
          f"{order['created_at'].strftime('%m-%d %H:%M %Z'):<20} "
          f"{local_time.strftime('%m-%d %H:%M %Z'):<20} "
          f"{order['status']:^10}")

print("\n💡 总结：数据库存UTC，显示时转用户时区，提升用户体验")

