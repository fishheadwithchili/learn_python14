"""
场景 6：模板字符串处理

应用：处理模板标记，提取变量名、解析模板语法
"""

# 测试数据
template_vars = [
    "{{ username }}",
    "{{ user.email }}",
    "{{ item.price }}",
    "{{ total }}"
]

mustache_templates = [
    "Hello {{name}}!",
    "Price: ${{price}}",
    "{{#items}}{{name}}{{/items}}"
]

jinja_templates = [
    "{% if user %}Welcome, {{ user.name }}{% endif %}",
    "{% for item in items %}{{ item }}{% endfor %}",
    "{{ value|default('N/A') }}"
]

print("=" * 60)
print("场景 6：模板字符串处理")
print("=" * 60)

# 示例 1：提取 Django/Jinja 变量
print("\n[示例 1] 提取模板变量：\n")

print("传统方式:")
for var in template_vars:
    if var.startswith("{{") and var.endswith("}}"):
        # 手动切片
        name = var[2:-2].strip()  # 移除 {{ 和 }}
        print(f"  {var} → {name}")

print("\nPython 3.9+ 方式:")
for var in template_vars:
    # 使用 removeprefix/removesuffix
    name = var.removeprefix("{{").removesuffix("}}").strip()
    print(f"  {var} → {name}")

# 示例 2：解析 Mustache 模板
print("\n[示例 2] 解析 Mustache 模板：\n")

import re

def extract_mustache_vars(template):
    """提取 Mustache 模板中的所有变量"""
    pattern = r'\{\{(.+?)\}\}'
    matches = re.findall(pattern, template)
    return [m.strip() for m in matches]

for template in mustache_templates:
    variables = extract_mustache_vars(template)
    print(f"  模板: {template}")
    print(f"  变量: {variables}")

# 示例 3：移除块标签
print("\n[示例 3] 提取块标签内容：\n")

block_template = "{{#items}}Item: {{name}}{{/items}}"

# 移除开始和结束标签
if "{{#" in block_template and "{{/" in block_template:
    # 找到开始标签
    start_tag_end = block_template.find("}}")
    start_tag = block_template[:start_tag_end+2]
    
    # 找到结束标签
    end_tag_start = block_template.rfind("{{/")
    end_tag = block_template[end_tag_start:]
    
    # 提取中间内容
    content = block_template.removeprefix(start_tag).removesuffix(end_tag)
    
    print(f"  模板: {block_template}")
    print(f"  开始标签: {start_tag}")
    print(f"  结束标签: {end_tag}")
    print(f"  内容: {content}")

# 示例 4：处理 Jinja2 块
print("\n[示例 4] 移除 Jinja2 控制块：\n")

for template in jinja_templates:
    # 提取纯内容（移除控制语句）
    # 这是简化版，实际应用需要完整的解析器
    content = template
    
    # 移除 {% ... %} 标签
    import re
    cleaned = re.sub(r'\{%.*?%\}', '', content)
    
    print(f"  原始: {template}")
    print(f"  清理后: {cleaned}")

# 示例 5：替换模板变量
print("\n[示例 5] 简单模板渲染：\n")

template = "Hello {{ name }}, your balance is ${{ balance }}."
context = {
    "name": "Alice",
    "balance": "1000.00"
}

# 简单替换
rendered = template
for key, value in context.items():
    placeholder = "{{ " + key + " }}"
    rendered = rendered.replace(placeholder, str(value))

print(f"  模板: {template}")
print(f"  上下文: {context}")
print(f"  渲染结果: {rendered}")

# 示例 6：移除注释标记
print("\n[示例 6] 移除模板注释：\n")

templates_with_comments = [
    "{# This is a comment #}Hello",
    "Price: $100 {# TODO: make dynamic #}",
    "{# Start #}Content{# End #}"
]

for template in templates_with_comments:
    # 移除 Jinja2 注释
    cleaned = re.sub(r'\{#.*?#\}', '', template)
    print(f"  原始: {template}")
    print(f"  清理后: {cleaned}")

# 示例 7：提取 HTML 模板标签
print("\n[示例 7] 提取 HTML 自定义标签：\n")

html_templates = [
    "<user-card>{{user.name}}</user-card>",
    "<product-list>{{items}}</product-list>",
    "<nav-bar></nav-bar>"
]

for html in html_templates:
    # 提取标签名
    if html.startswith("<") and ">" in html:
        tag_end = html.find(">")
        opening_tag = html[1:tag_end]
        
        # 移除自闭合斜杠
        tag_name = opening_tag.removesuffix("/").split()[0]
        
        print(f"  HTML: {html}")
        print(f"  标签名: {tag_name}")

# 示例 8：处理 f-string 模板
print("\n[示例 8] 解析 f-string 风格模板：\n")

f_string_templates = [
    "f'{name}'",
    "f'{user.email}'",
    "f'Total: ${total:.2f}'"
]

for template in f_string_templates:
    # 移除 f-string 标记
    if template.startswith("f'") and template.endswith("'"):
        expression = template.removeprefix("f'").removesuffix("'")
        print(f"  模板: {template}")
        print(f"  表达式: {expression}")

print("\n💡 总结：removeprefix/removesuffix 简化模板解析，提取模板变量")

