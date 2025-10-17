"""
场景 6：回调函数接口标准化

应用：框架定义回调接口时固定前几个参数
"""

from typing import Callable, Any, Dict
import time

print("=" * 60)
print("事件处理器接口")
print("=" * 60)

# 事件系统
class EventBus:
    def __init__(self):
        self.handlers: Dict[str, list] = {}
    
    def register(self, event_type, handler, /, priority=0, **metadata):
        """
        注册事件处理器
        
        参数:
            event_type: 事件类型（仅位置）
            handler: 处理函数（仅位置）
            priority: 优先级
            **metadata: 处理器元数据
        """
        if event_type not in self.handlers:
            self.handlers[event_type] = []
        
        self.handlers[event_type].append({
            'handler': handler,
            'priority': priority,
            'metadata': metadata
        })
        
        # 按优先级排序
        self.handlers[event_type].sort(key=lambda x: x['priority'], reverse=True)
    
    def emit(self, event_type, data):
        """触发事件"""
        if event_type not in self.handlers:
            return
        
        for handler_info in self.handlers[event_type]:
            handler_info['handler'](data)

# 创建事件总线
bus = EventBus()

# 注册处理器
def on_user_login(data):
    print(f"  [处理器1] 用户登录: {data['username']}")

def on_user_login_log(data):
    print(f"  [处理器2] 记录日志: {data['username']} at {data['timestamp']}")

def on_user_login_notify(data):
    print(f"  [处理器3] 发送通知: 欢迎 {data['username']}")

print("\n注册事件处理器：\n")

# handler 参数不会与用户的回调函数参数冲突
bus.register('user.login', on_user_login, priority=10)
bus.register('user.login', on_user_login_log, priority=5, handler='metadata_value')  # handler 可以作为元数据
bus.register('user.login', on_user_login_notify, priority=1)

print("触发登录事件：\n")

bus.emit('user.login', {
    'username': 'alice',
    'timestamp': time.time()
})

print("\n" + "=" * 60)
print("HTTP 路由注册")
print("=" * 60)

class Router:
    def __init__(self):
        self.routes = []
    
    def route(self, path, handler, /, methods=None, **options):
        """
        注册路由
        
        参数:
            path: URL 路径（仅位置）
            handler: 处理函数（仅位置）
            methods: HTTP 方法列表
            **options: 路由选项（可以包含 'path', 'handler' 等键）
        """
        if methods is None:
            methods = ['GET']
        
        self.routes.append({
            'path': path,
            'handler': handler,
            'methods': methods,
            'options': options
        })
    
    def handle_request(self, path: str, method: str):
        """处理请求"""
        for route in self.routes:
            if route['path'] == path and method in route['methods']:
                return route['handler']()
        return "404 Not Found"

router = Router()

# 路由处理器
def home_handler():
    return "Welcome to Home"

def api_users_handler():
    return '{"users": ["alice", "bob"]}'

def dashboard_handler():
    return "Dashboard (Admin Only)"

print("\n注册路由：\n")

router.route('/', home_handler)
router.route('/api/users', api_users_handler, methods=['GET', 'POST'])
router.route('/dashboard', dashboard_handler, methods=['GET'], path='/admin/dashboard', auth_required=True)

print("处理请求：\n")
print(f"  GET /: {router.handle_request('/', 'GET')}")
print(f"  GET /api/users: {router.handle_request('/api/users', 'GET')}")
print(f"  POST /api/users: {router.handle_request('/api/users', 'POST')}")

print("\n" + "=" * 60)
print("插件系统")
print("=" * 60)

class PluginManager:
    def __init__(self):
        self.plugins = []
    
    def register_plugin(self, plugin_class, config, /, enabled=True, **metadata):
        """
        注册插件
        
        参数:
            plugin_class: 插件类（仅位置）
            config: 插件配置（仅位置）
            enabled: 是否启用
            **metadata: 插件元数据
        """
        plugin = {
            'class': plugin_class,
            'config': config,
            'enabled': enabled,
            'metadata': metadata,
            'instance': None
        }
        
        if enabled:
            plugin['instance'] = plugin_class(config)
        
        self.plugins.append(plugin)
    
    def load_plugins(self):
        """加载所有插件"""
        for plugin in self.plugins:
            if plugin['enabled'] and plugin['instance']:
                plugin['instance'].initialize()

# 示例插件
class CachePlugin:
    def __init__(self, config):
        self.config = config
    
    def initialize(self):
        print(f"  初始化缓存插件: {self.config}")

class LogPlugin:
    def __init__(self, config):
        self.config = config
    
    def initialize(self):
        print(f"  初始化日志插件: {self.config}")

pm = PluginManager()

print("\n注册插件：\n")

pm.register_plugin(CachePlugin, {'max_size': 1000}, enabled=True, author='Alice', version='1.0')
pm.register_plugin(LogPlugin, {'level': 'DEBUG'}, enabled=True, config='can_be_metadata')

print("加载插件：\n")
pm.load_plugins()

print("\n💡 总结：回调接口中仅位置参数确保核心参数固定，避免与回调内部参数冲突")

