"""
场景 1：循环条件中避免重复调用

应用：从文件或输入流逐行读取数据时，避免重复调用 readline()
"""

# 模拟一个文件对象
class SimpleFile:
    def __init__(self, lines):
        self.lines = lines
        self.index = 0
    
    def readline(self):
        """每次读取一行"""
        if self.index < len(self.lines):
            line = self.lines[self.index]
            self.index += 1
            print(f"  [读取] {line}")
            return line
        return ""

# 创建模拟文件
file = SimpleFile([
    "第一行数据",
    "第二行数据",
    "第三行数据"
])

print("=" * 50)
print("使用 Walrus Operator 读取文件")
print("=" * 50)

# ✅ 使用 walrus operator - 简洁且只调用一次 readline()
while (line := file.readline()) != "":
    print(f"  [处理] {line}")

print("\n✅ 完成！每行只读取一次\n")

# ❌ 传统方式对比（需要先读一次，然后在循环内再读）
print("=" * 50)
print("传统方式（不推荐）")
print("=" * 50)

file2 = SimpleFile(["数据A", "数据B"])

line = file2.readline()
while line != "":
    print(f"  [处理] {line}")
    line = file2.readline()

print("\n💡 总结：walrus operator 让代码更紧凑，逻辑集中在循环条件")

