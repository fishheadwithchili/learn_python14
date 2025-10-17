静态类型检查（mypy / pyright）最小指引

建议：
- 为示例分离配置，避免学习者环境差异影响：
  - mypy：`mypy.ini` 指定 `python_version = 3.12`（按需调整）；
  - pyright：`pyproject.toml` 或 `pyrightconfig.json` 指定 `pythonVersion`。
- 常见提示：
  - 使用 3.9+ 泛型（`list[int]`），替代 `typing.List[int]`；
  - 逐步启用严格选项，结合 CI 执行。


