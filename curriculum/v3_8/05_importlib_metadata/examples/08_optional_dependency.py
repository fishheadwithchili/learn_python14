"""场景 8：动态导入验证"""
from importlib import metadata

def check_feature(feature_name, package):
    """检查可选功能是否可用"""
    try:
        metadata.version(package)
        return True
    except metadata.PackageNotFoundError:
        return False

print("=" * 60)
has_requests = check_feature('HTTP', 'requests')
print(f"HTTP 功能: {'✅ 可用' if has_requests else '❌ 不可用'}")

print("\n💡 友好的可选依赖提示")

