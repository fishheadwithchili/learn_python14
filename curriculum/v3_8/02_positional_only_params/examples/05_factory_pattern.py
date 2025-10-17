"""
场景 5：工厂函数/构造器模式

应用：对象构造函数第一个参数通常是类型或标识符
"""

from typing import Dict, Any
from dataclasses import dataclass

print("=" * 60)
print("工厂模式：固定类型参数")
print("=" * 60)

# 模拟不同类型的数据库连接
@dataclass
class MySQLConnection:
    host: str
    port: int
    database: str
    
    def connect(self):
        return f"MySQL连接: {self.host}:{self.port}/{self.database}"

@dataclass
class PostgresConnection:
    host: str
    port: int
    database: str
    
    def connect(self):
        return f"PostgreSQL连接: {self.host}:{self.port}/{self.database}"

@dataclass
class SQLiteConnection:
    path: str
    
    def connect(self):
        return f"SQLite连接: {self.path}"

# ✅ 使用仅位置参数的工厂函数
def create_connection(db_type, /, host=None, port=None, database=None, path=None, **options):
    """
    数据库连接工厂
    
    参数:
        db_type: 数据库类型（仅位置，避免混淆）
        host, port, database: 网络数据库参数
        path: SQLite 数据库路径
        **options: 其他选项
    """
    if db_type == 'mysql':
        if not all([host, port, database]):
            raise ValueError("MySQL 需要 host, port, database")
        return MySQLConnection(host, port, database)
    
    elif db_type == 'postgres':
        if not all([host, port, database]):
            raise ValueError("PostgreSQL 需要 host, port, database")
        return PostgresConnection(host, port, database)
    
    elif db_type == 'sqlite':
        if not path:
            raise ValueError("SQLite 需要 path")
        return SQLiteConnection(path)
    
    else:
        raise ValueError(f"未知的数据库类型: {db_type}")

print("\n创建不同类型的连接：\n")

# db_type 必须位置传递，清晰明确
mysql_conn = create_connection('mysql', host='localhost', port=3306, database='myapp')
print(f"  {mysql_conn.connect()}")

postgres_conn = create_connection('postgres', host='db.example.com', port=5432, database='users')
print(f"  {postgres_conn.connect()}")

sqlite_conn = create_connection('sqlite', path='/data/app.db')
print(f"  {sqlite_conn.connect()}")

# 不能用关键字传递类型（避免混淆）
try:
    create_connection(db_type='mysql', host='localhost', port=3306, database='test')
except TypeError:
    print(f"  ✅ 正确阻止: db_type 必须位置传递")

print("\n" + "=" * 60)
print("HTTP 客户端工厂")
print("=" * 60)

class HTTPClient:
    def __init__(self, base_url: str, timeout: int = 30):
        self.base_url = base_url
        self.timeout = timeout
    
    def __repr__(self):
        return f"HTTPClient({self.base_url}, timeout={self.timeout})"

class WebSocketClient:
    def __init__(self, base_url: str, ping_interval: int = 30):
        self.base_url = base_url
        self.ping_interval = ping_interval
    
    def __repr__(self):
        return f"WebSocketClient({self.base_url}, ping_interval={self.ping_interval})"

def create_client(protocol, /, base_url, **config):
    """
    创建网络客户端
    
    参数:
        protocol: 协议类型（'http', 'ws'）- 仅位置
        base_url: 基础 URL
        **config: 协议特定配置
    """
    if protocol == 'http':
        timeout = config.get('timeout', 30)
        return HTTPClient(base_url, timeout)
    
    elif protocol == 'ws':
        ping_interval = config.get('ping_interval', 30)
        return WebSocketClient(base_url, ping_interval)
    
    else:
        raise ValueError(f"不支持的协议: {protocol}")

print("\n创建不同协议的客户端：\n")

http = create_client('http', 'https://api.example.com', timeout=60)
print(f"  {http}")

ws = create_client('ws', 'wss://realtime.example.com', ping_interval=15)
print(f"  {ws}")

print("\n" + "=" * 60)
print("日志记录器工厂")
print("=" * 60)

class ConsoleLogger:
    def __init__(self, level: str):
        self.level = level
    
    def log(self, message: str):
        return f"[{self.level}] {message}"

class FileLogger:
    def __init__(self, level: str, filepath: str):
        self.level = level
        self.filepath = filepath
    
    def log(self, message: str):
        return f"[{self.level}] → {self.filepath}: {message}"

def create_logger(logger_type, /, level='INFO', **config):
    """
    创建日志记录器
    
    参数:
        logger_type: 日志类型（'console', 'file'）- 仅位置
        level: 日志级别
        **config: 类型特定配置
    """
    if logger_type == 'console':
        return ConsoleLogger(level)
    
    elif logger_type == 'file':
        filepath = config.get('filepath', 'app.log')
        return FileLogger(level, filepath)
    
    else:
        raise ValueError(f"未知的日志类型: {logger_type}")

print("\n创建不同类型的日志器：\n")

console_logger = create_logger('console', level='DEBUG')
print(f"  {console_logger.log('Application started')}")

file_logger = create_logger('file', level='ERROR', filepath='/var/log/app.log')
print(f"  {file_logger.log('Critical error occurred')}")

print("\n" + "=" * 60)
print("优势总结")
print("=" * 60)

print("""
工厂模式中使用仅位置参数的优势：

✅ 类型参数位置固定，一眼就能看出创建什么对象
✅ 避免 create_connection(db_type='mysql', ...) 这种冗余写法
✅ 防止类型参数被误用为关键字参数
✅ API 更清晰：第一个参数永远是"类型"

对比：
  create_connection('mysql', ...)     # 清晰
  create_connection(db_type='mysql')  # 冗余，且可能与 options 冲突
""")

print("💡 总结：工厂函数的类型参数应该位置固定，提升 API 清晰度")

