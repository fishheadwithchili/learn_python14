"""
场景 2：单位和度量信息

应用：为数值类型附加单位信息，避免单位混淆导致的错误
"""

from typing import Annotated
from dataclasses import dataclass

# 定义单位类
class Unit:
    """单位信息"""
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name
    
    def __repr__(self):
        return f"{self.name}({self.symbol})"

# 定义常用单位
METER = Unit("m", "米")
KILOMETER = Unit("km", "千米")
SECOND = Unit("s", "秒")
HOUR = Unit("h", "小时")
METER_PER_SECOND = Unit("m/s", "米每秒")
KILOMETER_PER_HOUR = Unit("km/h", "千米每小时")
CELSIUS = Unit("°C", "摄氏度")
FAHRENHEIT = Unit("°F", "华氏度")
KILOGRAM = Unit("kg", "千克")
GRAM = Unit("g", "克")

# ✅ 使用 Annotated 附加单位信息

Meters = Annotated[float, METER]
Kilometers = Annotated[float, KILOMETER]
Seconds = Annotated[float, SECOND]
Hours = Annotated[float, HOUR]
MetersPerSecond = Annotated[float, METER_PER_SECOND]
KilometersPerHour = Annotated[float, KILOMETER_PER_HOUR]
Celsius = Annotated[float, CELSIUS]
Fahrenheit = Annotated[float, FAHRENHEIT]
Kilograms = Annotated[float, KILOGRAM]
Grams = Annotated[float, GRAM]

@dataclass
class Distance:
    """距离计算"""
    length: Meters
    
    def to_kilometers(self) -> Kilometers:
        return self.length / 1000

@dataclass
class Speed:
    """速度"""
    velocity: MetersPerSecond
    
    def to_kmh(self) -> KilometersPerHour:
        return self.velocity * 3.6

@dataclass
class Temperature:
    """温度"""
    value: Celsius
    
    def to_fahrenheit(self) -> Fahrenheit:
        return self.value * 9/5 + 32

@dataclass
class Weight:
    """重量"""
    value: Kilograms
    
    def to_grams(self) -> Grams:
        return self.value * 1000

def calculate_distance(speed: MetersPerSecond, time: Seconds) -> Meters:
    """计算距离 = 速度 × 时间"""
    return speed * time

def calculate_time(distance: Kilometers, speed: KilometersPerHour) -> Hours:
    """计算时间 = 距离 / 速度"""
    return distance / speed

print("=" * 60)
print("场景 2：单位和度量信息")
print("=" * 60)

# 示例 1：距离转换
print("\n[示例 1] 距离转换：\n")

dist = Distance(length=5000.0)  # 5000米
print(f"距离: {dist.length} 米")
print(f"转换为千米: {dist.to_kilometers()} 千米")

# 示例 2：速度转换
print("\n[示例 2] 速度转换：\n")

speed = Speed(velocity=25.0)  # 25 m/s
print(f"速度: {speed.velocity} m/s")
print(f"转换为 km/h: {speed.to_kmh():.2f} km/h")

# 示例 3：温度转换
print("\n[示例 3] 温度转换：\n")

temp = Temperature(value=25.0)  # 25°C
print(f"温度: {temp.value}°C")
print(f"转换为华氏度: {temp.to_fahrenheit():.2f}°F")

# 示例 4：重量转换
print("\n[示例 4] 重量转换：\n")

weight = Weight(value=2.5)  # 2.5 kg
print(f"重量: {weight.value} kg")
print(f"转换为克: {weight.to_grams()} g")

# 示例 5：物理计算（距离 = 速度 × 时间）
print("\n[示例 5] 物理计算（距离 = 速度 × 时间）：\n")

velocity: MetersPerSecond = 10.0  # 10 m/s
duration: Seconds = 60.0  # 60秒

distance = calculate_distance(velocity, duration)
print(f"速度: {velocity} m/s")
print(f"时间: {duration} 秒")
print(f"距离: {distance} 米")

# 示例 6：物理计算（时间 = 距离 / 速度）
print("\n[示例 6] 物理计算（时间 = 距离 / 速度）：\n")

trip_distance: Kilometers = 120.0  # 120 km
trip_speed: KilometersPerHour = 60.0  # 60 km/h

trip_time = calculate_time(trip_distance, trip_speed)
print(f"距离: {trip_distance} km")
print(f"速度: {trip_speed} km/h")
print(f"时间: {trip_time} 小时")

# 示例 7：复杂计算
print("\n[示例 7] 复杂计算（马拉松配速）：\n")

marathon_distance: Kilometers = 42.195  # 马拉松距离
finish_time_hours: Hours = 4.0  # 4小时完成

average_speed: KilometersPerHour = marathon_distance / finish_time_hours
print(f"马拉松距离: {marathon_distance} km")
print(f"完成时间: {finish_time_hours} 小时")
print(f"平均配速: {average_speed:.2f} km/h")

# 转换为 分钟/公里
minutes_per_km = 60 / average_speed
print(f"配速（分钟/公里）: {minutes_per_km:.2f} 分钟/公里")

print("\n[单位信息的优势]")
print("  ✅ 代码自文档化，单位一目了然")
print("  ✅ 减少单位混淆错误")
print("  ✅ IDE 可以显示单位信息")
print("  ✅ 便于单位转换验证")

print("\n💡 总结：Annotated 让物理量的单位信息明确，避免计算错误")

