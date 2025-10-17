"""
场景 4：航班时刻表

应用：处理跨时区的航班起飞和降落时间
"""

try:
    from zoneinfo import ZoneInfo
except ImportError:
    print("需要 Python 3.9+ 或 pip install tzdata")
    exit(1)

from datetime import datetime, timedelta

print("=" * 60)
print("场景 4：航班时刻表")
print("=" * 60)

class Flight:
    def __init__(self, flight_no, departure_airport, arrival_airport, 
                 departure_time, flight_duration):
        self.flight_no = flight_no
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.departure_time = departure_time
        self.flight_duration = flight_duration
        self.arrival_time = departure_time + flight_duration
    
    def display_schedule(self):
        print(f"\n航班 {self.flight_no}:")
        print(f"  起飞: {self.departure_airport} "
              f"{self.departure_time.strftime('%Y-%m-%d %H:%M %Z')}")
        print(f"  降落: {self.arrival_airport} "
              f"{self.arrival_time.strftime('%Y-%m-%d %H:%M %Z')}")
        print(f"  飞行时长: {self.flight_duration}")

# 北京到纽约
departure_beijing = datetime(2023, 6, 15, 10, 0, tzinfo=ZoneInfo("Asia/Shanghai"))
flight_duration = timedelta(hours=14)

flight1 = Flight(
    "CA981",
    "北京首都机场 (PEK)",
    "纽约肯尼迪机场 (JFK)",
    departure_beijing,
    flight_duration
)

# 显示时刻表（起飞地时间）
flight1.display_schedule()

# 转换为降落地时区
arrival_newyork_local = flight1.arrival_time.astimezone(ZoneInfo("America/New_York"))
print(f"\n降落地当地时间: {arrival_newyork_local.strftime('%Y-%m-%d %H:%M %Z')}")

print("\n💡 总结：zoneinfo 准确处理跨时区航班时间")

