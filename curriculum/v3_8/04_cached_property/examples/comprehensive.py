"""
cached_property 实战示例：Markdown 文档分析器

业务场景：
构建一个文档分析工具，用于处理 Markdown 文件：
1. 解析文档内容和元数据
2. 生成文档摘要
3. 统计字数和阅读时间
4. 提取标题和链接

演示 cached_property 如何避免重复计算和 I/O 操作。

运行要求：Python >= 3.8
"""

from functools import cached_property
import re
import time
from typing import List, Dict

# ============ 模拟的 Markdown 文档 ============

SAMPLE_MARKDOWN = """---
title: Python 3.8 新特性指南
author: 技术团队
date: 2024-01-15
tags: python, tutorial
---

# Python 3.8 新特性指南

## 简介

Python 3.8 带来了多项重要改进，包括赋值表达式、仅位置参数等。

## Walrus Operator

赋值表达式 `:=` 允许在表达式中进行赋值操作。更多信息请访问 [官方文档](https://docs.python.org)。

### 示例代码

```python
if (n := len(data)) > 10:
    print(f"数据量: {n}")
```

## 性能改进

Python 3.8 在多个方面进行了性能优化。

## 总结

本文介绍了 Python 3.8 的核心特性，推荐所有开发者升级。更多详情请参考 [PEP 572](https://peps.python.org/pep-0572/)。
"""


# ============ 文档分析器类 ============

class MarkdownDocument:
    """Markdown 文档分析器
    
    使用 cached_property 确保昂贵的解析操作只执行一次
    """
    
    def __init__(self, content: str):
        self.content = content
        print(f"📄 初始化文档（{len(content)} 字符）")
    
    @cached_property
    def lines(self) -> List[str]:
        """解析文档为行（模拟耗时操作）"""
        print("  🔄 解析文档行...")
        time.sleep(0.1)  # 模拟 I/O 耗时
        return self.content.strip().split('\n')
    
    @cached_property
    def metadata(self) -> Dict[str, str]:
        """提取 YAML 前置元数据"""
        print("  🔄 提取元数据...")
        time.sleep(0.05)
        
        meta = {}
        in_frontmatter = False
        
        for line in self.lines:
            if line.strip() == '---':
                if not in_frontmatter:
                    in_frontmatter = True
                else:
                    break
            elif in_frontmatter and ':' in line:
                key, value = line.split(':', 1)
                meta[key.strip()] = value.strip()
        
        return meta
    
    @cached_property
    def body_text(self) -> str:
        """提取正文内容（去除元数据和代码块）"""
        print("  🔄 提取正文...")
        
        # 跳过前置元数据
        lines = self.lines[:]
        if lines[0].strip() == '---':
            # 找到第二个 ---
            for i, line in enumerate(lines[1:], 1):
                if line.strip() == '---':
                    lines = lines[i+1:]
                    break
        
        # 移除代码块
        text = '\n'.join(lines)
        text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
        
        # 移除 Markdown 标记
        text = re.sub(r'#+\s*', '', text)  # 标题
        text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)  # 链接
        text = re.sub(r'[*_`]', '', text)  # 强调和代码
        
        return text.strip()
    
    @cached_property
    def word_count(self) -> int:
        """计算字数"""
        print("  🔄 统计字数...")
        # 中英文混合计数
        chinese = len(re.findall(r'[\u4e00-\u9fff]', self.body_text))
        english = len(re.findall(r'\b[a-zA-Z]+\b', self.body_text))
        return chinese + english
    
    @cached_property
    def reading_time(self) -> float:
        """估算阅读时间（分钟）"""
        print("  🔄 计算阅读时间...")
        # 假设中文 400 字/分钟，英文 200 词/分钟
        return self.word_count / 300
    
    @cached_property
    def headings(self) -> List[Dict[str, str]]:
        """提取所有标题"""
        print("  🔄 提取标题...")
        headings = []
        
        for line in self.lines:
            match = re.match(r'^(#{1,6})\s+(.+)$', line)
            if match:
                level = len(match.group(1))
                title = match.group(2)
                headings.append({'level': level, 'title': title})
        
        return headings
    
    @cached_property
    def links(self) -> List[Dict[str, str]]:
        """提取所有链接"""
        print("  🔄 提取链接...")
        links = []
        
        for match in re.finditer(r'\[([^\]]+)\]\(([^\)]+)\)', self.content):
            links.append({
                'text': match.group(1),
                'url': match.group(2)
            })
        
        return links
    
    @cached_property
    def summary(self) -> str:
        """生成文档摘要"""
        print("  🔄 生成摘要...")
        time.sleep(0.1)  # 模拟 NLP 处理
        
        # 简单的摘要：取第一段
        paragraphs = self.body_text.split('\n\n')
        first_para = paragraphs[0] if paragraphs else ""
        
        # 截断到 100 字符
        if len(first_para) > 100:
            return first_para[:100] + "..."
        return first_para
    
    def refresh(self):
        """清除所有缓存（模拟文档更新后的刷新）"""
        print("  🔄 清除所有缓存...")
        cache_keys = [
            'lines', 'metadata', 'body_text', 'word_count',
            'reading_time', 'headings', 'links', 'summary'
        ]
        for key in cache_keys:
            self.__dict__.pop(key, None)


# ============ 使用演示 ============

def main():
    print("=" * 60)
    print("Markdown 文档分析器演示")
    print("=" * 60)
    
    # 创建文档对象
    doc = MarkdownDocument(SAMPLE_MARKDOWN)
    
    # ===== 演示 1: 首次访问会触发计算 =====
    print("\n[演示 1] 首次访问属性")
    print("-" * 60)
    
    print(f"📊 元数据: {doc.metadata}")
    print(f"📊 字数统计: {doc.word_count}")
    print(f"📊 阅读时间: {doc.reading_time:.1f} 分钟")
    
    # ===== 演示 2: 再次访问直接返回缓存 =====
    print("\n[演示 2] 再次访问（注意无计算提示）")
    print("-" * 60)
    
    start = time.time()
    for _ in range(3):
        _ = doc.word_count
        _ = doc.reading_time
    elapsed = time.time() - start
    print(f"✅ 6 次属性访问耗时: {elapsed*1000:.2f} ms（几乎无耗时）")
    
    # ===== 演示 3: 查看缓存内容 =====
    print("\n[演示 3] 查看对象的缓存状态")
    print("-" * 60)
    
    cache_keys = [k for k in doc.__dict__.keys() if not k.startswith('_')]
    print(f"已缓存的属性: {cache_keys}")
    
    # ===== 演示 4: 其他分析功能 =====
    print("\n[演示 4] 其他文档分析")
    print("-" * 60)
    
    print(f"\n标题结构:")
    for heading in doc.headings:
        indent = "  " * (heading['level'] - 1)
        print(f"{indent}- {heading['title']}")
    
    print(f"\n链接列表:")
    for link in doc.links:
        print(f"  - {link['text']}: {link['url']}")
    
    print(f"\n文档摘要:")
    print(f"  {doc.summary}")
    
    # ===== 演示 5: 清除缓存 =====
    print("\n[演示 5] 清除缓存后重新访问")
    print("-" * 60)
    
    doc.refresh()
    print(f"📊 字数统计（重新计算）: {doc.word_count}")
    
    print("\n" + "=" * 60)
    print("✅ 演示完成！")
    print("=" * 60)
    print("\n💡 总结:")
    print("  - cached_property 避免了重复的文件 I/O 和计算")
    print("  - 首次访问稍慢，后续访问几乎零成本")
    print("  - 适合不可变数据或对象生命周期内不变的属性")


if __name__ == "__main__":
    main()
