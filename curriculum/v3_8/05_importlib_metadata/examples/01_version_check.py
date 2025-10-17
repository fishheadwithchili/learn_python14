"""场景 1：CLI 工具显示版本信息"""
from importlib import metadata

print("=" * 60)
try:
    version = metadata.version('pip')
    print(f"pip 版本: {version}")
    
    setuptools_ver = metadata.version('setuptools')
    print(f"setuptools 版本: {setuptools_ver}")
except metadata.PackageNotFoundError as e:
    print(f"包未找到: {e}")

print("💡 版本号自动从包元数据读取")

