"""
场景 4：API 调用或数据库查询结果复用

应用：查询结果需要同时用于判断和后续处理，避免重复查询
"""

import time
from typing import Optional, Dict

# 模拟数据库
USER_DATABASE = {
    101: {"id": 101, "name": "Alice", "is_active": True, "email": "alice@example.com"},
    102: {"id": 102, "name": "Bob", "is_active": False, "email": "bob@example.com"},
    103: {"id": 103, "name": "Charlie", "is_active": True, "email": "charlie@example.com"},
}

def get_user_from_db(user_id: int) -> Optional[Dict]:
    """模拟数据库查询（耗时操作）"""
    print(f"  [DB查询] 查询用户 ID={user_id}...")
    time.sleep(0.1)  # 模拟网络延迟
    return USER_DATABASE.get(user_id)

def send_notification(user: Dict):
    """发送通知"""
    print(f"  [通知] 发送邮件到 {user['email']}")

print("=" * 60)
print("API/数据库查询结果复用")
print("=" * 60)

# ❌ 传统方式 - 可能需要多次查询或临时变量
print("\n[传统方式 1] 可能重复查询：\n")
user_id = 101
if get_user_from_db(user_id):  # 第一次查询
    user = get_user_from_db(user_id)  # 第二次查询！
    if user['is_active']:
        send_notification(user)

print("\n[传统方式 2] 使用临时变量污染作用域：\n")
user_id = 103
user = get_user_from_db(user_id)
if user and user['is_active']:
    send_notification(user)
# user 变量在这里依然存在，可能被误用

# ✅ 使用 walrus operator - 清晰且只查询一次
print("\n[Walrus Operator] 简洁优雅：\n")
user_id = 103
if (user := get_user_from_db(user_id)) and user['is_active']:
    send_notification(user)

print("\n" + "=" * 60)
print("更复杂的示例：链式条件判断")
print("=" * 60)

def get_user_permissions(user_id: int) -> Optional[Dict]:
    """获取用户权限"""
    print(f"  [权限查询] 用户 {user_id}")
    time.sleep(0.05)
    return {"can_edit": True, "can_delete": False}

# 复杂的权限检查
user_id = 101
if (user := get_user_from_db(user_id)) and \
   user['is_active'] and \
   (perms := get_user_permissions(user_id)) and \
   perms['can_edit']:
    print(f"\n✅ 用户 {user['name']} 有编辑权限")
    print(f"   权限: {perms}")
else:
    print(f"\n❌ 用户无权操作")

print("\n💡 总结：减少数据库/API调用次数，提升性能")

