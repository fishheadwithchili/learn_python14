"""场景 4：数据集统计信息"""
from functools import cached_property

class Dataset:
    def __init__(self, data):
        self.data = data
    
    @cached_property
    def mean(self):
        return sum(self.data) / len(self.data)
    
    @cached_property
    def variance(self):
        m = self.mean
        return sum((x - m) ** 2 for x in self.data) / len(self.data)
    
    @cached_property
    def std_dev(self):
        return self.variance ** 0.5

print("=" * 60)
ds = Dataset([1, 2, 3, 4, 5] * 1000)
print(f"均值: {ds.mean:.2f}")
print(f"方差: {ds.variance:.2f}")
print(f"标准差: {ds.std_dev:.2f}")
print("💡 避免重复遍历大数据集")

