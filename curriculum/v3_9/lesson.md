Python 3.9 要点（相对 3.7/3.8 的增量）

1) 字典合并/更新运算符（PEP 584）
- `a | b` 生成新字典、`a |= b` 就地更新；对配置分层合并直观。
- 示例：`examples/dict_merge_configs.py`

2) 内置泛型（PEP 585）与 `typing.Annotated`（PEP 593）
- 可写 `list[int]`、`dict[str, int]`，替代 `typing.List[int]` 等。
- `Annotated[T, meta...]` 为类型附加元数据（校验/文档/约束）。
- 示例：`examples/typing_generics_basics.py`, `examples/typing_annotated_validation.py`

3) 字符串新方法（PEP 616）
- `removeprefix` / `removesuffix` 简化前后缀处理。
- 示例：`examples/str_prefix_suffix.py`

4) `zoneinfo`（IANA 时区数据库）
- 标准库内置时区支持，替代第三方基础用法。
- 示例：`examples/zoneinfo_basics.py`

练习建议（exercises/）
- 将多层配置按优先级合并，比较 `|` 与 `dict.update` 的不同；
- 将旧式 `typing.List` 注解替换为内置泛型；
- 用 `Annotated` 为参数添加“范围/单位”等元数据；
- 实现一个按时区显示当地时间的小工具。


