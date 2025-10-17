Python 3.13 要点（前沿与迭代）

1) 可选“无 GIL”自由线程构建（PEP 703，实验/预览）
- 目标：去除全局解释器锁以提升多线程 CPU 绑定任务的伸缩性。
- 现状：作为可选构建提供，生态兼容性与 C 扩展适配仍在推进中。
- 示例/文档：`examples/nogil_readme.md`, `examples/threading_cpu_bound_compare.py`

2) 持续的标准库与 typing 演进
- 关注发行说明中的 API 行为差异与弃用计划，维持跨版本兼容。

练习建议（exercises/）
- 在常规构建对比“无 GIL”构建的线程扩展性（如果可用）；
- 审视项目依赖的 C 扩展兼容性清单并记录风险。


