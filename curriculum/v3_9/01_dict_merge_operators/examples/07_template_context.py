"""
场景 7：模板渲染上下文

应用：Web 框架中合并全局上下文、页面上下文和动态数据
"""

# 全局上下文（所有页面共享）
GLOBAL_CONTEXT = {
    "site_name": "我的博客",
    "site_url": "https://myblog.com",
    "year": 2023,
    "analytics_id": "GA-12345"
}

# 页面特定上下文
def get_page_context(page_type):
    """根据页面类型返回特定上下文"""
    contexts = {
        "home": {
            "page_title": "首页",
            "show_sidebar": True,
            "featured_posts": 5
        },
        "article": {
            "page_title": "文章详情",
            "show_sidebar": False,
            "enable_comments": True
        },
        "about": {
            "page_title": "关于我们",
            "show_sidebar": False
        }
    }
    return contexts.get(page_type, {})

# 动态数据（每次请求不同）
def get_dynamic_data(user=None):
    """获取用户相关的动态数据"""
    if user:
        return {
            "user_name": user["name"],
            "user_avatar": user["avatar"],
            "is_authenticated": True
        }
    return {"is_authenticated": False}

print("=" * 60)
print("场景 7：模板渲染上下文")
print("=" * 60)

# 测试用户
test_user = {
    "name": "Alice",
    "avatar": "/static/avatars/alice.jpg"
}

# ❌ 传统方式：逐步构建上下文
print("\n[传统方式] 逐步构建上下文：\n")

def render_page_old(page_type, user=None, extra_context=None):
    """传统方式渲染页面"""
    context = GLOBAL_CONTEXT.copy()
    context.update(get_page_context(page_type))
    context.update(get_dynamic_data(user))
    if extra_context:
        context.update(extra_context)
    return context

context_old = render_page_old(
    "article",
    user=test_user,
    extra_context={"article_id": 123, "article_title": "Python 3.9 新特性"}
)
print("渲染上下文:")
for key, value in context_old.items():
    print(f"  {key}: {value}")

# ✅ 使用 Python 3.9+ 的 | 运算符
print("\n[Python 3.9+] 使用 | 运算符：\n")

def render_page_new(page_type, user=None, extra_context=None):
    """Python 3.9+ 方式渲染页面"""
    return (
        GLOBAL_CONTEXT
        | get_page_context(page_type)
        | get_dynamic_data(user)
        | (extra_context or {})
    )

context_new = render_page_new(
    "article",
    user=test_user,
    extra_context={"article_id": 123, "article_title": "Python 3.9 新特性"}
)
print("渲染上下文:")
for key, value in context_new.items():
    print(f"  {key}: {value}")

# 验证结果一致
print(f"\n结果一致: {context_old == context_new}")

# 不同页面类型示例
print("\n[不同页面类型示例]")

home_context = render_page_new("home", user=test_user)
print(f"首页标题: {home_context['page_title']}")
print(f"显示侧边栏: {home_context['show_sidebar']}")

about_context = render_page_new("about")
print(f"关于页标题: {about_context['page_title']}")
print(f"用户认证: {about_context['is_authenticated']}")

# 代码对比
print("\n[代码对比]")
print("传统方式：")
print("  context = GLOBAL_CONTEXT.copy()")
print("  context.update(get_page_context(page_type))")
print("  context.update(get_dynamic_data(user))")
print("  if extra_context:")
print("      context.update(extra_context)")
print()
print("新方式：")
print("  context = (")
print("      GLOBAL_CONTEXT")
print("      | get_page_context(page_type)")
print("      | get_dynamic_data(user)")
print("      | (extra_context or {})")
print("  )")

print("\n💡 总结：| 运算符让上下文来源清晰，便于理解数据流")

