"""
场景 10：从 pytz 迁移到 zoneinfo

应用：将现有使用 pytz 的代码迁移到标准库 zoneinfo
"""

try:
    from zoneinfo import ZoneInfo
except ImportError:
    print("需要 Python 3.9+ 或 pip install tzdata")
    exit(1)

from datetime import datetime

print("=" * 60)
print("场景 10：从 pytz 迁移到 zoneinfo")
print("=" * 60)

# ========== 迁移对照表 ==========

print("\n[迁移指南] pytz vs zoneinfo 对照：\n")

print("1. 导入模块")
print("-" * 50)
print("# pytz")
print("import pytz")
print()
print("# zoneinfo")
print("from zoneinfo import ZoneInfo")
print()

print("2. 创建时区对象")
print("-" * 50)
print("# pytz")
print("tz = pytz.timezone('Asia/Shanghai')")
print()
print("# zoneinfo")
print("tz = ZoneInfo('Asia/Shanghai')")
print()

print("3. 创建带时区的 datetime")
print("-" * 50)
print("# pytz - 需要使用 localize()")
print("tz = pytz.timezone('Asia/Shanghai')")
print("dt = tz.localize(datetime(2023, 6, 15, 10, 30))")
print()
print("# zoneinfo - 直接使用 tzinfo 参数")
print("dt = datetime(2023, 6, 15, 10, 30, tzinfo=ZoneInfo('Asia/Shanghai'))")
print()

print("4. 获取当前时间（带时区）")
print("-" * 50)
print("# pytz")
print("now = datetime.now(pytz.timezone('Asia/Shanghai'))")
print()
print("# zoneinfo - 完全相同")
print("now = datetime.now(ZoneInfo('Asia/Shanghai'))")
print()

print("5. 时区转换")
print("-" * 50)
print("# pytz - 需要 normalize()")
print("utc_time = dt.astimezone(pytz.UTC)")
print("ny_time = utc_time.astimezone(pytz.timezone('America/New_York'))")
print()
print("# zoneinfo - 直接使用 astimezone()")
print("utc_time = dt.astimezone(ZoneInfo('UTC'))")
print("ny_time = utc_time.astimezone(ZoneInfo('America/New_York'))")
print()

# ========== 实际代码迁移示例 ==========

print("\n[示例 1] 实际代码迁移：\n")

# 假设这是原来的 pytz 代码（注释掉，因为可能没安装 pytz）
print("❌ 原 pytz 代码:")
print("""
import pytz
from datetime import datetime

# 创建时区
shanghai_tz = pytz.timezone('Asia/Shanghai')

# 创建时间（需要 localize）
meeting_time = shanghai_tz.localize(datetime(2023, 6, 15, 14, 0))

# 转换时区（需要 normalize）
ny_tz = pytz.timezone('America/New_York')
meeting_time_ny = meeting_time.astimezone(ny_tz)
""")

print("\n✅ 迁移后的 zoneinfo 代码:")
print("""
from zoneinfo import ZoneInfo
from datetime import datetime

# 创建时间（直接指定 tzinfo）
meeting_time = datetime(2023, 6, 15, 14, 0, tzinfo=ZoneInfo('Asia/Shanghai'))

# 转换时区（直接 astimezone）
meeting_time_ny = meeting_time.astimezone(ZoneInfo('America/New_York'))
""")

# 实际运行 zoneinfo 版本
meeting_time = datetime(2023, 6, 15, 14, 0, tzinfo=ZoneInfo('Asia/Shanghai'))
meeting_time_ny = meeting_time.astimezone(ZoneInfo('America/New_York'))

print("\n运行结果:")
print(f"上海时间: {meeting_time.strftime('%Y-%m-%d %H:%M %Z')}")
print(f"纽约时间: {meeting_time_ny.strftime('%Y-%m-%d %H:%M %Z')}")

# ========== 常见陷阱及解决方案 ==========

print("\n[示例 2] 常见陷阱：naive datetime 的处理\n")

# 陷阱：直接使用 replace() 可能导致问题
print("⚠️  注意：使用 replace() 添加时区")
print("-" * 50)

naive_dt = datetime(2023, 6, 15, 10, 30)
print(f"Naive datetime: {naive_dt}")

# 使用 replace 添加时区（假设这个时间就是该时区的本地时间）
aware_dt = naive_dt.replace(tzinfo=ZoneInfo('Asia/Shanghai'))
print(f"使用 replace: {aware_dt.strftime('%Y-%m-%d %H:%M %Z')}")

# 如果是 UTC 时间需要转换
utc_dt = naive_dt.replace(tzinfo=ZoneInfo('UTC'))
shanghai_dt = utc_dt.astimezone(ZoneInfo('Asia/Shanghai'))
print(f"UTC 转上海: {shanghai_dt.strftime('%Y-%m-%d %H:%M %Z')}")

# ========== 性能对比 ==========

print("\n[示例 3] zoneinfo 的优势：\n")

advantages = [
    ("标准库内置", "无需安装第三方库"),
    ("API 更简单", "不需要 localize() 和 normalize()"),
    ("更好的性能", "使用系统时区数据，启动更快"),
    ("自动更新", "系统时区数据更新时自动生效"),
    ("类型提示友好", "更好的 IDE 支持")
]

print(f"{'优势':<20} {'说明':<40}")
print("-" * 65)
for advantage, description in advantages:
    print(f"{advantage:<20} {description:<40}")

# ========== 兼容性处理 ==========

print("\n[示例 4] 兼容性处理（同时支持两种库）：\n")

print("# 同时支持 pytz 和 zoneinfo 的代码:")
print("""
try:
    from zoneinfo import ZoneInfo
    def get_timezone(name):
        return ZoneInfo(name)
except ImportError:
    # 回退到 pytz
    import pytz
    def get_timezone(name):
        return pytz.timezone(name)

# 使用统一的接口
tz = get_timezone('Asia/Shanghai')
""")

# 实际演示
def get_timezone(name):
    """获取时区对象（兼容 pytz 和 zoneinfo）"""
    try:
        return ZoneInfo(name)
    except Exception:
        # 如果 zoneinfo 失败，可以考虑回退到 pytz
        # 这里仅作演示
        raise

tz = get_timezone('Asia/Shanghai')
print(f"\n获取时区成功: {tz}")

# ========== 迁移检查清单 ==========

print("\n[迁移检查清单]")
print("-" * 50)

checklist = [
    "✓ 将 import pytz 改为 from zoneinfo import ZoneInfo",
    "✓ 将 pytz.timezone('...') 改为 ZoneInfo('...')",
    "✓ 将 tz.localize(dt) 改为 datetime(..., tzinfo=tz)",
    "✓ 移除所有 normalize() 调用（不再需要）",
    "✓ 将 pytz.UTC 改为 ZoneInfo('UTC')",
    "✓ 测试夏令时边界情况",
    "✓ Windows 环境安装 tzdata: pip install tzdata",
    "✓ 运行完整的测试套件"
]

for item in checklist:
    print(item)

# ========== 实际迁移案例 ==========

print("\n[示例 5] 完整迁移案例：\n")

def old_pytz_style():
    """使用 pytz 风格的代码（仅作示例）"""
    # 注释版本 - 假设使用 pytz
    print("# 旧代码（pytz 风格）：")
    print("""
    import pytz
    tz = pytz.timezone('Asia/Shanghai')
    dt = tz.localize(datetime(2023, 6, 15, 10, 0))
    utc_dt = dt.astimezone(pytz.UTC)
    """)

def new_zoneinfo_style():
    """使用 zoneinfo 的新代码"""
    print("# 新代码（zoneinfo）：")
    dt = datetime(2023, 6, 15, 10, 0, tzinfo=ZoneInfo('Asia/Shanghai'))
    utc_dt = dt.astimezone(ZoneInfo('UTC'))
    
    print(f"dt = datetime(2023, 6, 15, 10, 0, tzinfo=ZoneInfo('Asia/Shanghai'))")
    print(f"utc_dt = dt.astimezone(ZoneInfo('UTC'))")
    print(f"\n结果:")
    print(f"  本地: {dt.strftime('%Y-%m-%d %H:%M %Z')}")
    print(f"  UTC:  {utc_dt.strftime('%Y-%m-%d %H:%M %Z')}")

old_pytz_style()
print()
new_zoneinfo_style()

print("\n💡 总结：zoneinfo 更简单、更符合 Python 标准库习惯，建议迁移")

