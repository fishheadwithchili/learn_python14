多版本 Python 环境与虚拟环境指南（Windows 优先）

多版本共存
- Windows 推荐使用 Python Launcher（官方安装器自带）：
  - 查看可用版本：`py -0p`
  - 指定版本运行：`py -3.10 -V`、`py -3.12 -m pip --version`
- 也可选用 pyenv-win（可选）：https://github.com/pyenv-win/pyenv-win
- macOS/Linux：建议 `pyenv` 或包管理器（brew/apt/dnf）安装多个 3.x 版本。

为每个版本创建独立虚拟环境
- 示例（Windows, 使用 Launcher）：
  - 创建：`py -3.12 -m venv .venv312`
  - 激活（PowerShell）：`./.venv312/Scripts/Activate.ps1`
  - 升级 pip：`python -m pip install -U pip`

按版本运行示例
- v3_8 示例：`py -3.8 curriculum/v3_8/examples/walrus_log_filter.py`
- v3_10 示例：`py -3.10 curriculum/v3_10/examples/match_ast_router.py`

故障排查
- 无法选择版本：确认已安装对应大版本；在 Windows “应用与功能” 检查并勾选“为所有用户安装”。
- `importlib.metadata` 等模块不存在：确认使用的 Python 版本是否满足示例要求。


