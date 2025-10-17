"""场景 6：依赖图生成"""
from importlib import metadata

print("=" * 60)
print("依赖树（简化）:\n")

try:
    requires = metadata.requires('pip')
    if requires:
        print("  pip 依赖:")
        for req in requires[:5]:  # 只显示前5个
            print(f"    - {req}")
except:
    print("  无法获取依赖信息")

print("\n💡 理解依赖复杂度")

