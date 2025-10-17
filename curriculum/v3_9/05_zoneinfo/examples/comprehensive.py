"""
综合示例：全球电商平台的订单时间管理系统

场景：
一个全球化电商平台需要处理来自不同时区的订单、物流追踪和客服支持。
系统需要：
1. 记录订单时间（数据库使用 UTC）
2. 向用户显示本地时间
3. 协调跨时区的物流配送
4. 生成全球销售报表
5. 支持客服在不同时区查看订单信息
"""

try:
    from zoneinfo import ZoneInfo
except ImportError:
    print("需要 Python 3.9+ 或 pip install tzdata")
    exit(1)

from datetime import datetime, timedelta
from typing import Dict, List
import json

print("=" * 70)
print("综合示例：全球电商平台订单时间管理系统")
print("=" * 70)

# ========== 核心类定义 ==========

class Order:
    """订单类（时区感知）"""
    
    def __init__(self, order_id: str, user_timezone: str, items: List[str], 
                 total: float):
        self.order_id = order_id
        self.user_timezone = user_timezone
        self.items = items
        self.total = total
        # 订单时间始终用 UTC 存储
        self.created_at_utc = datetime.now(ZoneInfo("UTC"))
        self.status = "pending"
        self.shipped_at_utc = None
        self.delivered_at_utc = None
    
    def get_local_time(self, timezone_name: str = None) -> datetime:
        """获取指定时区的订单时间"""
        if timezone_name is None:
            timezone_name = self.user_timezone
        
        tz = ZoneInfo(timezone_name)
        return self.created_at_utc.astimezone(tz)
    
    def mark_shipped(self):
        """标记为已发货"""
        self.shipped_at_utc = datetime.now(ZoneInfo("UTC"))
        self.status = "shipped"
    
    def mark_delivered(self):
        """标记为已送达"""
        self.delivered_at_utc = datetime.now(ZoneInfo("UTC"))
        self.status = "delivered"
    
    def estimate_delivery(self) -> datetime:
        """预估送达时间（48小时后，用户时区）"""
        if self.shipped_at_utc:
            base_time = self.shipped_at_utc
        else:
            base_time = self.created_at_utc
        
        delivery_utc = base_time + timedelta(hours=48)
        return delivery_utc.astimezone(ZoneInfo(self.user_timezone))
    
    def to_user_dict(self) -> Dict:
        """生成用户视图（本地时间）"""
        local_time = self.get_local_time()
        
        result = {
            "order_id": self.order_id,
            "items": self.items,
            "total": f"${self.total:.2f}",
            "status": self.status,
            "ordered_at": local_time.strftime('%Y-%m-%d %H:%M %Z'),
        }
        
        if self.shipped_at_utc:
            shipped_local = self.shipped_at_utc.astimezone(
                ZoneInfo(self.user_timezone)
            )
            result["shipped_at"] = shipped_local.strftime('%Y-%m-%d %H:%M %Z')
            result["estimated_delivery"] = self.estimate_delivery().strftime(
                '%Y-%m-%d %H:%M %Z'
            )
        
        return result
    
    def to_admin_dict(self, admin_timezone: str = "UTC") -> Dict:
        """生成管理员视图（可选时区）"""
        tz = ZoneInfo(admin_timezone)
        
        result = {
            "order_id": self.order_id,
            "user_timezone": self.user_timezone,
            "status": self.status,
            "created_at": self.created_at_utc.astimezone(tz).strftime(
                '%Y-%m-%d %H:%M %Z'
            ),
            "total": f"${self.total:.2f}"
        }
        
        if self.shipped_at_utc:
            result["shipped_at"] = self.shipped_at_utc.astimezone(tz).strftime(
                '%Y-%m-%d %H:%M %Z'
            )
        
        return result


class OrderAnalytics:
    """订单分析系统"""
    
    def __init__(self, orders: List[Order]):
        self.orders = orders
    
    def get_hourly_stats(self, timezone_name: str) -> Dict[int, int]:
        """按小时统计订单数（指定时区）"""
        tz = ZoneInfo(timezone_name)
        hourly_counts = {hour: 0 for hour in range(24)}
        
        for order in self.orders:
            local_time = order.created_at_utc.astimezone(tz)
            hourly_counts[local_time.hour] += 1
        
        return hourly_counts
    
    def get_peak_hour(self, timezone_name: str) -> tuple:
        """获取峰值小时"""
        stats = self.get_hourly_stats(timezone_name)
        peak_hour = max(stats.items(), key=lambda x: x[1])
        return peak_hour
    
    def get_orders_by_timezone(self) -> Dict[str, int]:
        """按用户时区分组统计"""
        timezone_counts = {}
        for order in self.orders:
            tz = order.user_timezone
            timezone_counts[tz] = timezone_counts.get(tz, 0) + 1
        
        return timezone_counts


# ========== 场景演示 ==========

print("\n[场景 1] 创建全球订单\n")

# 模拟来自不同时区的订单（实际场景中时间会不同，这里用同一时刻简化）
base_utc = datetime(2023, 6, 15, 10, 0, tzinfo=ZoneInfo("UTC"))

orders = [
    Order("ORD-US-001", "America/New_York", ["Laptop", "Mouse"], 1299.99),
    Order("ORD-CN-002", "Asia/Shanghai", ["Phone", "Case"], 899.99),
    Order("ORD-UK-003", "Europe/London", ["Tablet", "Keyboard"], 649.99),
    Order("ORD-JP-004", "Asia/Tokyo", ["Camera", "Lens"], 1899.99),
    Order("ORD-AU-005", "Australia/Sydney", ["Watch", "Band"], 399.99),
]

# 手动设置创建时间以模拟不同时间的订单
for i, order in enumerate(orders):
    order.created_at_utc = base_utc + timedelta(hours=i)

print(f"创建了 {len(orders)} 个订单")
print()

# 显示用户视图
print("[场景 2] 用户查看订单（本地时间）\n")

for order in orders[:3]:
    user_view = order.to_user_dict()
    print(f"订单 {user_view['order_id']}:")
    print(f"  下单时间: {user_view['ordered_at']} (用户本地时间)")
    print(f"  商品: {', '.join(user_view['items'])}")
    print(f"  总计: {user_view['total']}")
    print(f"  状态: {user_view['status']}")
    print()

# 模拟发货
print("[场景 3] 订单发货和预估送达时间\n")

# 将前两个订单标记为已发货
for order in orders[:2]:
    order.mark_shipped()
    # 模拟发货时间
    order.shipped_at_utc = order.created_at_utc + timedelta(hours=2)

# 显示发货信息
for order in orders[:2]:
    user_view = order.to_user_dict()
    print(f"订单 {user_view['order_id']}:")
    print(f"  发货时间: {user_view['shipped_at']}")
    print(f"  预计送达: {user_view['estimated_delivery']}")
    print()

# 管理员视图（多时区支持）
print("[场景 4] 客服/管理员查看订单（可切换时区）\n")

# 纽约客服查看所有订单
admin_timezone = "America/New_York"
print(f"客服时区: {admin_timezone}\n")

print(f"{'订单号':<15} {'用户时区':<20} {'下单时间 (客服时区)':<25} {'状态':<10}")
print("-" * 75)

for order in orders:
    admin_view = order.to_admin_dict(admin_timezone)
    print(f"{admin_view['order_id']:<15} "
          f"{admin_view['user_timezone']:<20} "
          f"{admin_view['created_at']:<25} "
          f"{admin_view['status']:<10}")

# 数据分析
print("\n[场景 5] 全球销售数据分析\n")

analytics = OrderAnalytics(orders)

# 按时区统计订单
print("按用户时区统计：")
tz_stats = analytics.get_orders_by_timezone()
for tz, count in sorted(tz_stats.items(), key=lambda x: x[1], reverse=True):
    print(f"  {tz:<25}: {count} 个订单")

# 分析各时区的峰值时间
print("\n各时区的订单高峰时间：")
major_timezones = ["America/New_York", "Asia/Shanghai", "Europe/London"]

for tz in major_timezones:
    peak_hour, peak_count = analytics.get_peak_hour(tz)
    print(f"  {tz:<25}: {peak_hour:02d}:00 ({peak_count} 订单)")

# API 响应（JSON 格式，ISO 8601 时间）
print("\n[场景 6] API 响应示例（ISO 8601 格式）\n")

def create_api_response(order: Order) -> Dict:
    """生成 API 响应"""
    return {
        "order_id": order.order_id,
        "created_at": order.created_at_utc.isoformat(),  # ISO 8601
        "user_timezone": order.user_timezone,
        "status": order.status,
        "total": order.total
    }

# 生成第一个订单的 API 响应
api_response = create_api_response(orders[0])
print("GET /api/orders/ORD-US-001")
print(json.dumps(api_response, indent=2))

# 客户端解析
print("\n客户端解析时间戳：")
timestamp_str = api_response["created_at"]
dt_utc = datetime.fromisoformat(timestamp_str)
user_tz = ZoneInfo(api_response["user_timezone"])
dt_local = dt_utc.astimezone(user_tz)

print(f"  服务器返回 (UTC): {timestamp_str}")
print(f"  用户本地时间: {dt_local.strftime('%Y-%m-%d %H:%M %Z')}")

# 跨时区团队协作
print("\n[场景 7] 全球团队会议时间协调\n")

# 找一个适合所有区域的会议时间
meeting_base = datetime(2023, 6, 16, 14, 0, tzinfo=ZoneInfo("UTC"))

print("全球团队会议时间协调：\n")
print(f"{'地区':<20} {'本地时间':<25} {'适合开会':<10}")
print("-" * 60)

team_timezones = {
    "美国纽约": "America/New_York",
    "中国上海": "Asia/Shanghai",
    "英国伦敦": "Europe/London",
    "日本东京": "Asia/Tokyo"
}

for location, tz_name in team_timezones.items():
    local_time = meeting_base.astimezone(ZoneInfo(tz_name))
    hour = local_time.hour
    suitable = "✅" if 9 <= hour <= 18 else "❌"
    
    print(f"{location:<20} "
          f"{local_time.strftime('%Y-%m-%d %H:%M %Z'):<25} "
          f"{suitable:<10}")

# 总结
print("\n" + "=" * 70)
print("💡 系统总结")
print("=" * 70)
print("""
1. 数据库存储：始终使用 UTC 时间
2. 用户显示：转换为用户本地时区
3. API 通信：使用 ISO 8601 格式（包含时区信息）
4. 管理员工具：支持切换时区查看
5. 数据分析：统一转 UTC 分析，按需转本地时区展示
6. 团队协作：自动协调多时区会议时间

zoneinfo 的优势：
✓ 标准库支持，无需第三方依赖
✓ API 简洁，易于使用
✓ 自动处理夏令时
✓ 性能优秀
✓ 与 datetime 完美集成
""")

