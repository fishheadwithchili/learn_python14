"""
Walrus Operator 实战示例：Web 服务器日志分析

业务场景：
分析 Nginx 访问日志，找出：
1. 超长的请求 URL（可能是攻击）
2. 高频访问的 IP 地址
3. 响应时间超过阈值的请求

演示 walrus operator 如何避免重复计算和临时变量污染。

运行要求：Python >= 3.8
"""

import re
from collections import Counter

# 模拟的 Nginx 访问日志（实际场景会从文件读取）
LOG_LINES = [
    '192.168.1.100 - - [01/Jan/2024:10:23:45] "GET /api/users HTTP/1.1" 200 1234 0.123',
    '10.0.0.5 - - [01/Jan/2024:10:23:46] "POST /api/login HTTP/1.1" 200 567 0.056',
    '192.168.1.100 - - [01/Jan/2024:10:23:47] "GET /api/data?param=' + 'x' * 200 + ' HTTP/1.1" 200 8901 0.234',
    '172.16.0.20 - - [01/Jan/2024:10:23:48] "GET /health HTTP/1.1" 200 12 0.005',
    '192.168.1.100 - - [01/Jan/2024:10:23:49] "DELETE /api/resource/123 HTTP/1.1" 204 0 0.089',
    '10.0.0.5 - - [01/Jan/2024:10:23:50] "GET /dashboard HTTP/1.1" 200 4567 0.567',
]

# 日志解析正则
LOG_PATTERN = re.compile(
    r'(?P<ip>[\d.]+) .+ "(?P<method>\w+) (?P<url>\S+) HTTP.+" '
    r'(?P<status>\d+) (?P<size>\d+) (?P<time>[\d.]+)'
)

def analyze_logs(lines, url_threshold=100, time_threshold=0.5):
    """分析日志并返回统计结果"""
    
    ip_counter = Counter()
    suspicious_requests = []
    slow_requests = []
    
    for line in lines:
        # 场景 1: 避免重复正则匹配
        # 传统写法需要先匹配判断是否成功，再提取数据
        if (match := LOG_PATTERN.search(line)):
            ip = match.group('ip')
            url = match.group('url')
            response_time = float(match.group('time'))
            
            # 场景 2: 条件判断中复用计算结果
            # 避免对同一个 URL 调用两次 len()
            if (url_len := len(url)) > url_threshold:
                suspicious_requests.append({
                    'ip': ip,
                    'url': url[:50] + '...',  # 截断显示
                    'length': url_len
                })
            
            # 场景 3: 组合条件中避免重复查询
            ip_counter[ip] += 1
            
            # 响应时间检查
            if response_time > time_threshold:
                slow_requests.append({
                    'ip': ip,
                    'url': url[:30] + '...',
                    'time': response_time
                })
    
    return {
        'suspicious': suspicious_requests,
        'slow': slow_requests,
        'top_ips': ip_counter.most_common(3)
    }

def main():
    print("=" * 60)
    print("Web 服务器日志分析报告")
    print("=" * 60)
    
    results = analyze_logs(LOG_LINES)
    
    # 场景 4: 列表推导式中复用长度计算
    # 只对超长 URL 的请求进行格式化输出
    print("\n[可疑请求] URL 长度超过 100 字符:")
    if results['suspicious']:
        for req in results['suspicious']:
            print(f"  - IP: {req['ip']}, 长度: {req['length']}, URL: {req['url']}")
    else:
        print("  无")
    
    print("\n[慢请求] 响应时间超过 0.5 秒:")
    if results['slow']:
        for req in results['slow']:
            print(f"  - IP: {req['ip']}, 耗时: {req['time']:.3f}s, URL: {req['url']}")
    else:
        print("  无")
    
    print("\n[高频 IP] 访问次数 Top 3:")
    for ip, count in results['top_ips']:
        print(f"  - {ip}: {count} 次")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()

