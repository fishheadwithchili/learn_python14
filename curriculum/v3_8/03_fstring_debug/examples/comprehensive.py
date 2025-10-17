"""
f-string 调试语法实战示例：用户行为数据分析

业务场景：
分析电商网站的用户行为数据，计算关键指标：
1. 用户活跃度统计
2. 转化率计算
3. 异常行为检测

演示 f"{var=}" 如何简化调试和日志输出。

运行要求：Python >= 3.8
"""

from datetime import datetime, timedelta
from typing import List, Dict
import random

# ============ 模拟用户行为数据 ============

def generate_sample_data() -> List[Dict]:
    """生成模拟的用户行为数据"""
    actions = ['view', 'click', 'add_cart', 'purchase']
    data = []
    
    for user_id in range(1, 21):
        num_actions = random.randint(1, 10)
        for _ in range(num_actions):
            data.append({
                'user_id': user_id,
                'action': random.choice(actions),
                'timestamp': datetime.now() - timedelta(days=random.randint(0, 7)),
                'value': random.randint(10, 500) if random.random() > 0.7 else 0
            })
    
    return data


# ============ 数据分析函数 ============

def analyze_user_behavior(data: List[Dict]) -> Dict:
    """分析用户行为数据"""
    
    print("=" * 60)
    print("开始数据分析...")
    print("=" * 60)
    
    # 步骤 1: 数据概览
    total_records = len(data)
    print(f"\n[步骤 1] 数据加载")
    print(f"{total_records=}")  # 自动显示变量名和值
    
    # 步骤 2: 用户去重
    unique_users = len(set(record['user_id'] for record in data))
    print(f"\n[步骤 2] 用户统计")
    print(f"{unique_users=}")
    print(f"{total_records / unique_users=:.2f}")  # 平均每用户行为数
    
    # 步骤 3: 行为类型分布
    print(f"\n[步骤 3] 行为分布")
    action_counts = {}
    for record in data:
        action = record['action']
        action_counts[action] = action_counts.get(action, 0) + 1
    
    # 使用 f"{var=}" 快速输出多个指标
    views = action_counts.get('view', 0)
    clicks = action_counts.get('click', 0)
    add_carts = action_counts.get('add_cart', 0)
    purchases = action_counts.get('purchase', 0)
    
    print(f"{views=}, {clicks=}, {add_carts=}, {purchases=}")
    
    # 步骤 4: 转化率计算
    print(f"\n[步骤 4] 转化率分析")
    if views > 0:
        click_rate = clicks / views * 100
        print(f"{click_rate=:.2f}%")  # 格式化输出
        
        if clicks > 0:
            cart_rate = add_carts / clicks * 100
            print(f"{cart_rate=:.2f}%")
            
            if add_carts > 0:
                purchase_rate = purchases / add_carts * 100
                print(f"{purchase_rate=:.2f}%")
    
    # 步骤 5: 异常检测
    print(f"\n[步骤 5] 异常检测")
    high_value_actions = [r for r in data if r['value'] > 300]
    suspicious_count = len(high_value_actions)
    
    # 复杂表达式也能直接输出
    print(f"{suspicious_count=}")
    print(f"{suspicious_count / total_records * 100=:.1f}% (占比)")
    
    if suspicious_count > 0:
        max_value = max(r['value'] for r in high_value_actions)
        min_value = min(r['value'] for r in high_value_actions)
        avg_value = sum(r['value'] for r in high_value_actions) / suspicious_count
        
        # 一行输出多个统计量
        print(f"高价值行为: {max_value=}, {min_value=}, {avg_value=:.2f}")
    
    # 步骤 6: 时间分布
    print(f"\n[步骤 6] 时间分析")
    timestamps = [r['timestamp'] for r in data]
    earliest = min(timestamps)
    latest = max(timestamps)
    time_span = (latest - earliest).days
    
    # datetime 对象也能直接输出（会显示 repr）
    print(f"{earliest=}")
    print(f"{latest=}")
    print(f"{time_span=} 天")
    
    return {
        'total_records': total_records,
        'unique_users': unique_users,
        'conversion_rate': purchase_rate if views > 0 else 0,
        'suspicious_count': suspicious_count
    }


# ============ 异常处理中的应用 ============

def safe_divide(a: float, b: float) -> float:
    """演示在异常处理中使用调试语法"""
    try:
        result = a / b
        print(f"{a=}, {b=}, {result=}")
        return result
    except ZeroDivisionError as e:
        # 异常时输出详细上下文
        print(f"\n❌ 除零错误!")
        print(f"{a=}, {b=}")  # 快速定位问题
        print(f"{type(e)=}, {str(e)=}")
        return float('inf')


# ============ 主函数 ============

def main():
    # 生成测试数据
    random.seed(42)  # 固定随机种子以便复现
    data = generate_sample_data()
    
    # 分析数据
    results = analyze_user_behavior(data)
    
    # 输出汇总报告
    print("\n" + "=" * 60)
    print("分析结果汇总")
    print("=" * 60)
    
    # 使用 !r 和 !s 转换符
    summary = f"共 {results['total_records']} 条记录"
    print(f"{summary=!s}")  # 使用 str() 表示（无引号）
    
    # 最终指标
    print(f"\n关键指标:")
    print(f"  {results['unique_users']=}")
    print(f"  {results['conversion_rate']=:.2f}%")
    print(f"  {results['suspicious_count']=}")
    
    # 演示除零处理
    print("\n" + "=" * 60)
    print("除法运算测试")
    print("=" * 60)
    safe_divide(10, 2)
    safe_divide(10, 0)  # 触发异常
    
    print("\n✅ 分析完成!")


if __name__ == "__main__":
    main()

