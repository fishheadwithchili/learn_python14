"""场景 2：依赖健康检查"""
from importlib import metadata

required = {
    'pip': '20.0.0',
    'setuptools': '50.0.0',
}

print("=" * 60)
print("依赖检查:\n")
for pkg, min_ver in required.items():
    try:
        installed = metadata.version(pkg)
        print(f"  ✅ {pkg}: {installed}")
    except metadata.PackageNotFoundError:
        print(f"  ❌ {pkg}: 未安装")

print("\n💡 早期发现依赖问题")

