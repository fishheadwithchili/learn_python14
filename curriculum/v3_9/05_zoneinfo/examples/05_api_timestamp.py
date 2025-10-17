"""
场景 5：API 时间戳

应用：API 返回和接收带时区的时间戳
"""

try:
    from zoneinfo import ZoneInfo
except ImportError:
    print("需要 Python 3.9+ 或 pip install tzdata")
    exit(1)

from datetime import datetime
import json

print("=" * 60)
print("场景 5：API 时间戳")
print("=" * 60)

# API 响应示例
def create_api_response():
    """创建 API 响应（使用 UTC）"""
    return {
        "status": "success",
        "data": {
            "user_id": 123,
            "username": "alice"
        },
        "timestamp": datetime.now(ZoneInfo("UTC")).isoformat()
    }

# 生成响应
response = create_api_response()
print("\n[API 响应] JSON:")
print(json.dumps(response, indent=2))

# 解析 ISO 时间戳
timestamp_str = response["timestamp"]
dt_utc = datetime.fromisoformat(timestamp_str)
print(f"\n解析时间戳:")
print(f"  UTC: {dt_utc}")
print(f"  北京时间: {dt_utc.astimezone(ZoneInfo('Asia/Shanghai'))}")

print("\n💡 总结：API 使用 ISO 8601 格式 + UTC，客户端转本地时区")

