"""场景 3：插件系统实现"""
from importlib import metadata

print("=" * 60)
print("插件发现（模拟）:\n")

# 实际使用中会查询 entry_points
# for ep in metadata.entry_points(group='myapp.plugins'):
#     plugin = ep.load()

print("  插件系统需要包定义 entry_points")
print("  可以自动发现和加载插件")

print("\n💡 插件自动发现，无需配置文件")

