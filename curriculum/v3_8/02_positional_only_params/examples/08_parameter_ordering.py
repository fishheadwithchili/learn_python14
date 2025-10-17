"""
场景 8: 多态函数参数重载模拟

应用：根据位置参数个数决定行为（类似函数重载）
"""

from typing import Union, Optional
from datetime import datetime, timedelta

print("=" * 60)
print("参数重载模拟")
print("=" * 60)

def schedule_task(task_id, /, when=None, delay=None, repeat=None):
    """
    安排任务
    
    参数:
        task_id: 任务 ID（仅位置）
        when: 指定时间
        delay: 延迟秒数
        repeat: 重复间隔
    """
    if when is not None:
        scheduled_time = when
        method = "指定时间"
    elif delay is not None:
        scheduled_time = datetime.now() + timedelta(seconds=delay)
        method = "延迟执行"
    else:
        scheduled_time = datetime.now()
        method = "立即执行"
    
    print(f"  任务 {task_id}: {method}")
    print(f"  计划时间: {scheduled_time.strftime('%H:%M:%S')}")
    
    if repeat:
        print(f"  重复间隔: 每 {repeat} 秒")

print("\n不同的调用方式：\n")

schedule_task(1, when=datetime.now() + timedelta(hours=1))
print()

schedule_task(2, delay=300)
print()

schedule_task(3, repeat=60)

print("\n" + "=" * 60)
print("创建对象的多种方式")
print("=" * 60)

class Point:
    def __init__(self, x, y=None, /):
        """
        创建点对象
        
        支持：
        - Point((3, 4))  # 元组
        - Point(3, 4)    # 两个数字
        """
        if y is None:
            # 假设 x 是元组
            if isinstance(x, tuple) and len(x) == 2:
                self.x, self.y = x
            else:
                raise ValueError("需要元组 (x, y) 或两个数字")
        else:
            self.x, self.y = x, y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

print("\n创建点对象：\n")

p1 = Point(3, 4)
print(f"  Point(3, 4) = {p1}")

p2 = Point((5, 6))
print(f"  Point((5, 6)) = {p2}")

print("\n💡 总结：仅位置参数让参数语义更明确，支持重载风格的 API")

