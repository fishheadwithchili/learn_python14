"""
场景 3：命名约定处理

应用：移除类名、函数名、变量名中的前缀/后缀，提取核心名称
"""

# 测试数据
class_names = [
    "TestUserModel",
    "TestProductModel",
    "BaseController",
    "AbstractFactory",
    "IUserService"
]

function_names = [
    "get_user_by_id",
    "set_user_name",
    "is_valid_email",
    "has_permission"
]

variable_names = [
    "_private_var",
    "__dunder_var",
    "m_memberVar",
    "str_username",
    "int_count"
]

print("=" * 60)
print("场景 3：命名约定处理")
print("=" * 60)

# 示例 1：移除测试类前缀
print("\n[示例 1] 移除测试类前缀：\n")

print("移除 'Test' 前缀:")
for name in class_names:
    clean_name = name.removeprefix("Test")
    if clean_name != name:
        print(f"  {name} → {clean_name}")

# 示例 2：移除基类后缀
print("\n[示例 2] 移除常见后缀：\n")

suffixes_to_remove = ["Model", "Controller", "Service", "Factory"]

for name in class_names:
    clean_name = name
    # 移除所有已知后缀
    for suffix in suffixes_to_remove:
        clean_name = clean_name.removesuffix(suffix)
    
    if clean_name != name:
        print(f"  {name} → {clean_name}")

# 示例 3：移除接口前缀（I 开头）
print("\n[示例 3] 移除接口前缀：\n")

interface_names = [
    "IUserService",
    "IProductRepository",
    "ILogger",
    "UserService"  # 不以 I 开头
]

for name in interface_names:
    impl_name = name.removeprefix("I")
    if impl_name != name:
        print(f"  接口: {name} → 实现: {impl_name}")
    else:
        print(f"  {name} (已经是实现类)")

# 示例 4：移除函数前缀（get_, set_, is_, has_）
print("\n[示例 4] 提取函数核心名称：\n")

prefixes = ["get_", "set_", "is_", "has_"]

for func_name in function_names:
    core_name = func_name
    for prefix in prefixes:
        core_name = core_name.removeprefix(prefix)
    
    if core_name != func_name:
        print(f"  {func_name} → 核心: {core_name}")

# 示例 5：移除私有变量标记
print("\n[示例 5] 移除私有变量标记：\n")

for var_name in variable_names:
    # Python 私有变量约定
    public_name = var_name.removeprefix("_").removeprefix("__")
    if public_name != var_name:
        print(f"  {var_name} → {public_name}")

# 示例 6：移除匈牙利命名法前缀
print("\n[示例 6] 移除匈牙利命名法前缀：\n")

hungarian_vars = [
    "str_username",
    "int_count",
    "bool_isActive",
    "arr_items",
    "obj_user"
]

type_prefixes = ["str_", "int_", "bool_", "arr_", "obj_", "m_"]

for var_name in hungarian_vars:
    clean_name = var_name
    for prefix in type_prefixes:
        clean_name = clean_name.removeprefix(prefix)
    print(f"  {var_name} → {clean_name}")

# 示例 7：数据库表名转模型名
print("\n[示例 7] 数据库表名转模型名：\n")

table_names = [
    "tbl_users",
    "tbl_products",
    "user_sessions",
    "app_config"
]

for table_name in table_names:
    # 移除表前缀
    model_name = table_name.removeprefix("tbl_").removeprefix("app_")
    # 转换为类名格式（首字母大写）
    model_class = ''.join(word.capitalize() for word in model_name.split('_'))
    print(f"  表: {table_name} → 模型: {model_class}")

# 示例 8：环境变量前缀处理
print("\n[示例 8] 环境变量前缀处理：\n")

env_vars = [
    "APP_DATABASE_URL",
    "APP_SECRET_KEY",
    "APP_DEBUG",
    "DATABASE_HOST"
]

app_prefix = "APP_"

print(f"移除应用前缀 '{app_prefix}':")
for var in env_vars:
    config_key = var.removeprefix(app_prefix)
    if config_key != var:
        print(f"  {var} → {config_key}")
    else:
        print(f"  {var} (无前缀)")

# 示例 9：版本号处理
print("\n[示例 9] 版本号标签处理：\n")

version_tags = [
    "v1.0.0",
    "v2.3.1",
    "release-1.5.0",
    "beta-2.0.0"
]

for tag in version_tags:
    version = tag.removeprefix("v").removeprefix("release-").removeprefix("beta-")
    print(f"  标签: {tag} → 版本: {version}")

# 示例 10：文件备份后缀
print("\n[示例 10] 移除备份文件后缀：\n")

backup_files = [
    "config.json.bak",
    "database.sql.backup",
    "settings.ini.old",
    "log.txt~"
]

backup_suffixes = [".bak", ".backup", ".old", "~"]

for filename in backup_files:
    original = filename
    for suffix in backup_suffixes:
        original = original.removesuffix(suffix)
    print(f"  备份: {filename} → 原始: {original}")

print("\n💡 总结：removeprefix/removesuffix 处理命名约定，提取核心名称")

