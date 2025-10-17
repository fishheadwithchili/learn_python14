"""场景 5：Python 版本兼容性检测"""
from importlib import metadata
import sys

print("=" * 60)
print(f"当前 Python: {sys.version_info.major}.{sys.version_info.minor}")

try:
    meta = metadata.metadata('pip')
    requires_python = meta.get('Requires-Python', 'Any')
    print(f"pip 需要: {requires_python}")
except:
    pass

print("\n💡 提前发现兼容性问题")

