"""场景 3：文档解析和元数据提取"""
from functools import cached_property
import time

class Document:
    def __init__(self, filepath):
        self.filepath = filepath
    
    @cached_property
    def content(self):
        print(f"  [读取文件]...")
        time.sleep(0.05)
        return "文档内容模拟数据" * 100
    
    @cached_property
    def word_count(self):
        print(f"  [统计字数]...")
        return len(self.content.split())
    
    @cached_property
    def char_count(self):
        return len(self.content)

print("=" * 60)
doc = Document("document.txt")
print(f"字数: {doc.word_count}")
print(f"字符数: {doc.char_count}")
print(f"再次访问: {doc.word_count}")
print("💡 文件只读取一次")

