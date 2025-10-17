"""场景 9：矩阵计算中间结果"""
from functools import cached_property

class Matrix:
    def __init__(self, data):
        self.data = data
    
    @cached_property
    def transpose(self):
        print(f"  [转置]...")
        return list(zip(*self.data))
    
    @cached_property
    def determinant(self):
        print(f"  [行列式]...")
        return 42  # 简化示例

print("=" * 60)
m = Matrix([[1, 2], [3, 4]])
print(f"转置: {m.transpose}")
print(f"行列式: {m.determinant}")
print("💡 复杂计算只执行一次")

