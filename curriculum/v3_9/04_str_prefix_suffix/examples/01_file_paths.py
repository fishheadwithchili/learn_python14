"""
场景 1：文件路径处理

应用：移除路径前缀，提取相对路径或基础名称
"""

import os

# 测试数据
project_root = "/home/user/myproject"
full_paths = [
    "/home/user/myproject/src/main.py",
    "/home/user/myproject/src/utils/helper.py",
    "/home/user/myproject/tests/test_main.py",
    "/home/user/myproject/README.md"
]

print("=" * 60)
print("场景 1：文件路径处理")
print("=" * 60)

# ❌ 传统方式 - 使用切片
print("\n[传统方式] 使用字符串切片：\n")

print(f"项目根目录: {project_root}\n")

for path in full_paths:
    if path.startswith(project_root):
        relative = path[len(project_root):]
        # 需要额外处理开头的斜杠
        if relative.startswith("/"):
            relative = relative[1:]
        print(f"  {path}")
        print(f"  → {relative}")

# ✅ Python 3.9+ 方式 - 使用 removeprefix
print("\n[Python 3.9+] 使用 removeprefix()：\n")

print(f"项目根目录: {project_root}\n")

for path in full_paths:
    # 一步到位
    relative = path.removeprefix(project_root + "/")
    print(f"  {path}")
    print(f"  → {relative}")

# 示例 2：移除文件扩展名
print("\n[示例 2] 移除文件扩展名：\n")

filenames = [
    "document.pdf",
    "image.png",
    "script.py",
    "archive.tar.gz"
]

print("传统方式（使用 rsplit）:")
for filename in filenames:
    basename, ext = filename.rsplit(".", 1) if "." in filename else (filename, "")
    print(f"  {filename} → {basename}")

print("\nPython 3.9+ (使用 removesuffix):")
for filename in filenames:
    # 需要知道具体扩展名
    if filename.endswith(".tar.gz"):
        basename = filename.removesuffix(".tar.gz")
    elif filename.endswith(".pdf"):
        basename = filename.removesuffix(".pdf")
    elif filename.endswith(".png"):
        basename = filename.removesuffix(".png")
    elif filename.endswith(".py"):
        basename = filename.removesuffix(".py")
    else:
        basename = filename
    print(f"  {filename} → {basename}")

# 示例 3：通用扩展名移除
print("\n[示例 3] 通用扩展名移除：\n")

def remove_extension(filename):
    """移除任意扩展名"""
    if "." in filename:
        # 找到最后一个点的位置
        dot_index = filename.rfind(".")
        return filename[:dot_index]
    return filename

print("通用方法:")
for filename in filenames:
    basename = remove_extension(filename)
    print(f"  {filename} → {basename}")

# 示例 4：路径规范化
print("\n[示例 4] Windows 路径处理：\n")

windows_paths = [
    "C:\\Users\\Admin\\Documents\\file.txt",
    "C:\\Program Files\\MyApp\\config.ini"
]

prefix = "C:\\Users\\Admin\\"

print(f"移除前缀: {prefix}\n")

for path in windows_paths:
    relative = path.removeprefix(prefix)
    print(f"  {path}")
    print(f"  → {relative}")

print("\n💡 总结：removeprefix/removesuffix 让路径处理更简洁安全")

