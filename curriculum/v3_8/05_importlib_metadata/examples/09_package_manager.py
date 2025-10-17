"""场景 9：包管理器实现"""
from importlib import metadata

print("=" * 60)
print("已安装包列表:\n")

packages = []
for dist in metadata.distributions():
    packages.append((dist.name, dist.version))

# 按名称排序
packages.sort(key=lambda x: x[0].lower())

# 显示前10个
for name, ver in packages[:10]:
    print(f"  {name}: {ver}")

print(f"\n  总计: {len(packages)} 个包")

print("\n💡 构建自动化工具")

