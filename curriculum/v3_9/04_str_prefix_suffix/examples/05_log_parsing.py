"""
场景 5：日志解析

应用：从日志行中提取时间戳、级别、消息等信息
"""

from datetime import datetime

# 测试数据
log_lines = [
    "[2023-06-15 10:30:00] [ERROR] Database connection failed",
    "[2023-06-15 10:30:01] [WARNING] Retry attempt 1",
    "[2023-06-15 10:30:05] [INFO] Connection established",
    "[2023-06-15 10:30:10] [DEBUG] Query executed successfully"
]

apache_logs = [
    '192.168.1.100 - - [15/Jun/2023:10:30:00 +0800] "GET /index.html HTTP/1.1" 200 1234',
    '192.168.1.101 - - [15/Jun/2023:10:30:05 +0800] "POST /api/users HTTP/1.1" 201 567',
    '192.168.1.102 - - [15/Jun/2023:10:30:10 +0800] "GET /static/style.css HTTP/1.1" 304 0'
]

print("=" * 60)
print("场景 5：日志解析")
print("=" * 60)

# 示例 1：解析结构化日志
print("\n[示例 1] 解析结构化日志：\n")

def parse_log_line(line):
    """解析日志行"""
    # 提取时间戳
    if line.startswith("["):
        rest = line.removeprefix("[")
        timestamp_end = rest.find("]")
        timestamp = rest[:timestamp_end]
        rest = rest[timestamp_end:].removeprefix("] ")
    else:
        timestamp = None
        rest = line
    
    # 提取日志级别
    level = None
    if rest.startswith("["):
        rest = rest.removeprefix("[")
        level_end = rest.find("]")
        level = rest[:level_end]
        rest = rest[level_end:].removeprefix("] ")
    
    # 剩余部分是消息
    message = rest
    
    return {
        "timestamp": timestamp,
        "level": level,
        "message": message
    }

print("解析结果:")
for log in log_lines:
    parsed = parse_log_line(log)
    print(f"  原始: {log}")
    print(f"    时间: {parsed['timestamp']}")
    print(f"    级别: {parsed['level']}")
    print(f"    消息: {parsed['message']}")
    print()

# 示例 2：按日志级别过滤
print("[示例 2] 按日志级别过滤：\n")

def filter_by_level(logs, level):
    """过滤特定级别的日志"""
    filtered = []
    for log in logs:
        parsed = parse_log_line(log)
        if parsed['level'] == level:
            filtered.append(parsed)
    return filtered

errors = filter_by_level(log_lines, "ERROR")
print(f"ERROR 级别日志 ({len(errors)} 条):")
for log in errors:
    print(f"  [{log['timestamp']}] {log['message']}")

warnings = filter_by_level(log_lines, "WARNING")
print(f"\nWARNING 级别日志 ({len(warnings)} 条):")
for log in warnings:
    print(f"  [{log['timestamp']}] {log['message']}")

# 示例 3：移除日志前缀
print("\n[示例 3] 提取纯文本消息：\n")

for log in log_lines:
    # 移除所有前缀，只保留消息
    message = log
    
    # 移除时间戳
    if "[" in message:
        first_close = message.find("]")
        message = message[first_close+1:].strip()
    
    # 移除级别标签
    if message.startswith("["):
        first_close = message.find("]")
        message = message[first_close+1:].strip()
    
    print(f"  {log}")
    print(f"  → {message}")

# 示例 4：Apache 日志解析
print("\n[示例 4] Apache 访问日志解析：\n")

def parse_apache_log(line):
    """解析 Apache 访问日志"""
    parts = line.split(" ")
    
    ip = parts[0]
    
    # 提取时间戳（在方括号中）
    timestamp_start = line.find("[")
    timestamp_end = line.find("]")
    timestamp = line[timestamp_start+1:timestamp_end]
    
    # 提取请求（在引号中）
    request_start = line.find('"')
    request_end = line.find('"', request_start + 1)
    request = line[request_start+1:request_end]
    
    # 提取状态码和大小
    after_request = line[request_end+1:].strip().split()
    status = after_request[0]
    size = after_request[1]
    
    return {
        "ip": ip,
        "timestamp": timestamp,
        "request": request,
        "status": status,
        "size": size
    }

print("解析 Apache 日志:")
for log in apache_logs:
    parsed = parse_apache_log(log)
    print(f"\n  IP: {parsed['ip']}")
    print(f"  时间: {parsed['timestamp']}")
    print(f"  请求: {parsed['request']}")
    print(f"  状态: {parsed['status']}")
    print(f"  大小: {parsed['size']} bytes")

# 示例 5：日志统计
print("\n[示例 5] 日志级别统计：\n")

level_counts = {}
for log in log_lines:
    parsed = parse_log_line(log)
    level = parsed['level']
    level_counts[level] = level_counts.get(level, 0) + 1

print("日志级别分布:")
for level, count in sorted(level_counts.items()):
    print(f"  {level}: {count} 条")

# 示例 6：时间范围过滤
print("\n[示例 6] 时间范围过滤：\n")

def filter_by_time(logs, start_time, end_time):
    """过滤时间范围内的日志"""
    filtered = []
    for log in logs:
        parsed = parse_log_line(log)
        if parsed['timestamp']:
            log_time = parsed['timestamp']
            if start_time <= log_time <= end_time:
                filtered.append(parsed)
    return filtered

filtered_logs = filter_by_time(
    log_lines,
    "2023-06-15 10:30:00",
    "2023-06-15 10:30:05"
)

print(f"时间范围内的日志 ({len(filtered_logs)} 条):")
for log in filtered_logs:
    print(f"  [{log['timestamp']}] [{log['level']}] {log['message']}")

print("\n💡 总结：removeprefix/removesuffix 简化日志解析，提取关键信息")

