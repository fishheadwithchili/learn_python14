"""
检查 Python 版本和 GIL 状态

用于确认是否使用了 Python 3.14t (free-threading) 版本
"""

import sys
import sysconfig

print("=" * 60)
print("Python 版本信息检查")
print("=" * 60)

# 基本版本信息
print(f"\nPython 版本: {sys.version}")
print(f"版本号: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
print(f"可执行文件: {sys.executable}")

# 检查是否为 free-threading 构建
print("\n" + "=" * 60)
print("GIL 状态检查")
print("=" * 60)

# Python 3.13+ 可以通过 sys._is_gil_enabled() 检查
if hasattr(sys, '_is_gil_enabled'):
    try:
        gil_enabled = sys._is_gil_enabled()
        if gil_enabled:
            print("❌ GIL 状态: 已启用 (标准版本)")
            print("   这是带 GIL 的标准 Python")
        else:
            print("✅ GIL 状态: 已禁用 (free-threading 版本)")
            print("   🎉 这是 Python 3.14t - 支持真多线程!")
    except Exception as e:
        print(f"⚠️  无法检测 GIL 状态: {e}")
else:
    print("⚠️  此版本不支持 GIL 状态检查")
    print("   (需要 Python 3.13+)")

# 检查构建配置
print("\n" + "=" * 60)
print("构建配置")
print("=" * 60)

config_vars = sysconfig.get_config_vars()

# 检查是否包含 free-threading 相关配置
if 'Py_GIL_DISABLED' in config_vars:
    print(f"✅ Py_GIL_DISABLED: {config_vars['Py_GIL_DISABLED']}")
    print("   这是 free-threading 构建")
else:
    print("❌ 未找到 Py_GIL_DISABLED 配置")
    print("   这可能是标准 GIL 构建")

# 检查 abiflags
abiflags = sysconfig.get_config_var('abiflags') or ''
print(f"\nABI Flags: {abiflags if abiflags else '(无)'}")
if 't' in abiflags:
    print("✅ 包含 't' 标志 - free-threading 版本")
else:
    print("❌ 不包含 't' 标志 - 标准版本")

# 总结
print("\n" + "=" * 60)
print("总结")
print("=" * 60)

is_free_threading = (
    hasattr(sys, '_is_gil_enabled') and 
    callable(sys._is_gil_enabled) and 
    not sys._is_gil_enabled()
)

if is_free_threading:
    print("🎉 恭喜！你正在使用 Python 3.14t (free-threading)")
    print("   可以学习和测试无 GIL 的真多线程特性")
    print("\n💡 建议学习内容:")
    print("   - 多线程性能对比（有GIL vs 无GIL）")
    print("   - CPU 密集型任务的并行加速")
    print("   - 线程安全的新注意事项")
elif sys.version_info >= (3, 13):
    print("⚠️  你正在使用带 GIL 的 Python 3.13+")
    print("   如果要学习 free-threading，需要安装 3.13t 或 3.14t")
    print("\n💡 安装方法:")
    print("   1. 从 python.org 下载 'free-threaded' 版本")
    print("   2. 或使用 pyenv: pyenv install 3.14t")
else:
    print(f"ℹ️  当前版本: Python {sys.version_info.major}.{sys.version_info.minor}")
    print("   free-threading 需要 Python 3.13+")

print("\n" + "=" * 60)

