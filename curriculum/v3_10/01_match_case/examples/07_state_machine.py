"""
场景 7：状态机实现

应用：实现订单处理、工作流、游戏状态等状态转换逻辑
运行要求：Python >= 3.10
"""

print("=" * 60)
print("场景 7：状态机实现")
print("=" * 60)

# 示例 1：订单状态机
print("\n[示例 1] 订单状态机：\n")

def order_state_transition(current_state, event):
    """处理订单状态转换"""
    match (current_state, event):
        case ("pending", "pay"):
            return ("paid", "✅ 订单已支付")
        case ("paid", "ship"):
            return ("shipped", "📦 订单已发货")
        case ("shipped", "deliver"):
            return ("delivered", "✅ 订单已送达")
        case ("delivered", "confirm"):
            return ("completed", "🎉 订单已完成")
        case ("pending", "cancel"):
            return ("cancelled", "❌ 订单已取消")
        case ("paid", "refund"):
            return ("refunded", "💰 订单已退款")
        case (state, "cancel") if state in ["pending", "paid"]:
            return ("cancelled", "❌ 订单已取消")
        case (state, event):
            return (state, f"⚠️  无效操作: {state} -> {event}")

# 模拟订单流程
order_flow = [
    ("pending", "pay"),
    ("paid", "ship"),
    ("shipped", "deliver"),
    ("delivered", "confirm")
]

current_state = "pending"
print(f"初始状态: {current_state}\n")

for state, event in order_flow:
    new_state, message = order_state_transition(current_state, event)
    print(f"{current_state:12s} --[{event}]--> {new_state:12s} | {message}")
    current_state = new_state

# 测试无效转换
print("\n测试无效转换：")
invalid_transitions = [
    ("pending", "ship"),
    ("shipped", "pay"),
    ("completed", "cancel")
]

for state, event in invalid_transitions:
    new_state, message = order_state_transition(state, event)
    print(f"{state:12s} --[{event}]--> {new_state:12s} | {message}")

# 示例 2：门禁状态机
print("\n[示例 2] 门禁系统状态机：\n")

class DoorStateMachine:
    """门禁状态机"""
    
    def __init__(self):
        self.state = "locked"
    
    def transition(self, event):
        """状态转换"""
        match (self.state, event):
            case ("locked", "unlock"):
                self.state = "unlocked"
                return "🔓 门已解锁"
            case ("unlocked", "open"):
                self.state = "open"
                return "🚪 门已打开"
            case ("open", "close"):
                self.state = "closed"
                return "🚪 门已关闭"
            case ("closed", "lock"):
                self.state = "locked"
                return "🔒 门已上锁"
            case ("closed", "open"):
                self.state = "open"
                return "🚪 门重新打开"
            case ("locked", "force_open"):
                return "🚨 警报！强制开门"
            case (state, event):
                return f"❌ 无效操作: 在 {state} 状态下不能 {event}"

# 测试门禁系统
door = DoorStateMachine()
print(f"初始状态: {door.state}\n")

events = ["unlock", "open", "close", "lock"]
for event in events:
    result = door.transition(event)
    print(f"[{event:12s}] {result} (当前状态: {door.state})")

# 测试异常情况
print("\n测试异常情况：")
door.state = "locked"
print(f"当前状态: {door.state}")
print(door.transition("open"))
print(door.transition("force_open"))

# 示例 3：音乐播放器状态机
print("\n[示例 3] 音乐播放器状态机：\n")

def player_state_transition(state, event, context=None):
    """音乐播放器状态转换"""
    match (state, event):
        case ("stopped", "play"):
            return ("playing", "▶️  开始播放")
        case ("playing", "pause"):
            return ("paused", "⏸️  暂停")
        case ("paused", "play"):
            return ("playing", "▶️  继续播放")
        case ("playing", "stop"):
            return ("stopped", "⏹️  停止")
        case ("paused", "stop"):
            return ("stopped", "⏹️  停止")
        case ("playing", "next"):
            return ("playing", "⏭️  下一曲")
        case ("playing", "previous"):
            return ("playing", "⏮️  上一曲")
        case (_, "load"):
            return ("stopped", "📀 加载歌曲")
        case (state, event):
            return (state, f"⚠️  在 {state} 状态下不能 {event}")

# 模拟播放器操作
player_state = "stopped"
print(f"初始状态: {player_state}\n")

player_events = [
    "load",
    "play",
    "pause",
    "play",
    "next",
    "previous",
    "stop"
]

for event in player_events:
    new_state, message = player_state_transition(player_state, event)
    print(f"{event:12s} -> {message} (状态: {player_state} -> {new_state})")
    player_state = new_state

# 示例 4：TCP 连接状态机
print("\n[示例 4] TCP 连接状态机：\n")

def tcp_state_transition(state, event):
    """TCP 连接状态转换（简化版）"""
    match (state, event):
        case ("CLOSED", "connect"):
            return ("SYN_SENT", "📤 发送 SYN")
        case ("SYN_SENT", "syn_ack"):
            return ("ESTABLISHED", "✅ 连接已建立")
        case ("ESTABLISHED", "send"):
            return ("ESTABLISHED", "📤 发送数据")
        case ("ESTABLISHED", "receive"):
            return ("ESTABLISHED", "📥 接收数据")
        case ("ESTABLISHED", "close"):
            return ("FIN_WAIT_1", "📤 发送 FIN")
        case ("FIN_WAIT_1", "ack"):
            return ("FIN_WAIT_2", "收到 ACK")
        case ("FIN_WAIT_2", "fin"):
            return ("TIME_WAIT", "📥 收到 FIN")
        case ("TIME_WAIT", "timeout"):
            return ("CLOSED", "🔌 连接已关闭")
        case (state, event):
            return (state, f"⚠️  无效转换: {state} + {event}")

# 模拟 TCP 连接生命周期
tcp_state = "CLOSED"
print("TCP 连接生命周期：\n")

tcp_flow = [
    "connect",
    "syn_ack",
    "send",
    "send",
    "receive",
    "close",
    "ack",
    "fin",
    "timeout"
]

for event in tcp_flow:
    new_state, message = tcp_state_transition(tcp_state, event)
    print(f"{tcp_state:15s} --[{event:10s}]--> {new_state:15s} | {message}")
    tcp_state = new_state

# 示例 5：游戏角色状态机
print("\n[示例 5] 游戏角色状态机：\n")

def character_state_transition(state, event, health=100):
    """游戏角色状态转换"""
    match (state, event):
        case ("idle", "move"):
            return ("moving", "🏃 移动中")
        case ("idle", "attack"):
            return ("attacking", "⚔️  攻击中")
        case ("moving", "stop"):
            return ("idle", "🧍 停止")
        case ("moving", "jump"):
            return ("jumping", "🦘 跳跃中")
        case ("jumping", "land"):
            return ("idle", "🧍 着陆")
        case ("attacking", "finish"):
            return ("idle", "✅ 攻击完成")
        case (_, "hit") if health > 20:
            return ("hurt", "💥 受伤")
        case (_, "hit") if health <= 20:
            return ("dying", "💀 濒死")
        case ("hurt", "recover"):
            return ("idle", "💚 恢复")
        case ("dying", "heal"):
            return ("hurt", "❤️  治疗中")
        case (_, "die"):
            return ("dead", "☠️  死亡")
        case ("dead", "respawn"):
            return ("idle", "♻️  重生")
        case (state, event):
            return (state, f"⚠️  无效操作: {state} + {event}")

# 模拟游戏场景
character_state = "idle"
hp = 100

print("游戏场景模拟：\n")

game_events = [
    ("move", 100),
    ("jump", 100),
    ("land", 100),
    ("attack", 100),
    ("finish", 100),
    ("hit", 50),
    ("recover", 50),
    ("hit", 15),
    ("hit", 5),
    ("die", 0),
    ("respawn", 100)
]

for event, health in game_events:
    new_state, message = character_state_transition(character_state, event, health)
    print(f"[HP:{health:3d}] {character_state:10s} --[{event:8s}]--> {new_state:10s} | {message}")
    character_state = new_state

# 示例 6：工作流状态机
print("\n[示例 6] 文档审批工作流：\n")

def workflow_transition(state, event, user_role):
    """文档审批工作流"""
    match (state, event, user_role):
        case ("draft", "submit", "author"):
            return ("pending_review", "📝 提交审核")
        case ("pending_review", "approve", "reviewer"):
            return ("pending_approval", "✅ 审核通过")
        case ("pending_review", "reject", "reviewer"):
            return ("draft", "❌ 审核退回")
        case ("pending_approval", "approve", "manager"):
            return ("approved", "✅ 批准")
        case ("pending_approval", "reject", "manager"):
            return ("pending_review", "❌ 批准退回")
        case ("approved", "publish", "admin"):
            return ("published", "🌐 已发布")
        case (state, event, role):
            return (state, f"⚠️  {role} 无权在 {state} 状态执行 {event}")

# 模拟审批流程
workflow_state = "draft"
print("审批流程：\n")

workflow_steps = [
    ("submit", "author"),
    ("approve", "reviewer"),
    ("approve", "manager"),
    ("publish", "admin")
]

for event, role in workflow_steps:
    new_state, message = workflow_transition(workflow_state, event, role)
    print(f"[{role:8s}] {workflow_state:18s} --[{event:8s}]--> {new_state:18s} | {message}")
    workflow_state = new_state

# 测试权限限制
print("\n测试权限限制：")
test_cases = [
    ("draft", "approve", "author"),
    ("pending_review", "publish", "reviewer")
]

for state, event, role in test_cases:
    new_state, message = workflow_transition(state, event, role)
    print(f"[{role:8s}] {state:18s} --[{event:8s}]--> {message}")

print("\n💡 总结：match/case 是实现状态机的优雅方案，代码清晰易维护")

