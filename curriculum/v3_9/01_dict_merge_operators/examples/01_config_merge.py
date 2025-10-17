"""
场景 1：配置文件合并

应用：应用程序需要合并默认配置、环境配置和用户配置，按优先级层层覆盖
"""

# 测试数据
default_config = {
    "theme": "light",
    "font_size": 12,
    "auto_save": True,
    "language": "en",
    "timeout": 30
}

env_config = {
    "language": "zh-CN",  # 覆盖默认
    "timeout": 60,
    "debug": False
}

user_config = {
    "theme": "dark",  # 用户自定义主题
    "font_size": 14
}

print("=" * 60)
print("场景 1：配置文件合并")
print("=" * 60)

# ❌ 传统方式 - 使用解包语法
print("\n[传统方式] 使用 {**dict1, **dict2} 解包语法：\n")
traditional_config = {**default_config, **env_config, **user_config}
print(f"合并结果: {traditional_config}")
print(f"最终主题: {traditional_config['theme']}")
print(f"最终语言: {traditional_config['language']}")

# ✅ 使用 Python 3.9 的 | 运算符
print("\n[Python 3.9+] 使用 | 运算符：\n")
modern_config = default_config | env_config | user_config
print(f"合并结果: {modern_config}")
print(f"最终主题: {modern_config['theme']}")
print(f"最终语言: {modern_config['language']}")

# 验证优先级
print("\n[优先级验证]")
print(f"  默认主题: {default_config['theme']}")
print(f"  环境配置: (无主题设置)")
print(f"  用户主题: {user_config['theme']}")
print(f"  → 最终主题: {modern_config['theme']} (用户配置优先级最高)")

print("\n💡 总结：| 运算符让配置合并更清晰，优先级一目了然")

