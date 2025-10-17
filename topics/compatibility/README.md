兼容性与弃用/移除清单

建议：
- 跟踪 `Deprecated`/`PendingDeprecation` 警告；
- 优先替换：`distutils` → setuptools/pep517 后端；`pkg_resources` → `importlib.resources`；
- 用 CI 针对多版本测试，结合 `python_requires` 和类型检查（不同解释器环境）。


