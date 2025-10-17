"""
场景 7：数据流处理中的状态追踪

应用：在生成器或管道中追踪中间状态，避免多次计算
"""

import time

class DataStream:
    """模拟数据流（如网络数据、传感器数据）"""
    
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def read(self, size):
        """读取指定大小的数据块"""
        if self.index >= len(self.data):
            return b''
        
        chunk = self.data[self.index:self.index + size]
        self.index += size
        
        print(f"  [读取] {len(chunk)} 字节")
        time.sleep(0.05)  # 模拟 I/O 延迟
        
        return chunk

# 模拟二进制数据流
binary_data = b'Hello World! This is a stream of binary data for processing.'

print("=" * 60)
print("数据流处理")
print("=" * 60)

# ❌ 传统方式 - 需要多次调用 len()
print("\n[传统方式] 重复调用 len()：\n")

stream1 = DataStream(binary_data)
chunk_size = 10
chunks_old = []

chunk = stream1.read(chunk_size)
while len(chunk) > 0:
    chunks_old.append({
        'data': chunk.decode('utf-8', errors='ignore'),
        'size': len(chunk)  # 又计算一次！
    })
    chunk = stream1.read(chunk_size)

for i, chunk_info in enumerate(chunks_old, 1):
    print(f"  块 {i}: {chunk_info['size']} 字节 - '{chunk_info['data']}'")

# ✅ 使用 walrus operator - 读取和大小检查合并
print("\n[Walrus Operator] 合并读取和检查：\n")

stream2 = DataStream(binary_data)
chunks_new = []

while (chunk := stream2.read(chunk_size)) and (size := len(chunk)) > 0:
    chunks_new.append({
        'data': chunk.decode('utf-8', errors='ignore'),
        'size': size  # 直接使用已计算的值
    })

for i, chunk_info in enumerate(chunks_new, 1):
    print(f"  块 {i}: {chunk_info['size']} 字节 - '{chunk_info['data']}'")

print("\n" + "=" * 60)
print("生成器中的应用")
print("=" * 60)

def process_stream(stream, chunk_size=10):
    """流式处理数据生成器"""
    while (batch := stream.read(chunk_size)) and (size := len(batch)) > 0:
        # 同时yield数据和大小
        yield {
            'chunk': batch,
            'size': size,
            'processed': batch.decode('utf-8', errors='ignore').upper()
        }

print("\n使用生成器处理流：\n")

stream3 = DataStream(binary_data)
for i, result in enumerate(process_stream(stream3, 15), 1):
    print(f"  处理块 {i}:")
    print(f"    原始大小: {result['size']} 字节")
    print(f"    处理结果: {result['processed'][:30]}...")

print("\n💡 总结：流处理中避免重复计算，提升处理效率")

