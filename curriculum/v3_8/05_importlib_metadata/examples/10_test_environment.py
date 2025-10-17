"""场景 10：测试环境验证"""
from importlib import metadata

test_packages = ['pytest', 'setuptools']

print("=" * 60)
print("测试环境检查:\n")

missing = []
for pkg in test_packages:
    try:
        ver = metadata.version(pkg)
        print(f"  ✅ {pkg}: {ver}")
    except metadata.PackageNotFoundError:
        missing.append(pkg)
        print(f"  ❌ {pkg}: 未安装")

if missing:
    print(f"\n缺少: {', '.join(missing)}")
else:
    print("\n✅ 测试环境完整")

print("\n💡 确保测试环境一致性")

