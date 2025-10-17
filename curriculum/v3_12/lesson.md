Python 3.12 要点（相对 3.11 的增量）

1) 类型参数新语法（PEP 695）
- `class Box[T]: ...`、`def f[T](x: T) -> T:`，原生语法定义泛型类型与函数。
- 示例：`examples/typing_typeparams_basics.py`

2) f-string 语法正式化（PEP 701）
- 更可靠的解析与嵌套，避免以往边缘情况的解析差异。
- 示例：`examples/fstring_advanced.py`

3) 低开销解释器监控 API（PEP 669 `sys.monitoring`）
- 事件订阅/回调，适用于性能分析、调试器与覆盖率工具构建。
- 示例：`examples/sys_monitoring_trace.py`

4) typing 增强
- `TypedDict` for **kwargs（PEP 692）、`typing.override`（PEP 698）。
- 示例：`examples/typed_kwargs.py`, `examples/typing_override_rules.py`

5) 生态与兼容
- 正式移除 `distutils`，打包生态全面转向 `pyproject.toml` 与构建后端。

练习建议（exercises/）
- 将 3.11 的泛型类改写为 PEP 695 语法；
- 编写一个最小 `sys.monitoring` 订阅器并记录函数调用次数；
- 使用 `TypedDict` 描述 `**kwargs` 并配合静态检查。


