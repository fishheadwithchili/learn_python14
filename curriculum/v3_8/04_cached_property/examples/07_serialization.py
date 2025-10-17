"""场景 7：对象序列化缓存"""
from functools import cached_property
import json

class APIResponse:
    def __init__(self, data):
        self.data = data
    
    @cached_property
    def json_str(self):
        print(f"  [序列化]...")
        return json.dumps(self.data, indent=2)
    
    @cached_property
    def size(self):
        return len(self.json_str)

print("=" * 60)
resp = APIResponse({"users": [{"id": i} for i in range(100)]})
print(f"大小: {resp.size} bytes")
print(f"再次: {resp.size}")
print("💡 避免重复序列化")

