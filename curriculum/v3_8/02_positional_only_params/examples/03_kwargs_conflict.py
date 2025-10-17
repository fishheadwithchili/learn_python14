"""
场景 3：避免参数名与 kwargs 冲突

应用：函数接受任意关键字参数，但自身参数名可能与之冲突
"""

print("=" * 60)
print("避免参数名与 **kwargs 冲突")
print("=" * 60)

# ❌ 没有使用仅位置参数的问题
print("\n[问题演示] 参数名冲突：\n")

def create_user_bad(name, **attributes):
    """创建用户（有问题的版本）"""
    user = {'username': name}
    user.update(attributes)
    return user

# 正常使用
user1 = create_user_bad('alice', age=30, email='alice@example.com')
print(f"  ✅ 正常: {user1}")

# 问题：如果 attributes 中有 'name' 键
try:
    # 这会导致：TypeError: create_user_bad() got multiple values for argument 'name'
    user2 = create_user_bad('bob', name='Bob Smith', age=25)
except TypeError as e:
    print(f"  ❌ 冲突: {e}")

# ✅ 使用仅位置参数解决
print("\n[解决方案] 使用仅位置参数：\n")

def create_user(name, /, **attributes):
    """
    创建用户（改进版）
    
    参数:
        name: 用户名（仅位置，避免与 attributes 冲突）
        **attributes: 其他属性（可以包含 'name' 字段）
    """
    user = {'username': name}
    user.update(attributes)
    return user

# 现在可以安全使用
user1 = create_user('alice', age=30, email='alice@example.com')
print(f"  ✅ 基本使用: {user1}")

# attributes 可以包含 'name' 字段而不冲突
user2 = create_user('bob', name='Bob Smith', age=25, email='bob@example.com')
print(f"  ✅ 包含 name: {user2}")

print("\n" + "=" * 60)
print("更多实际应用")
print("=" * 60)

def update_config(config_dict, /, **updates):
    """
    更新配置字典
    
    参数:
        config_dict: 要更新的配置（仅位置）
        **updates: 更新内容（可以包含任意键）
    """
    config_dict.update(updates)
    return config_dict

print("\n更新配置：\n")

config = {'debug': False, 'port': 8080}
print(f"  原始配置: {config}")

# 可以安全地使用 'config_dict' 作为更新键
updated = update_config(config, debug=True, config_dict='override', timeout=30)
print(f"  更新后: {updated}")

print("\n" + "=" * 60)
print("HTML 标签生成器示例")
print("=" * 60)

def create_tag(tag_name, content, /, **attrs):
    """
    生成 HTML 标签
    
    参数:
        tag_name: 标签名（仅位置）
        content: 标签内容（仅位置）
        **attrs: HTML 属性
    """
    attr_str = ' '.join(f'{k}="{v}"' for k, v in attrs.items())
    if attr_str:
        return f'<{tag_name} {attr_str}>{content}</{tag_name}>'
    return f'<{tag_name}>{content}</{tag_name}>'

print("\n生成 HTML 标签：\n")

# 基本使用
link = create_tag('a', 'Click here', href='https://example.com', class_='button')
print(f"  {link}")

# attrs 可以包含 'tag_name' 或 'content'（虽然没意义，但不会报错）
div = create_tag('div', 'Hello', tag_name='should_be_ignored', content='also_ignored', id='main')
print(f"  {div}")

print("\n" + "=" * 60)
print("装饰器参数传递")
print("=" * 60)

def with_metadata(func, /, **metadata):
    """
    为函数附加元数据
    
    参数:
        func: 要装饰的函数（仅位置）
        **metadata: 元数据（可以包含 'func' 字段）
    """
    func.__metadata__ = metadata
    return func

@with_metadata
def my_function():
    """示例函数"""
    pass

# 添加元数据
my_function = with_metadata(my_function, author='Alice', func='metadata_value', version='1.0')

print(f"\n函数元数据: {my_function.__metadata__}")

print("\n💡 总结：仅位置参数让 **kwargs 可以安全使用任意键名")

