"""
场景 8：定时任务调度

应用：在特定时区执行定时任务，确保任务在正确的本地时间运行
"""

try:
    from zoneinfo import ZoneInfo
except ImportError:
    print("需要 Python 3.9+ 或 pip install tzdata")
    exit(1)

from datetime import datetime, time, timedelta

print("=" * 60)
print("场景 8：定时任务调度")
print("=" * 60)

# 示例 1：指定时区的定时任务
print("\n[示例 1] 在特定时区执行任务：\n")

# 定义任务：每天上午 9:00（东京时间）发送报告
task_configs = [
    {
        "name": "东京市场日报",
        "timezone": "Asia/Tokyo",
        "schedule_time": time(9, 0),
        "description": "每天东京时间 09:00 发送"
    },
    {
        "name": "纽约市场周报",
        "timezone": "America/New_York",
        "schedule_time": time(17, 0),
        "description": "每周五纽约时间 17:00 发送"
    },
    {
        "name": "欧洲数据备份",
        "timezone": "Europe/London",
        "schedule_time": time(2, 0),
        "description": "每天伦敦时间 02:00 执行"
    }
]

# 计算下次执行时间
def calculate_next_run(schedule_time, timezone_name):
    """计算任务下次执行的时间"""
    tz = ZoneInfo(timezone_name)
    now_tz = datetime.now(tz)
    
    # 构造今天的执行时间
    today_run = datetime.combine(now_tz.date(), schedule_time, tzinfo=tz)
    
    # 如果已经过了今天的执行时间，调度到明天
    if now_tz > today_run:
        next_run = today_run + timedelta(days=1)
    else:
        next_run = today_run
    
    return next_run

# 当前时间
current_utc = datetime.now(ZoneInfo("UTC"))
print(f"当前 UTC 时间: {current_utc.strftime('%Y-%m-%d %H:%M %Z')}\n")

for task in task_configs:
    next_run = calculate_next_run(task['schedule_time'], task['timezone'])
    next_run_utc = next_run.astimezone(ZoneInfo("UTC"))
    
    # 计算距离下次执行的时间
    time_until = next_run_utc - current_utc
    hours_until = time_until.total_seconds() / 3600
    
    print(f"任务: {task['name']}")
    print(f"  时区: {task['timezone']}")
    print(f"  本地时间: {next_run.strftime('%Y-%m-%d %H:%M %Z')}")
    print(f"  UTC 时间: {next_run_utc.strftime('%Y-%m-%d %H:%M %Z')}")
    print(f"  距离执行: {hours_until:.1f} 小时")
    print()

# 示例 2：考虑夏令时的任务调度
print("[示例 2] 夏令时自动处理：\n")

# 纽约在 3 月和 11 月会切换夏令时
# zoneinfo 自动处理时区偏移变化

dates = [
    datetime(2023, 3, 10, 12, 0),   # 夏令时开始前
    datetime(2023, 3, 15, 12, 0),   # 夏令时开始后
    datetime(2023, 11, 3, 12, 0),   # 夏令时结束前
    datetime(2023, 11, 7, 12, 0)    # 夏令时结束后
]

ny_tz = ZoneInfo("America/New_York")

for date in dates:
    # 创建纽约时间
    ny_time = date.replace(tzinfo=ny_tz)
    
    # 转换为 UTC
    utc_time = ny_time.astimezone(ZoneInfo("UTC"))
    
    # 获取 UTC 偏移
    offset = ny_time.strftime('%z')
    
    print(f"{date.strftime('%Y-%m-%d')}:")
    print(f"  纽约: {ny_time.strftime('%H:%M %Z')} (UTC{offset})")
    print(f"  UTC:  {utc_time.strftime('%H:%M %Z')}")
    print()

# 示例 3：多时区任务协调
print("[示例 3] 协调多时区团队的会议：\n")

# 需要找到一个所有人都方便的时间
# 要求：上海 9:00-18:00，纽约 9:00-18:00，伦敦 9:00-18:00

def find_meeting_time():
    """找到适合所有时区的会议时间"""
    # 从上海时间 14:00 开始尝试（通常是合适的时间）
    shanghai_time = datetime(2023, 6, 15, 14, 0, tzinfo=ZoneInfo("Asia/Shanghai"))
    
    # 转换到其他时区
    newyork_time = shanghai_time.astimezone(ZoneInfo("America/New_York"))
    london_time = shanghai_time.astimezone(ZoneInfo("Europe/London"))
    
    return {
        "上海": shanghai_time,
        "纽约": newyork_time,
        "伦敦": london_time
    }

meeting_times = find_meeting_time()

print("全球团队会议时间：")
for city, dt in meeting_times.items():
    print(f"  {city:6s}: {dt.strftime('%H:%M %Z')}")

# 检查是否在工作时间内
print("\n工作时间检查：")
for city, dt in meeting_times.items():
    hour = dt.hour
    in_office_hours = 9 <= hour < 18
    status = "✅" if in_office_hours else "❌"
    print(f"  {city:6s}: {status} ({dt.strftime('%H:%M')})")

# 示例 4：Cron 风格的时区调度
print("\n[示例 4] 定时任务调度器示例：\n")

class TimezoneScheduler:
    """简单的时区感知任务调度器"""
    
    def __init__(self, timezone_name):
        self.timezone = ZoneInfo(timezone_name)
        self.tasks = []
    
    def schedule(self, name, hour, minute):
        """调度一个任务"""
        self.tasks.append({
            'name': name,
            'time': time(hour, minute)
        })
    
    def get_next_runs(self):
        """获取所有任务的下次执行时间"""
        now = datetime.now(self.timezone)
        results = []
        
        for task in self.tasks:
            next_run = datetime.combine(now.date(), task['time'], tzinfo=self.timezone)
            if now > next_run:
                next_run += timedelta(days=1)
            
            results.append({
                'name': task['name'],
                'local_time': next_run,
                'utc_time': next_run.astimezone(ZoneInfo("UTC"))
            })
        
        return results

# 创建东京时区的调度器
scheduler = TimezoneScheduler("Asia/Tokyo")
scheduler.schedule("晨会", 9, 0)
scheduler.schedule("午餐提醒", 12, 0)
scheduler.schedule("日报生成", 18, 0)

print("东京办公室任务调度：\n")
for task in scheduler.get_next_runs():
    print(f"{task['name']:12s}:")
    print(f"  本地: {task['local_time'].strftime('%H:%M %Z')}")
    print(f"  UTC:  {task['utc_time'].strftime('%H:%M %Z')}")
    print()

print("💡 总结：使用 zoneinfo 确保定时任务在正确的本地时间执行")

