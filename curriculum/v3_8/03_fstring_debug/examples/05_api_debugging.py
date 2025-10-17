"""
场景 5：API 响应调试

应用：调试 Web API 时记录请求和响应细节
"""

print("=" * 60)
print("API 调试")
print("=" * 60)

# 模拟 API 调用
url = "https://api.example.com/users/123"
method = "GET"
headers = {"Authorization": "Bearer token123"}
params = {"include": "profile,posts"}

print("\n请求信息：\n")
print(f"{method=}")
print(f"{url=}")
print(f"{headers=}")
print(f"{params=}")

# 模拟响应
status_code = 200
response_time = 0.234
content_length = 1548

print("\n响应信息：\n")
print(f"{status_code=}")
print(f"{response_time=:.3f}s")
print(f"{content_length=} bytes")

# 响应数据
response_data = {
    "id": 123,
    "name": "Alice",
    "posts_count": 42
}
print(f"{response_data=}")

print("\n💡 总结：API 调试信息完整，快速定位问题")

