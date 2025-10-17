Python 3.11 要点（相对 3.10 的增量）

1) ExceptionGroup 与 `except*`（PEP 654）
- 作用：并发/批处理场景下聚合多个异常，并以模式拆分捕获。
- 示例：`examples/exception_group_scraper.py`

2) `tomllib`（PEP 680）
- 作用：标准库读 TOML（只读）；替代第三方的最小需求，适合配置加载。
- 示例：`examples/tomllib_config.py`

3) 类型系统增强
- `typing.Self`（PEP 673）：流式 API/构建器模式返回自身类型。
- 可变参数泛型（PEP 646）：`TypeVarTuple`/`Unpack` 支持可变长度参数/元组形状。
- 示例：`examples/typing_self_fluent.py`, `examples/typing_variadic_matrix.py`

4) `asyncio.TaskGroup`
- 结构化并发与协作式取消；异常冒泡成组，结合 `except*` 使用。
- 示例：`examples/asyncio_taskgroup_cancellation.py`

5) 性能与调试
- 解释器显著提速；细粒度回溯位置（PEP 657）提供更准确的错误定位。

练习建议（exercises/）
- 用 `TaskGroup` 并发抓取多个 URL，演示单个失败导致的成组异常处理；
- 将流式 API 标注为 `Self` 并保证链式调用类型正确；
- 用 `TypeVarTuple` 给变长元组处理函数添加注解，并保持运行通过。


