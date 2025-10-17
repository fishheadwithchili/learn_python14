# zoneinfo 示例代码

本目录包含 **zoneinfo（标准库时区支持）** 的 10 个独立场景示例和 1 个综合示例。

## 📋 示例列表

| 文件 | 场景 | 难度 | 核心知识点 |
|------|------|------|-----------|
| `01_basic_usage.py` | 基本用法 | ⭐ | ZoneInfo 创建、时区转换、naive vs aware |
| `02_timezone_conversion.py` | 跨时区转换 | ⭐⭐ | astimezone()、多时区处理 |
| `03_database_storage.py` | 数据库时间存储 | ⭐⭐ | UTC 存储、本地时区显示 |
| `04_flight_schedule.py` | 航班时刻表 | ⭐⭐⭐ | 起降时间、飞行时长、时区计算 |
| `05_api_timestamp.py` | API 时间戳 | ⭐⭐ | ISO 8601 格式、时间序列化 |
| `06_trading_time.py` | 金融交易时间 | ⭐⭐⭐ | 市场开盘时间、交易窗口检查 |
| `07_ecommerce_order.py` | 电商订单时间 | ⭐⭐⭐ | 用户本地时间、相对时间显示 |
| `08_scheduled_tasks.py` | 定时任务调度 | ⭐⭐⭐ | Cron 调度、夏令时处理 |
| `09_data_analysis.py` | 数据分析 | ⭐⭐⭐⭐ | 时间序列对齐、跨时区聚合 |
| `10_migration_guide.py` | 从 pytz 迁移 | ⭐⭐⭐ | pytz vs zoneinfo 对照、迁移实践 |
| `comprehensive.py` | 综合示例 | ⭐⭐⭐⭐ | 全球电商平台订单时间管理系统 |

## 🚀 快速开始

### 环境要求

- **Python 版本**: 3.9+
- **Windows 用户**: 需要安装 `tzdata` 包
  ```bash
  pip install tzdata
  ```

### 运行示例

```bash
# 进入示例目录
cd curriculum/v3_9/05_zoneinfo/examples

# 运行单个示例
python 01_basic_usage.py

# 运行综合示例
python comprehensive.py
```

## 📚 核心概念

### 1. ZoneInfo 基本使用

```python
from zoneinfo import ZoneInfo
from datetime import datetime

# 创建带时区的 datetime
dt = datetime(2023, 6, 15, 10, 30, tzinfo=ZoneInfo("Asia/Shanghai"))

# 获取当前时间（带时区）
now = datetime.now(ZoneInfo("Asia/Shanghai"))
```

### 2. 时区转换

```python
# 转换到其他时区
shanghai_time = datetime.now(ZoneInfo("Asia/Shanghai"))
newyork_time = shanghai_time.astimezone(ZoneInfo("America/New_York"))
```

### 3. naive vs aware datetime

```python
# naive datetime（无时区信息）
dt_naive = datetime(2023, 6, 15, 10, 30)

# aware datetime（有时区信息）
dt_aware = datetime(2023, 6, 15, 10, 30, tzinfo=ZoneInfo("Asia/Shanghai"))
```

### 4. 常见时区名称

```python
ZoneInfo("UTC")                    # 协调世界时
ZoneInfo("Asia/Shanghai")          # 中国上海
ZoneInfo("America/New_York")       # 美国纽约
ZoneInfo("Europe/London")          # 英国伦敦
ZoneInfo("Asia/Tokyo")             # 日本东京
ZoneInfo("Australia/Sydney")       # 澳大利亚悉尼
```

## 🎯 学习路径

### 初学者（1-2 小时）

1. `01_basic_usage.py` - 了解基本概念
2. `02_timezone_conversion.py` - 学习时区转换
3. `05_api_timestamp.py` - ISO 8601 格式

### 进阶学习（2-3 小时）

4. `03_database_storage.py` - 数据库最佳实践
5. `07_ecommerce_order.py` - 实际业务场景
6. `08_scheduled_tasks.py` - 定时任务

### 高级应用（2-3 小时）

7. `04_flight_schedule.py` - 复杂时区计算
8. `06_trading_time.py` - 金融系统应用
9. `09_data_analysis.py` - 数据分析场景
10. `10_migration_guide.py` - 从 pytz 迁移

### 综合实践

11. `comprehensive.py` - 完整的业务系统

## ⚠️ 常见陷阱

### 1. Windows 需要 tzdata

```python
# Windows 上首次使用可能报错
# 解决方案：pip install tzdata
```

### 2. 时区名称大小写敏感

```python
# ✅ 正确
ZoneInfo("Asia/Shanghai")

# ❌ 错误
ZoneInfo("asia/shanghai")
```

### 3. naive 和 aware datetime 不能直接比较

```python
dt_naive = datetime.now()
dt_aware = datetime.now(ZoneInfo("UTC"))

# ❌ 这会报错
# dt_naive < dt_aware  # TypeError

# ✅ 需要先转换
dt_naive_aware = dt_naive.replace(tzinfo=ZoneInfo("Asia/Shanghai"))
dt_naive_aware < dt_aware  # 可以比较
```

### 4. 使用 replace() 添加时区要小心

```python
# 假设这个 naive time 代表上海时间
naive_dt = datetime(2023, 6, 15, 10, 30)

# ✅ 如果确定是上海本地时间
shanghai_dt = naive_dt.replace(tzinfo=ZoneInfo("Asia/Shanghai"))

# ⚠️ 如果是 UTC 时间需要转换
utc_dt = naive_dt.replace(tzinfo=ZoneInfo("UTC"))
shanghai_dt = utc_dt.astimezone(ZoneInfo("Asia/Shanghai"))
```

## ✅ 最佳实践

### 1. 数据库存储使用 UTC

```python
# 存储
created_at = datetime.now(ZoneInfo("UTC"))

# 读取后转换为用户时区
user_local_time = created_at.astimezone(ZoneInfo(user_timezone))
```

### 2. API 使用 ISO 8601 格式

```python
# 发送
timestamp = datetime.now(ZoneInfo("UTC")).isoformat()

# 接收
dt = datetime.fromisoformat(timestamp)
```

### 3. 始终使用 aware datetime

```python
# ✅ 推荐
dt = datetime(2023, 6, 15, 10, 30, tzinfo=ZoneInfo("Asia/Shanghai"))

# ❌ 避免（在时区相关代码中）
dt = datetime(2023, 6, 15, 10, 30)
```

### 4. 显示时使用用户时区

```python
# 存储在数据库（UTC）
order_time_utc = datetime.now(ZoneInfo("UTC"))

# 显示给用户（本地时间）
order_time_local = order_time_utc.astimezone(ZoneInfo(user.timezone))
print(f"下单时间: {order_time_local.strftime('%Y-%m-%d %H:%M %Z')}")
```

## 🔗 相关资源

- [PEP 615 – zoneinfo](https://peps.python.org/pep-0615/)
- [Python 3.9 新特性](https://docs.python.org/3/whatsnew/3.9.html#zoneinfo)
- [IANA 时区数据库](https://www.iana.org/time-zones)
- [时区名称列表](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

## 💡 小贴士

1. **查看所有可用时区**
   ```python
   from zoneinfo import available_timezones
   print(sorted(available_timezones()))
   ```

2. **调试时区问题**
   ```python
   # 打印详细时区信息
   dt = datetime.now(ZoneInfo("Asia/Shanghai"))
   print(f"时区: {dt.tzinfo}")
   print(f"UTC 偏移: {dt.strftime('%z')}")
   print(f"时区缩写: {dt.strftime('%Z')}")
   ```

3. **性能考虑**
   ```python
   # 可以缓存 ZoneInfo 对象
   SHANGHAI_TZ = ZoneInfo("Asia/Shanghai")
   
   # 重复使用
   dt1 = datetime.now(SHANGHAI_TZ)
   dt2 = datetime.now(SHANGHAI_TZ)
   ```

## 📝 练习建议

1. **基础练习**：修改示例中的时区，观察输出变化
2. **进阶练习**：实现一个时区转换器工具
3. **实战练习**：为你的项目添加时区支持

---

**下一步**: 查看 `../feature.md` 了解 zoneinfo 的详细特性说明

