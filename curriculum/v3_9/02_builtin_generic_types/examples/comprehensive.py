"""
综合示例：数据处理管道

场景：构建一个完整的数据处理管道，包括数据加载、转换、验证、
聚合和导出，展示内置泛型类型在实际应用中的综合运用。
"""

from dataclasses import dataclass, field
from typing import TypeVar, Callable

T = TypeVar('T')

# ============= 数据模型 =============

@dataclass
class Record:
    """数据记录"""
    id: int
    category: str
    value: float
    tags: list[str]
    metadata: dict[str, str]
    
    def has_tag(self, tag: str) -> bool:
        """检查是否包含标签"""
        return tag in self.tags


@dataclass
class ProcessingStats:
    """处理统计"""
    total_records: int = 0
    processed: int = 0
    errors: int = 0
    warnings: list[str] = field(default_factory=list)
    
    def success_rate(self) -> float:
        """成功率"""
        return self.processed / self.total_records if self.total_records > 0 else 0.0


# ============= 数据管道 =============

class DataPipeline:
    """数据处理管道"""
    
    _data: list[Record]
    _filters: list[Callable[[Record], bool]]
    _transformers: list[Callable[[Record], Record]]
    _cache: dict[str, list[Record]]
    stats: ProcessingStats
    
    def __init__(self):
        self._data = []
        self._filters = []
        self._transformers = []
        self._cache = {}
        self.stats = ProcessingStats()
    
    def load(self, records: list[Record]) -> 'DataPipeline':
        """加载数据"""
        self._data = records
        self.stats.total_records = len(records)
        print(f"✅ 加载了 {len(records)} 条记录")
        return self
    
    def filter(self, predicate: Callable[[Record], bool]) -> 'DataPipeline':
        """添加过滤器"""
        self._filters.append(predicate)
        return self
    
    def transform(self, transformer: Callable[[Record], Record]) -> 'DataPipeline':
        """添加转换器"""
        self._transformers.append(transformer)
        return self
    
    def execute(self) -> list[Record]:
        """执行管道"""
        result: list[Record] = self._data.copy()
        
        # 应用过滤器
        for filter_func in self._filters:
            result = [r for r in result if filter_func(r)]
        
        # 应用转换器
        for transform_func in self._transformers:
            try:
                result = [transform_func(r) for r in result]
                self.stats.processed = len(result)
            except Exception as e:
                self.stats.errors += 1
                self.stats.warnings.append(f"转换错误: {e}")
        
        return result
    
    def group_by(self, key_func: Callable[[Record], str]) -> dict[str, list[Record]]:
        """按键函数分组"""
        result: dict[str, list[Record]] = {}
        
        for record in self._data:
            key = key_func(record)
            result.setdefault(key, []).append(record)
        
        return result
    
    def aggregate(
        self,
        group_key: Callable[[Record], str],
        agg_func: Callable[[list[Record]], float]
    ) -> dict[str, float]:
        """聚合数据"""
        groups = self.group_by(group_key)
        return {key: agg_func(records) for key, records in groups.items()}
    
    def cache_result(self, key: str, data: list[Record]) -> None:
        """缓存结果"""
        self._cache[key] = data
    
    def get_cache(self, key: str) -> list[Record] | None:
        """获取缓存"""
        return self._cache.get(key)


# ============= 数据验证 =============

class DataValidator:
    """数据验证器"""
    
    _rules: list[tuple[str, Callable[[Record], bool]]]
    
    def __init__(self):
        self._rules = []
    
    def add_rule(self, name: str, rule: Callable[[Record], bool]) -> 'DataValidator':
        """添加验证规则"""
        self._rules.append((name, rule))
        return self
    
    def validate(self, records: list[Record]) -> dict[str, list[int]]:
        """验证数据，返回每个规则的违规记录ID"""
        violations: dict[str, list[int]] = {}
        
        for name, rule in self._rules:
            violated_ids = [r.id for r in records if not rule(r)]
            if violated_ids:
                violations[name] = violated_ids
        
        return violations


# ============= 辅助函数 =============

def create_sample_data() -> list[Record]:
    """创建示例数据"""
    return [
        Record(1, "A", 100.0, ["important", "urgent"], {"source": "system1"}),
        Record(2, "B", 50.0, ["normal"], {"source": "system2"}),
        Record(3, "A", 150.0, ["important"], {"source": "system1"}),
        Record(4, "C", 75.0, ["urgent"], {"source": "system3"}),
        Record(5, "B", 200.0, ["important", "normal"], {"source": "system2"}),
        Record(6, "A", 25.0, ["normal"], {"source": "system1"}),
        Record(7, "C", 300.0, ["important", "urgent"], {"source": "system3"}),
    ]


# ============= 主程序 =============

def main():
    print("=" * 70)
    print("综合示例：数据处理管道")
    print("=" * 70)
    
    # 创建示例数据
    data = create_sample_data()
    
    # 场景 1：数据加载和基本处理
    print("\n[场景 1] 数据加载和基本处理\n")
    
    pipeline = DataPipeline()
    pipeline.load(data)
    
    print(f"数据预览（前3条）:")
    for record in data[:3]:
        print(f"  - ID:{record.id}, 类别:{record.category}, 值:{record.value}, 标签:{record.tags}")
    
    # 场景 2：过滤和转换
    print("\n[场景 2] 过滤和转换\n")
    
    # 过滤：只保留重要的记录
    filtered_pipeline = (
        DataPipeline()
        .load(data)
        .filter(lambda r: r.has_tag("important"))
        .filter(lambda r: r.value > 50)
    )
    
    filtered_data = filtered_pipeline.execute()
    print(f"过滤后记录数: {len(filtered_data)}")
    print(f"过滤条件: 包含'important'标签 且 值>50")
    
    for record in filtered_data:
        print(f"  - ID:{record.id}, 值:{record.value}")
    
    # 场景 3：数据转换
    print("\n[场景 3] 数据转换\n")
    
    # 转换：将值加倍
    transformed_pipeline = (
        DataPipeline()
        .load(data)
        .transform(lambda r: Record(
            r.id, r.category, r.value * 2, r.tags, r.metadata
        ))
    )
    
    transformed_data = transformed_pipeline.execute()
    
    print("原始值 vs 转换后:")
    for i in range(min(3, len(data))):
        print(f"  ID:{data[i].id} - 原始:{data[i].value:.1f}, 转换后:{transformed_data[i].value:.1f}")
    
    # 场景 4：分组和聚合
    print("\n[场景 4] 分组和聚合\n")
    
    # 按类别分组
    pipeline_for_grouping = DataPipeline().load(data)
    groups = pipeline_for_grouping.group_by(lambda r: r.category)
    
    print("按类别分组:")
    for category, records in groups.items():
        print(f"  类别 {category}: {len(records)} 条记录")
    
    # 按类别聚合（计算平均值）
    avg_by_category = pipeline_for_grouping.aggregate(
        group_key=lambda r: r.category,
        agg_func=lambda records: sum(r.value for r in records) / len(records)
    )
    
    print("\n按类别平均值:")
    for category, avg in avg_by_category.items():
        print(f"  类别 {category}: {avg:.2f}")
    
    # 场景 5：数据验证
    print("\n[场景 5] 数据验证\n")
    
    validator = (
        DataValidator()
        .add_rule("value_positive", lambda r: r.value > 0)
        .add_rule("category_valid", lambda r: r.category in ["A", "B", "C"])
        .add_rule("has_tags", lambda r: len(r.tags) > 0)
    )
    
    violations = validator.validate(data)
    
    if violations:
        print("发现验证错误:")
        for rule, violated_ids in violations.items():
            print(f"  规则 '{rule}' 违规: {violated_ids}")
    else:
        print("✅ 所有数据验证通过")
    
    # 场景 6：复杂查询
    print("\n[场景 6] 复杂查询（多条件过滤 + 排序）\n")
    
    complex_query = (
        DataPipeline()
        .load(data)
        .filter(lambda r: r.category in ["A", "B"])
        .filter(lambda r: r.has_tag("important") or r.has_tag("urgent"))
    )
    
    query_result = complex_query.execute()
    # 手动排序（按值降序）
    query_result_sorted = sorted(query_result, key=lambda r: r.value, reverse=True)
    
    print(f"查询结果（前3条）:")
    for record in query_result_sorted[:3]:
        print(f"  - ID:{record.id}, 类别:{record.category}, 值:{record.value}, 标签:{record.tags}")
    
    # 场景 7：统计信息
    print("\n[场景 7] 处理统计\n")
    
    print(f"总记录数: {pipeline.stats.total_records}")
    print(f"成功率: {pipeline.stats.success_rate():.1%}")
    if pipeline.stats.warnings:
        print(f"警告: {pipeline.stats.warnings}")
    
    # 场景 8：导出摘要
    print("\n[场景 8] 数据摘要\n")
    
    summary: dict[str, dict[str, float | int]] = {}
    
    for category, records in groups.items():
        summary[category] = {
            "count": len(records),
            "total": sum(r.value for r in records),
            "average": sum(r.value for r in records) / len(records),
            "max": max(r.value for r in records),
            "min": min(r.value for r in records)
        }
    
    print("类别摘要:")
    for category, stats in summary.items():
        print(f"  类别 {category}:")
        print(f"    数量: {stats['count']}")
        print(f"    总和: {stats['total']:.2f}")
        print(f"    平均: {stats['average']:.2f}")
        print(f"    最大: {stats['max']:.2f}")
        print(f"    最小: {stats['min']:.2f}")
    
    # 总结
    print("\n" + "=" * 70)
    print("💡 总结")
    print("=" * 70)
    print()
    print("内置泛型类型的综合应用：")
    print("  ✅ 数据模型定义：dataclass + list[str], dict[str, str]")
    print("  ✅ 管道处理：list[Record], Callable[[Record], bool]")
    print("  ✅ 分组聚合：dict[str, list[Record]]")
    print("  ✅ 验证规则：list[tuple[str, Callable]]")
    print("  ✅ 统计摘要：dict[str, dict[str, float | int]]")
    print()
    print("适用场景：")
    print("  • ETL 数据管道")
    print("  • 日志分析系统")
    print("  • 数据验证框架")
    print("  • 报表生成系统")
    print("  • API 数据处理")


if __name__ == "__main__":
    main()

