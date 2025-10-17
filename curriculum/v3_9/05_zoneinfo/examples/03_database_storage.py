"""
场景 3：数据库存储

应用：数据库存储使用 UTC，显示时使用用户时区
"""

try:
    from zoneinfo import ZoneInfo
except ImportError:
    print("需要 Python 3.9+ 或 pip install tzdata")
    exit(1)

from datetime import datetime

print("=" * 60)
print("场景 3：数据库存储（UTC）与本地显示")
print("=" * 60)

# 模拟数据库操作
class Article:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        # 数据库存储：始终使用 UTC
        self.created_at = datetime.now(ZoneInfo("UTC"))
        self.updated_at = datetime.now(ZoneInfo("UTC"))
    
    def display_time(self, user_timezone):
        """根据用户时区显示时间"""
        created_local = self.created_at.astimezone(ZoneInfo(user_timezone))
        return created_local.strftime('%Y-%m-%d %H:%M:%S %Z')

# 示例 1：创建文章
print("\n[示例 1] 创建文章（UTC 存储）：\n")

article = Article("Python 3.9 新特性", "介绍 zoneinfo...")
print(f"标题: {article.title}")
print(f"创建时间 (UTC): {article.created_at.strftime('%Y-%m-%d %H:%M:%S %Z')}")

# 示例 2：不同用户查看
print("\n[示例 2] 不同地区用户查看：\n")

users = [
    ("Asia/Shanghai", "中国用户"),
    ("America/New_York", "美国用户"),
    ("Europe/London", "英国用户")
]

for tz, user_type in users:
    display_time = article.display_time(tz)
    print(f"{user_type:12s}: {display_time}")

# 示例 3：时间戳存储
print("\n[示例 3] 时间戳与时区转换：\n")

# 存储为时间戳
timestamp = article.created_at.timestamp()
print(f"时间戳: {timestamp}")

# 从时间戳恢复（UTC）
restored_utc = datetime.fromtimestamp(timestamp, tz=ZoneInfo("UTC"))
print(f"恢复 UTC: {restored_utc}")

# 转换为本地时间
restored_local = restored_utc.astimezone(ZoneInfo("Asia/Shanghai"))
print(f"本地时间: {restored_local}")

print("\n💡 总结：数据库存 UTC，显示时转用户时区，避免混淆")

