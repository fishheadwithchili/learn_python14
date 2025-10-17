"""
场景 2：时区转换

应用：在不同时区之间转换时间
"""

try:
    from zoneinfo import ZoneInfo
except ImportError:
    print("需要 Python 3.9+ 或 pip install tzdata")
    exit(1)

from datetime import datetime

print("=" * 60)
print("场景 2：时区转换")
print("=" * 60)

# 示例 1：基本时区转换
print("\n[示例 1] 基本时区转换：\n")

# 创建上海时间
shanghai_time = datetime(2023, 6, 15, 14, 30, tzinfo=ZoneInfo("Asia/Shanghai"))
print(f"上海时间: {shanghai_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")

# 转换为纽约时间
newyork_time = shanghai_time.astimezone(ZoneInfo("America/New_York"))
print(f"纽约时间: {newyork_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")

# 转换为伦敦时间
london_time = shanghai_time.astimezone(ZoneInfo("Europe/London"))
print(f"伦敦时间: {london_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")

# 示例 2：全球会议时间
print("\n[示例 2] 全球会议时间协调：\n")

meeting_beijing = datetime(2023, 6, 15, 14, 0, tzinfo=ZoneInfo("Asia/Shanghai"))
print(f"会议时间设定（北京）: {meeting_beijing.strftime('%H:%M %Z')}")

cities = [
    ("America/New_York", "纽约"),
    ("Europe/London", "伦敦"),
    ("Asia/Tokyo", "东京"),
    ("Australia/Sydney", "悉尼")
]

print("\n各地相应时间:")
for tz_name, city in cities:
    local_time = meeting_beijing.astimezone(ZoneInfo(tz_name))
    print(f"  {city:8s}: {local_time.strftime('%Y-%m-%d %H:%M %Z')}")

# 示例 3：UTC 作为中间格式
print("\n[示例 3] 使用 UTC 作为中间格式：\n")

# 步骤1：本地时间转 UTC
local_time = datetime(2023, 6, 15, 10, 0, tzinfo=ZoneInfo("Asia/Shanghai"))
utc_time = local_time.astimezone(ZoneInfo("UTC"))

print(f"本地时间: {local_time.strftime('%H:%M %Z')}")
print(f"UTC 时间: {utc_time.strftime('%H:%M %Z')}")

# 步骤2：UTC 转其他时区
target_time = utc_time.astimezone(ZoneInfo("America/Los_Angeles"))
print(f"洛杉矶时间: {target_time.strftime('%H:%M %Z')}")

print("\n💡 总结：astimezone() 方法可轻松实现时区转换")

