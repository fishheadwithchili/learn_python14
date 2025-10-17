# zoneinfo - 标准库时区支持

## 一句话总结

标准库内置 IANA 时区数据库支持，无需第三方库即可处理时区转换和本地化时间。

## 功能详解

### 是什么？

`zoneinfo` 是 Python 3.9 引入的标准库模块（PEP 615），提供对 IANA 时区数据库的访问，取代第三方库 `pytz`。

**语法格式**:
```python
from zoneinfo import ZoneInfo
from datetime import datetime

# 创建带时区的时间
dt = datetime(2023, 6, 15, 10, 30, tzinfo=ZoneInfo("Asia/Shanghai"))

# 转换时区
dt_ny = dt.astimezone(ZoneInfo("America/New_York"))
```

### 解决什么问题？

**问题 1: 时区处理依赖第三方库**
```python
# 旧代码 - 需要安装 pytz
import pytz
tz = pytz.timezone("Asia/Shanghai")
```

**问题 2: pytz 使用复杂且容易出错**
```python
# pytz 的 localize 和 normalize 容易混淆
tz = pytz.timezone("Asia/Shanghai")
dt = tz.localize(datetime(2023, 6, 15, 10, 30))
```

**问题 3: 标准库 datetime 时区支持不完善**
```python
# 旧代码 - 只有 UTC，其他时区需要自己实现
from datetime import timezone, timedelta
# 手动定义时区很麻烦
```

### 语法要点

1. **基本用法**
   ```python
   from zoneinfo import ZoneInfo
   from datetime import datetime
   
   # 创建带时区的时间
   dt = datetime(2023, 6, 15, 10, 30, tzinfo=ZoneInfo("Asia/Shanghai"))
   ```

2. **时区转换**
   ```python
   # 转换到其他时区
   dt_utc = dt.astimezone(ZoneInfo("UTC"))
   dt_ny = dt.astimezone(ZoneInfo("America/New_York"))
   ```

3. **获取当前时间（带时区）**
   ```python
   # 当前时间（指定时区）
   now = datetime.now(ZoneInfo("Asia/Shanghai"))
   
   # UTC 当前时间
   now_utc = datetime.now(ZoneInfo("UTC"))
   ```

4. **时区名称**
   ```python
   # 使用 IANA 时区数据库名称
   ZoneInfo("Asia/Shanghai")  # 中国上海
   ZoneInfo("America/New_York")  # 美国纽约
   ZoneInfo("Europe/London")  # 英国伦敦
   ```

5. **列出所有时区**
   ```python
   from zoneinfo import available_timezones
   
   # 获取所有可用时区
   all_zones = available_timezones()
   ```

6. **Windows 支持**
   ```python
   # Windows 可能需要安装 tzdata 包
   # pip install tzdata
   ```

## 核心应用场景

### 1. **跨时区时间转换**
将时间从一个时区转换到另一个时区：
```python
shanghai = datetime.now(ZoneInfo("Asia/Shanghai"))
newyork = shanghai.astimezone(ZoneInfo("America/New_York"))
```
**收益**: 准确处理夏令时和历史时区变化

### 2. **国际化应用**
显示用户所在时区的本地时间：
```python
utc_time = get_from_database()  # UTC 时间
local_time = utc_time.astimezone(ZoneInfo(user_timezone))
```
**收益**: 提升用户体验

### 3. **日志时间戳**
为日志添加准确的时区信息：
```python
log_time = datetime.now(ZoneInfo("Asia/Shanghai"))
```
**收益**: 便于跨时区调试

### 4. **会议时间安排**
协调不同时区的会议时间：
```python
meeting_beijing = datetime(2023, 6, 15, 14, 0, tzinfo=ZoneInfo("Asia/Shanghai"))
meeting_london = meeting_beijing.astimezone(ZoneInfo("Europe/London"))
```
**收益**: 避免时间混淆

### 5. **航班时刻表**
处理起飞和降落时间的时区转换：
```python
departure = datetime(2023, 6, 15, 10, 0, tzinfo=ZoneInfo("Asia/Shanghai"))
arrival_local = arrival_utc.astimezone(ZoneInfo("America/Los_Angeles"))
```
**收益**: 准确显示当地时间

### 6. **金融交易时间**
记录交易的准确时区：
```python
trade_time = datetime.now(ZoneInfo("America/New_York"))
```
**收益**: 符合监管要求

### 7. **电商订单时间**
显示用户时区的订单时间：
```python
order_time_utc = get_order_time()
order_time_local = order_time_utc.astimezone(ZoneInfo(user.timezone))
```
**收益**: 用户友好

### 8. **定时任务调度**
在特定时区执行任务：
```python
run_time = datetime(2023, 6, 15, 9, 0, tzinfo=ZoneInfo("Asia/Tokyo"))
```
**收益**: 准确的任务执行时间

### 9. **数据分析**
处理带时区的时间序列数据：
```python
df['timestamp'] = df['timestamp'].apply(
    lambda x: x.astimezone(ZoneInfo("Asia/Shanghai"))
)
```
**收益**: 统一时区便于分析

### 10. **API 响应**
返回 ISO 格式的时区时间：
```python
response_time = datetime.now(ZoneInfo("UTC")).isoformat()
```
**收益**: 标准化时间格式

## 示例代码说明

本目录的 `examples/` 包含 **10 个独立场景示例** 和 **1 个综合示例**。

运行示例：
```bash
cd curriculum/v3_9/05_zoneinfo/examples
python 01_basic_usage.py
```

**注意**: Windows 用户可能需要安装 `tzdata` 包：
```bash
pip install tzdata
```

## 注意事项

### ⚠️ 常见陷阱

1. **Windows 需要 tzdata 包**
   ```python
   # Windows 上可能报错
   # pip install tzdata 解决
   ```

2. **时区名称大小写敏感**
   ```python
   # ✅ 正确
   ZoneInfo("Asia/Shanghai")
   
   # ❌ 错误
   ZoneInfo("asia/shanghai")
   ```

3. **naive vs aware datetime**
   ```python
   # naive datetime（无时区信息）
   dt_naive = datetime.now()
   
   # aware datetime（有时区信息）
   dt_aware = datetime.now(ZoneInfo("UTC"))
   
   # 不能直接比较 naive 和 aware
   # dt_naive < dt_aware  # TypeError
   ```

4. **夏令时自动处理**
   ```python
   # zoneinfo 自动处理夏令时
   # 无需手动调整
   ```

### ✅ 最佳实践

1. **数据库存储使用 UTC** - 避免时区混淆
2. **显示时使用用户时区** - 提升体验
3. **始终使用 aware datetime** - 避免歧义
4. **使用 IANA 时区名称** - 标准化
5. **API 使用 ISO 8601 格式** - 包含时区信息

## 与其他版本的关系

- **Python 3.8**: 不支持，需使用 `pytz`
- **Python 3.9+**: 标准库支持，推荐使用
- **向后兼容**: `zoneinfo` 可与 `pytz` 共存

**迁移指南**:
```python
# 从 pytz 迁移到 zoneinfo

# pytz
import pytz
tz = pytz.timezone("Asia/Shanghai")
dt = tz.localize(datetime(2023, 6, 15, 10, 30))

# zoneinfo
from zoneinfo import ZoneInfo
dt = datetime(2023, 6, 15, 10, 30, tzinfo=ZoneInfo("Asia/Shanghai"))
```

## 扩展阅读

- [PEP 615 – Support for the IANA Time Zone Database in the Standard Library](https://peps.python.org/pep-0615/)
- [Python 3.9 新特性文档](https://docs.python.org/3/whatsnew/3.9.html#zoneinfo)
- [IANA 时区数据库](https://www.iana.org/time-zones)

## 快速检查清单

- [ ] 理解 zoneinfo 和 pytz 的区别
- [ ] 知道如何创建带时区的 datetime
- [ ] 能够进行时区转换
- [ ] 了解 naive 和 aware datetime 的区别
- [ ] 知道 Windows 需要安装 tzdata

