Python 3.10 要点（相对 3.7/3.8/3.9 的增量）

1) 结构化模式匹配 `match/case`（PEP 634/635/636）
- 作用：对序列、映射、类实例（具名属性）进行结构匹配，比 if/elif 链更清晰。
- 能力：守卫（`case pattern if cond`）、序列/字面量/映射/类模式、通配 `_`。
- 示例：`examples/match_ast_router.py`

2) 联合类型简写 `X | Y`（PEP 604）
- 作用：代替 `typing.Union[X, Y]`，更直观，提高注解可读性。
- 示例：`examples/typing_union_api.py`

3) `ParamSpec`（PEP 612）
- 作用：为装饰器/高阶函数精确保留被包装函数的参数签名类型，避免 `*args/**kwargs` 丢失类型信息。
- 示例：`examples/paramspec_decorators.py`

4) `zip(strict=True)`（PEP 618）
- 作用：当输入可迭代长度不一致时抛出 `ValueError`，避免静默截断。
- 示例：`examples/zip_strict_csv.py`

练习建议（exercises/）
- 用 `match` 重写命令解析或 AST 访问器；
- 将现有装饰器改为使用 `ParamSpec` 保留参数类型；
- 用 `X | Y` 改写旧的 `Union[...]` 注解；
- 为数据对齐流程添加 `zip(strict=True)` 校验并处理异常。

注意事项
- `match` 不等同于正则匹配；注意类模式需定义属性/`__match_args__`。
- 在公共 API 中逐步引入 `|` 与 `ParamSpec` 时，确认静态检查工具版本（mypy/pyright）。


