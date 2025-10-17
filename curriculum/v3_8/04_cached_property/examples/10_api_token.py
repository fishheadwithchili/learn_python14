"""场景 10：API 客户端认证令牌"""
from functools import cached_property
import time

class APIClient:
    @cached_property
    def auth_token(self):
        print(f"  [获取令牌]...")
        time.sleep(0.1)
        return "token_abc123"
    
    def request(self, endpoint):
        return f"GET {endpoint} (Token: {self.auth_token})"

print("=" * 60)
client = APIClient()
print(client.request("/users"))
print(client.request("/posts"))
print("💡 令牌复用，减少认证请求")

# 清除缓存
del client.__dict__['auth_token']
print("\n清除后重新获取:")
print(client.request("/data"))

