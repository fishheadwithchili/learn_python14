"""
场景 10：递归数据结构的深度遍历

应用：遍历树或图时需要同时赋值和判断，避免 None 检查
"""

from typing import Optional

class TreeNode:
    """二叉树节点"""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"Node({self.value})"

# 构建示例树
#         1
#       /   \
#      2     3
#     / \     \
#    4   5     6
tree = TreeNode(1,
    TreeNode(2,
        TreeNode(4),
        TreeNode(5)
    ),
    TreeNode(3,
        None,
        TreeNode(6)
    )
)

print("=" * 60)
print("树结构遍历")
print("=" * 60)

# ❌ 传统方式 - 需要额外的 None 检查
print("\n[传统方式] 显式 None 检查：\n")

def find_node_old(root: Optional[TreeNode], target: int, path: list) -> bool:
    """查找节点（传统方式）"""
    if root is None:
        return False
    
    path.append(root.value)
    
    if root.value == target:
        return True
    
    if find_node_old(root.left, target, path):
        return True
    
    if find_node_old(root.right, target, path):
        return True
    
    path.pop()
    return False

path_old = []
target = 5
if find_node_old(tree, target, path_old):
    print(f"  ✅ 找到节点 {target}")
    print(f"  路径: {' → '.join(map(str, path_old))}")

# ✅ 使用 walrus operator - 更简洁
print("\n[Walrus Operator] 简洁的遍历：\n")

def find_node_new(root: Optional[TreeNode], target: int, path: list) -> bool:
    """查找节点（使用 walrus operator）"""
    if root is None:
        return False
    
    path.append(root.value)
    
    if root.value == target:
        return True
    
    # 合并赋值和判断
    if (left := root.left) and find_node_new(left, target, path):
        return True
    
    if (right := root.right) and find_node_new(right, target, path):
        return True
    
    path.pop()
    return False

path_new = []
target = 6
if find_node_new(tree, target, path_new):
    print(f"  ✅ 找到节点 {target}")
    print(f"  路径: {' → '.join(map(str, path_new))}")

print("\n" + "=" * 60)
print("字典/JSON 深度访问")
print("=" * 60)

# 嵌套字典（类似 JSON 数据）
config = {
    'database': {
        'primary': {
            'host': 'db1.example.com',
            'port': 5432,
            'credentials': {
                'username': 'admin',
                'password': 'secret'
            }
        }
    },
    'cache': {
        'redis': {
            'host': 'redis.example.com'
        }
    }
}

print("\n安全的深度访问：\n")

# ✅ 使用 walrus operator 进行安全的深度访问
path = ['database', 'primary', 'credentials', 'username']

current = config
for key in path:
    if not (current := current.get(key)):
        print(f"  ❌ 路径中断于: {key}")
        break
else:
    print(f"  ✅ 找到值: {current}")
    print(f"  完整路径: {' → '.join(path)}")

print("\n尝试访问不存在的路径：\n")

# 不存在的路径
invalid_path = ['database', 'secondary', 'host']

current = config
for i, key in enumerate(invalid_path):
    if not (current := current.get(key)):
        print(f"  ❌ 键 '{key}' 不存在（路径深度: {i}）")
        print(f"  已访问: {' → '.join(invalid_path[:i])}")
        break
else:
    print(f"  ✅ 找到值: {current}")

print("\n" + "=" * 60)
print("链表遍历")
print("=" * 60)

class ListNode:
    """链表节点"""
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# 创建链表: 1 → 2 → 3 → 4 → 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print("\n遍历链表：\n")

# ✅ 使用 walrus operator
current = head
values = []
while (node := current):
    values.append(node.value)
    current = node.next

print(f"  链表值: {' → '.join(map(str, values))}")

# 查找特定值
print("\n查找链表中的值：\n")

current = head
target = 3
position = 0

while (node := current) and node.value != target:
    position += 1
    current = node.next

if node:
    print(f"  ✅ 在位置 {position} 找到值 {target}")
else:
    print(f"  ❌ 未找到值 {target}")

print("\n💡 总结：简化递归结构遍历，减少 None 检查代码")

