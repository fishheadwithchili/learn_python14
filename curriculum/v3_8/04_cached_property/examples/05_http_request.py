"""场景 5：Web 请求对象派生属性"""
from functools import cached_property
import json

class Request:
    def __init__(self, body):
        self.body = body
    
    @cached_property
    def json_data(self):
        print(f"  [解析JSON]...")
        return json.loads(self.body)
    
    @cached_property
    def user_id(self):
        return self.json_data.get('user_id')

print("=" * 60)
req = Request('{"user_id": 123, "action": "login"}')
print(f"User ID: {req.user_id}")
print(f"Data: {req.json_data}")
print(f"再次: {req.user_id}")
print("💡 JSON 只解析一次")

