"""场景 6：图像处理派生数据"""
from functools import cached_property

class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @cached_property
    def aspect_ratio(self):
        return self.width / self.height
    
    @cached_property
    def is_landscape(self):
        return self.aspect_ratio > 1

print("=" * 60)
img = Image(1920, 1080)
print(f"宽高比: {img.aspect_ratio:.2f}")
print(f"横向: {img.is_landscape}")
print("💡 计算只执行一次")

