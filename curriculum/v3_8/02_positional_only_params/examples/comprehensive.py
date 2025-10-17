"""
Positional-only Parameters 实战示例：数据库连接池 API 设计

业务场景：
设计一个通用数据库连接池库的公共 API，需要：
1. 支持多种数据库类型（MySQL、PostgreSQL、SQLite）
2. API 演化时保持向后兼容
3. 避免参数名与配置项冲突

演示仅位置参数如何保护 API 稳定性。

运行要求：Python >= 3.8
"""

from typing import Optional, Dict, Any
from dataclasses import dataclass

# ============ 模拟的数据库连接类 ============

@dataclass
class DatabaseConnection:
    """模拟的数据库连接对象"""
    db_type: str
    host: str
    port: int
    config: Dict[str, Any]
    
    def execute(self, query: str):
        return f"[{self.db_type}] Executing: {query}"


# ============ API v1.0 - 早期设计（有缺陷） ============

def create_connection_v1(type, host, port=3306, **options):
    """
    早期版本 - 没有使用仅位置参数
    
    问题：
    1. 如果用户使用 create_connection_v1(type='mysql', host='localhost')
       后续无法重命名 'type' 为 'db_type' 而不破坏兼容性
    2. 如果 options 中有 'type' 或 'host' 键，会导致冲突
    """
    return DatabaseConnection(type, host, port, options)


# ============ API v2.0 - 使用仅位置参数改进 ============

def create_connection_v2(db_type, /, host, port=3306, **options):
    """
    改进版本 - 使用 / 保护 db_type 参数
    
    优势：
    1. db_type 必须按位置传递，未来可以重命名而不影响用户代码
    2. host 和 port 依然可以用关键字传递（提高可读性）
    3. options 可以安全地包含 'db_type' 键
    """
    # options 可以包含数据库特定的配置
    if 'db_type' in options:
        options['database_type'] = options.pop('db_type')  # 重命名避免冲突
    
    return DatabaseConnection(db_type, host, port, options)


# ============ API v3.0 - 完整的参数分层设计 ============

def create_connection_v3(
    db_type,           # 仅位置：核心类型参数
    /,
    host,              # 位置或关键字：常用参数
    port=None,         # 位置或关键字：带默认值
    *,                 # 以下仅关键字
    timeout=30,        # 仅关键字：可选配置
    pool_size=10,      # 仅关键字：连接池配置
    **options          # 其他数据库特定选项
):
    """
    最佳实践版本 - 清晰的参数分层
    
    参数说明：
    - db_type: 必须按位置传递（'mysql', 'postgres', 'sqlite'）
    - host: 可以位置或关键字传递
    - port: 默认根据数据库类型自动选择
    - timeout: 仅关键字，避免位置错乱
    - pool_size: 仅关键字
    - **options: 数据库特定的额外配置
    """
    # 自动推断默认端口
    if port is None:
        default_ports = {'mysql': 3306, 'postgres': 5432, 'sqlite': 0}
        port = default_ports.get(db_type, 5432)
    
    # 合并配置
    config = {
        'timeout': timeout,
        'pool_size': pool_size,
        **options
    }
    
    return DatabaseConnection(db_type, host, port, config)


# ============ 实际使用演示 ============

def demo_api_evolution():
    """演示 API 演化过程"""
    
    print("=" * 60)
    print("数据库连接池 API 演化示例")
    print("=" * 60)
    
    # ===== v1.0 的问题 =====
    print("\n[v1.0 - 有问题的设计]")
    conn1 = create_connection_v1('mysql', 'localhost', 3306)
    print(f"✓ 创建连接: {conn1.db_type}@{conn1.host}:{conn1.port}")
    
    # 用户可能这样调用（使用关键字参数）
    conn1_kw = create_connection_v1(type='postgres', host='db.example.com', port=5432)
    print(f"✓ 关键字调用: {conn1_kw.db_type}@{conn1_kw.host}:{conn1_kw.port}")
    print("⚠ 问题：如果未来想把 'type' 改为 'db_type'，会破坏用户代码！")
    
    # ===== v2.0 的改进 =====
    print("\n[v2.0 - 使用仅位置参数]")
    conn2 = create_connection_v2('mysql', host='localhost', port=3306)
    print(f"✓ 创建连接: {conn2.db_type}@{conn2.host}:{conn2.port}")
    
    # 现在 db_type 不能用关键字传递
    try:
        create_connection_v2(db_type='mysql', host='localhost')
    except TypeError as e:
        print(f"✗ 尝试关键字传递 db_type: TypeError")
        print(f"  (这是预期行为，保护了参数名）")
    
    # options 可以包含 db_type 键而不冲突
    conn2_opt = create_connection_v2(
        'postgres', 
        host='db.example.com', 
        db_type='重要：这个是 options 中的 db_type',
        charset='utf8'
    )
    print(f"✓ options 中可以安全使用 'db_type' 键: {conn2_opt.config}")
    
    # ===== v3.0 的最佳实践 =====
    print("\n[v3.0 - 完整的参数分层]")
    
    # 简洁的调用
    conn3_simple = create_connection_v3('mysql', 'localhost')
    print(f"✓ 简洁调用（自动端口）: {conn3_simple.db_type}@{conn3_simple.host}:{conn3_simple.port}")
    
    # 完整的调用
    conn3_full = create_connection_v3(
        'postgres',                  # 仅位置
        'db.example.com',            # 位置或关键字
        5432,                        # 位置或关键字
        timeout=60,                  # 仅关键字
        pool_size=20,                # 仅关键字
        ssl=True,                    # options
        application_name='my_app'    # options
    )
    print(f"✓ 完整调用: {conn3_full.db_type}@{conn3_full.host}:{conn3_full.port}")
    print(f"  配置: {conn3_full.config}")
    
    print("\n" + "=" * 60)
    print("总结：仅位置参数让 API 演化更安全！")
    print("=" * 60)


if __name__ == "__main__":
    demo_api_evolution()

