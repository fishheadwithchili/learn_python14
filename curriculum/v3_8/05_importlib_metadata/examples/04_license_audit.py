"""场景 4：许可证合规审计"""
from importlib import metadata

print("=" * 60)
print("许可证扫描:\n")

packages = ['pip', 'setuptools']
for pkg in packages:
    try:
        meta = metadata.metadata(pkg)
        license_type = meta.get('License', 'Unknown')
        print(f"  {pkg}: {license_type}")
    except:
        pass

print("\n💡 快速生成依赖许可证报告")

