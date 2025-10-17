"""
场景 5：事件处理系统

应用：处理GUI、游戏或系统中的各种事件消息
运行要求：Python >= 3.10
"""

print("=" * 60)
print("场景 5：事件处理系统")
print("=" * 60)

# 示例 1：鼠标事件处理
print("\n[示例 1] 鼠标事件处理：\n")

def handle_mouse_event(event):
    """处理各种鼠标事件"""
    match event:
        case {"type": "click", "button": "left", "x": x, "y": y}:
            return f"🖱️  左键点击位置: ({x}, {y})"
        case {"type": "click", "button": "right", "x": x, "y": y}:
            return f"🖱️  右键点击位置: ({x}, {y})"
        case {"type": "double_click", "x": x, "y": y}:
            return f"🖱️  双击位置: ({x}, {y})"
        case {"type": "drag", "from": (x1, y1), "to": (x2, y2)}:
            return f"🖱️  拖拽: ({x1}, {y1}) -> ({x2}, {y2})"
        case {"type": "scroll", "direction": "up", "amount": amount}:
            return f"🖱️  向上滚动 {amount} 单位"
        case {"type": "scroll", "direction": "down", "amount": amount}:
            return f"🖱️  向下滚动 {amount} 单位"
        case {"type": "hover", "x": x, "y": y}:
            return f"🖱️  悬停在: ({x}, {y})"
        case _:
            return "❓ 未知鼠标事件"

# 测试鼠标事件
mouse_events = [
    {"type": "click", "button": "left", "x": 100, "y": 200},
    {"type": "click", "button": "right", "x": 150, "y": 250},
    {"type": "double_click", "x": 120, "y": 220},
    {"type": "drag", "from": (50, 50), "to": (200, 200)},
    {"type": "scroll", "direction": "up", "amount": 3},
    {"type": "scroll", "direction": "down", "amount": 5},
    {"type": "hover", "x": 175, "y": 225}
]

for event in mouse_events:
    print(handle_mouse_event(event))

# 示例 2：键盘事件处理
print("\n[示例 2] 键盘事件处理：\n")

def handle_keyboard_event(event):
    """处理键盘事件"""
    match event:
        case {"type": "keydown", "key": "Enter"}:
            return "⌨️  回车键按下"
        case {"type": "keydown", "key": "Escape"}:
            return "⌨️  ESC 键按下"
        case {"type": "keydown", "key": key, "ctrl": True}:
            return f"⌨️  Ctrl+{key}"
        case {"type": "keydown", "key": key, "shift": True}:
            return f"⌨️  Shift+{key}"
        case {"type": "keydown", "key": key, "alt": True}:
            return f"⌨️  Alt+{key}"
        case {"type": "keydown", "key": "F" + num} if num.isdigit():
            return f"⌨️  功能键 F{num}"
        case {"type": "keydown", "key": key}:
            return f"⌨️  按下 {key}"
        case {"type": "keyup", "key": key}:
            return f"⌨️  释放 {key}"
        case _:
            return "❓ 未知键盘事件"

# 测试键盘事件
keyboard_events = [
    {"type": "keydown", "key": "Enter"},
    {"type": "keydown", "key": "Escape"},
    {"type": "keydown", "key": "s", "ctrl": True},
    {"type": "keydown", "key": "a", "shift": True},
    {"type": "keydown", "key": "Tab", "alt": True},
    {"type": "keydown", "key": "F5"},
    {"type": "keydown", "key": "A"},
    {"type": "keyup", "key": "A"}
]

for event in keyboard_events:
    print(handle_keyboard_event(event))

# 示例 3：窗口事件处理
print("\n[示例 3] 窗口事件处理：\n")

def handle_window_event(event):
    """处理窗口事件"""
    match event:
        case {"type": "resize", "width": w, "height": h}:
            return f"🪟 窗口调整大小: {w}x{h}"
        case {"type": "move", "x": x, "y": y}:
            return f"🪟 窗口移动到: ({x}, {y})"
        case {"type": "minimize"}:
            return "🪟 窗口最小化"
        case {"type": "maximize"}:
            return "🪟 窗口最大化"
        case {"type": "close"}:
            return "🪟 窗口关闭"
        case {"type": "focus", "gained": True}:
            return "🪟 窗口获得焦点"
        case {"type": "focus", "gained": False}:
            return "🪟 窗口失去焦点"
        case _:
            return "❓ 未知窗口事件"

# 测试窗口事件
window_events = [
    {"type": "resize", "width": 1024, "height": 768},
    {"type": "move", "x": 100, "y": 100},
    {"type": "minimize"},
    {"type": "maximize"},
    {"type": "focus", "gained": True},
    {"type": "focus", "gained": False},
    {"type": "close"}
]

for event in window_events:
    print(handle_window_event(event))

# 示例 4：用户行为事件（带上下文）
print("\n[示例 4] 用户行为事件（带上下文信息）：\n")

def handle_user_action(event):
    """处理用户行为事件"""
    match event:
        case {"action": "login", "user_id": uid, "timestamp": ts}:
            return f"🔐 用户 {uid} 登录（时间: {ts}）"
        case {"action": "logout", "user_id": uid, "session_duration": duration}:
            return f"🔐 用户 {uid} 登出（会话时长: {duration}秒）"
        case {"action": "purchase", "user_id": uid, "item": item, "price": price}:
            return f"🛒 用户 {uid} 购买 {item}（价格: ${price}）"
        case {"action": "search", "query": query, "results": count}:
            return f"🔍 搜索 '{query}'，找到 {count} 个结果"
        case {"action": "share", "content_id": cid, "platform": platform}:
            return f"📤 分享内容 {cid} 到 {platform}"
        case {"action": "comment", "post_id": pid, "text": text}:
            preview = text[:30] + "..." if len(text) > 30 else text
            return f"💬 在帖子 {pid} 评论: {preview}"
        case _:
            return "❓ 未知用户行为"

# 测试用户行为事件
user_actions = [
    {"action": "login", "user_id": 12345, "timestamp": "2023-06-15T10:30:00Z"},
    {"action": "logout", "user_id": 12345, "session_duration": 3600},
    {"action": "purchase", "user_id": 12345, "item": "Premium Plan", "price": 9.99},
    {"action": "search", "query": "Python tutorials", "results": 156},
    {"action": "share", "content_id": "post-789", "platform": "twitter"},
    {"action": "comment", "post_id": 456, "text": "This is a great article! Thanks for sharing."}
]

for action in user_actions:
    print(handle_user_action(action))

# 示例 5：通知事件处理
print("\n[示例 5] 系统通知事件：\n")

def handle_notification_event(event):
    """处理通知事件"""
    match event:
        case {"level": "info", "message": msg, "timestamp": ts}:
            return f"ℹ️  [{ts}] {msg}"
        case {"level": "warning", "message": msg, "source": src}:
            return f"⚠️  [{src}] {msg}"
        case {"level": "error", "message": msg, "code": code, "details": details}:
            return f"❌ 错误 {code}: {msg}\n   详情: {details}"
        case {"level": "success", "message": msg}:
            return f"✅ {msg}"
        case _:
            return "❓ 未知通知"

# 测试通知事件
notifications = [
    {"level": "info", "message": "系统启动完成", "timestamp": "10:30:00"},
    {"level": "warning", "message": "磁盘空间不足", "source": "storage-monitor"},
    {
        "level": "error",
        "message": "数据库连接失败",
        "code": "DB_CONN_001",
        "details": "Connection timeout after 30 seconds"
    },
    {"level": "success", "message": "备份完成"}
]

for notif in notifications:
    print(handle_notification_event(notif))
    print()

# 示例 6：综合事件分发器
print("[示例 6] 综合事件分发器：\n")

class EventDispatcher:
    """事件分发器"""
    
    def dispatch(self, event):
        """根据事件类型分发到相应的处理器"""
        match event:
            case {"category": "mouse", **data}:
                return ("mouse", handle_mouse_event(data))
            case {"category": "keyboard", **data}:
                return ("keyboard", handle_keyboard_event(data))
            case {"category": "window", **data}:
                return ("window", handle_window_event(data))
            case {"category": "user", **data}:
                return ("user", handle_user_action(data))
            case {"category": "notification", **data}:
                return ("notification", handle_notification_event(data))
            case _:
                return ("unknown", "未知事件类别")

# 测试事件分发
dispatcher = EventDispatcher()

mixed_events = [
    {"category": "mouse", "type": "click", "button": "left", "x": 100, "y": 200},
    {"category": "keyboard", "type": "keydown", "key": "s", "ctrl": True},
    {"category": "window", "type": "resize", "width": 800, "height": 600},
    {"category": "user", "action": "login", "user_id": 999, "timestamp": "12:00:00"},
    {"category": "notification", "level": "success", "message": "操作完成"}
]

for event in mixed_events:
    category, result = dispatcher.dispatch(event)
    print(f"[{category.upper()}] {result}")

print("\n💡 总结：match/case 是实现事件驱动系统的理想工具")

