"""场景 7：环境诊断工具"""
from importlib import metadata

print("=" * 60)
print("环境信息:\n")

count = 0
for dist in metadata.distributions():
    if count < 10:  # 只显示前10个
        print(f"  {dist.name}: {dist.version}")
        count += 1

print(f"  ... (共 {count}+ 个包)")

print("\n💡 快速诊断环境差异")

