# Python 3.7 → 3.14 增量学习项目

> 📚 系统化掌握 Python 3.8-3.14 每个版本的核心新特性

## 📋 项目概述

本项目面向已掌握 Python 3.7 的开发者，按 3.8→3.14 版本递进式学习关键语法、类型系统与标准库变化。

**特色**：
- ✅ **模块化结构**：每个特性独立目录，包含详细说明和多个示例
- ✅ **详尽场景说明**：每个功能提供 10 个实际应用场景
- ✅ **实用示例代码**：10-50 行的完整可运行示例
- ✅ **清单式学习**：系统化掌握每个版本的新特性
- ✅ **真实业务场景**：所有示例模拟实际开发中的使用场景

## 🎯 当前进度

```
Python 3.8  ████████████████████ 100% ✅ (5个特性，66个文件)
Python 3.9  ████████████████████ 100% ✅ (5个特性，66个文件)
Python 3.10 █████░░░░░░░░░░░░░░░  25% 🚧 (1/4个特性完成)
Python 3.11 ░░░░░░░░░░░░░░░░░░░░   0% ⏳
Python 3.12 ░░░░░░░░░░░░░░░░░░░░   0% ⏳
Python 3.13 ░░░░░░░░░░░░░░░░░░░░   0% ⏳
Python 3.14 ░░░░░░░░░░░░░░░░░░░░   0% ⏳

总进度：约 40% (145/368 文件)
```

## 🔧 环境配置

### Python 版本要求

本项目使用 **Python 3.14t (free-threading)** 进行开发和测试。

#### 安装步骤

1. **安装 Python 3.14t**
   - 项目包含安装包：`python-3.14.0-amd64.exe`
   - 安装时选择 **free-threading** 版本
   - 建议安装路径：`C:\Users\<用户名>\AppData\Local\Programs\Python\Python314`

2. **创建虚拟环境**
   ```bash
   # Windows PowerShell
   cd C:\Users\WDAGUtilityAccount\Desktop\comfyui_src\unsafe_project\learn_python14
   
   # 使用 Python 3.14t 创建虚拟环境
   python -m venv .venv314t
   
   # 激活虚拟环境
   .venv314t\Scripts\activate
   
   # 验证版本
   python --version
   # 应该显示：Python 3.14.0 (带 free-threading)
   ```

3. **PyCharm IDE 配置**
   - 打开项目：`File` → `Open` → 选择项目目录
   - 配置解释器：`File` → `Settings` → `Project` → `Python Interpreter`
   - 点击齿轮图标 → `Add Interpreter` → `Existing`
   - 选择：`.venv314t\Scripts\python.exe`
   - 确认解释器版本为 **Python 3.14t (free-threading)**

### 环境说明

- **虚拟环境路径**：`.venv314t/`（已加入 .gitignore）
- **Python 版本**：3.14.0 (free-threading)
- **项目路径**：`C:\Users\WDAGUtilityAccount\Desktop\comfyui_src\unsafe_project\learn_python14`

**注意事项**：
- ⚠️ 某些特性需要特定 Python 版本才能运行（示例文件中会标注）
- ⚠️ Python 3.14t 的 free-threading 特性为实验性功能
- ⚠️ 建议使用虚拟环境，避免影响系统 Python 环境

## 🚀 快速开始

### 1. 配置环境

```bash
# 激活虚拟环境
.venv314t\Scripts\activate

# 验证 Python 版本
python --version
```

### 2. 开始学习

```bash
# 从 Python 3.8 开始
cd curriculum\v3_8

# 1. 阅读版本概览
type overview.md

# 2. 学习第一个特性
cd 01_walrus_operator
type feature.md          # 阅读功能说明和 10 个应用场景
cd examples
python 01_loop_condition.py    # 运行第一个场景示例
python 02_file_processing.py   # 运行第二个场景示例
python comprehensive.py         # 运行综合示例
```

### 3. 学习一个特性的流程

1. **阅读文档** - 打开 `feature.md`
   - 一句话总结：快速理解特性核心
   - 功能详解：是什么、解决什么问题、语法要点
   - **10 个核心场景**：详细说明实际应用
   - 注意事项：常见陷阱 + 最佳实践

2. **运行示例** - 进入 `examples/` 目录
   - `01-10_*.py`：10 个场景示例（每个 10-30 行）
   - `comprehensive.py`：综合示例（30-50 行）
   - 查看 `README.md` 了解示例列表

3. **完成检查** - 对照 `feature.md` 底部的快速检查清单

## 📚 版本内容

### ✅ Python 3.8（100% 完成）

```
curriculum/v3_8/
├── overview.md                      # 版本整体概览
├── 01_walrus_operator/              # 赋值表达式 (:=)
│   ├── feature.md                   # 详细说明 + 10 个场景
│   └── examples/
│       ├── 01-10_*.py               # 10 个场景示例
│       ├── comprehensive.py         # 综合示例
│       └── README.md
├── 02_positional_only_params/       # 仅位置参数 (/)
├── 03_fstring_debug/                # f-string 调试 (f"{x=}")
├── 04_cached_property/              # 缓存属性
└── 05_importlib_metadata/           # 包元数据
```

**核心特性**：
- ✅ Walrus Operator (`:=`) - 表达式内赋值
- ✅ Positional-only Parameters (`/`) - API 设计保护
- ✅ F-string Debug (`f"{x=}"`) - 快速调试
- ✅ `functools.cached_property` - 性能优化
- ✅ `importlib.metadata` - 依赖管理

### ✅ Python 3.9（100% 完成）

```
curriculum/v3_9/
├── overview.md
├── 01_dict_merge_operators/         # 字典合并运算符 (|, |=)
├── 02_builtin_generic_types/        # 内置泛型 (list[int])
├── 03_annotated/                    # typing.Annotated
├── 04_str_prefix_suffix/            # removeprefix/removesuffix
└── 05_zoneinfo/                     # zoneinfo 时区支持
```

**核心特性**：
- ✅ 字典合并运算符 `|` 和 `|=` (PEP 584)
- ✅ 内置泛型类型 `list[int]`, `dict[str, int]` (PEP 585)
- ✅ `typing.Annotated` (PEP 593)
- ✅ 字符串方法 `removeprefix` / `removesuffix` (PEP 616)
- ✅ `zoneinfo` 时区支持

### 🚧 Python 3.10（25% 完成）

```
curriculum/v3_10/
├── overview.md                      # ✅ 已完成
├── 01_match_case/                   # ✅ 已完成 - 结构化模式匹配
│   ├── feature.md
│   └── examples/                    # 12 个文件
├── 02_union_types/                  # ⏳ 待完成 - 联合类型简写 (X | Y)
├── 03_paramspec/                    # ⏳ 待完成 - ParamSpec
└── 04_zip_strict/                   # ⏳ 待完成 - zip(strict=True)
```

**核心特性**：
- ✅ 结构化模式匹配 `match/case` (PEP 634-636)
- ⏳ 联合类型简写 `X | Y` (PEP 604)
- ⏳ `ParamSpec` (PEP 612)
- ⏳ `zip(strict=True)` (PEP 618)

### ⏳ Python 3.11（待完成）

**计划特性**：
- ExceptionGroup 和 `except*` (PEP 654)
- `tomllib` (PEP 680)
- `typing.Self` (PEP 673)
- TypeVarTuple (PEP 646)
- `asyncio.TaskGroup`

### ⏳ Python 3.12（待完成）

**计划特性**：
- 类型参数语法 `class Box[T]` (PEP 695)
- f-string 增强 (PEP 701)
- `sys.monitoring` API (PEP 669)
- TypedDict for `**kwargs` (PEP 692)
- `typing.override` (PEP 698)

### ⏳ Python 3.13-3.14（待完成）

**计划特性**：
- 无 GIL 自由线程（实验性）
- 其他待定特性

## 📂 完整目录结构

```
learn_python14/
├── README.md                        # 📖 项目说明（本文件）
├── PROGRESS.md                      # 📊 详细进度报告
├── CONTINUATION_PROMPT.md           # 📋 重构指南
├── PROJECT_GUIDE.md                 # 📐 项目结构说明
├── env.md                           # 🔧 环境配置详细指南
├── check_python_version.py          # ✅ 版本检查脚本
├── .gitignore                       # 🚫 Git 忽略配置
├── python-3.14.0-amd64.exe          # 📦 Python 安装包
├── .venv314t/                       # 🐍 虚拟环境（不提交）
├── curriculum/                      # 📚 按版本组织的课程
│   ├── v3_8/                       # ✅ Python 3.8（100%）
│   │   ├── overview.md
│   │   ├── 01_walrus_operator/
│   │   │   ├── feature.md
│   │   │   └── examples/
│   │   │       ├── 01-10_*.py      # 10 个场景示例
│   │   │       ├── comprehensive.py # 综合示例
│   │   │       └── README.md
│   │   ├── 02_positional_only_params/
│   │   ├── 03_fstring_debug/
│   │   ├── 04_cached_property/
│   │   └── 05_importlib_metadata/
│   ├── v3_9/                       # ✅ Python 3.9（100%）
│   │   ├── overview.md
│   │   ├── 01_dict_merge_operators/
│   │   ├── 02_builtin_generic_types/
│   │   ├── 03_annotated/
│   │   ├── 04_str_prefix_suffix/
│   │   └── 05_zoneinfo/
│   ├── v3_10/                      # 🚧 Python 3.10（25%）
│   │   ├── overview.md
│   │   ├── 01_match_case/          # ✅ 已完成
│   │   ├── 02_union_types/         # ⏳ 待完成
│   │   ├── 03_paramspec/           # ⏳ 待完成
│   │   └── 04_zip_strict/          # ⏳ 待完成
│   ├── v3_11/                      # ⏳ Python 3.11（待完成）
│   ├── v3_12/                      # ⏳ Python 3.12（待完成）
│   ├── v3_13/                      # ⏳ Python 3.13（待完成）
│   └── v3_14/                      # ⏳ Python 3.14（待完成）
├── topics/                          # 🔖 跨版本专题
│   ├── typing/                     # 类型系统演进
│   ├── packaging/                  # 打包与发布
│   ├── concurrency/                # 并发编程
│   ├── compatibility/              # 兼容性处理
│   └── debugging_monitoring/       # 调试与监控
├── tooling/                         # 🛠️ 工具配置
│   ├── mypy_pyright.md
│   └── pyproject_samples/
└── capstone/                        # 🎓 结业项目
    ├── README.md
    └── src/
        ├── main.py
        └── config.toml
```

## 📖 学习路径建议

### 初学者路径（按顺序学习）
- **第 1-2 周**：Python 3.8-3.9（基础语法增强）
- **第 3-4 周**：Python 3.10-3.11（类型系统 + 并发）
- **第 5-6 周**：Python 3.12-3.14（性能优化 + 前沿特性）
- **第 7 周**：完成 capstone 结业项目

### 进阶路径（按主题学习）
1. **类型系统专题**：v3_9 泛型 → v3_10 联合类型 → v3_11 Self → v3_12 类型参数
2. **并发编程专题**：v3_11 TaskGroup → v3_13 无 GIL
3. **调试监控专题**：v3_8 f-string debug → v3_12 sys.monitoring

### 快速查阅（按需学习）
- 查看各版本的 `overview.md` 快速了解核心特性
- 直接运行感兴趣特性的示例代码
- 阅读 `feature.md` 中的 10 个场景说明

## 🎯 文件命名规范

### 每个特性包含（共 12-13 个文件）
1. **feature.md** - 详细文档（1 个）
2. **场景示例** - 10 个 Python 文件（`01-10_*.py`）
3. **综合示例** - 1 个 Python 文件（`comprehensive.py`）
4. **README.md** - 示例目录说明（1 个）

### 示例文件格式
```python
"""
场景 X：场景名称

应用：具体应用场景描述
运行要求：Python >= 3.X
"""

# 测试数据
data = [...]

print("=" * 60)
print("场景标题")
print("=" * 60)

# ❌ 传统方式
print("\n[传统方式] 说明：")
# 旧代码...

# ✅ 使用新特性
print("\n[新特性] 说明：")
# 新代码...

print("\n💡 总结：一句话总结收益")
```

## 📊 统计数据

### 文件统计
| 版本 | 已完成 | 待完成 | 总计 | 完成率 |
|------|--------|--------|------|--------|
| v3.8 | 66 | 0 | 66 | 100% |
| v3.9 | 66 | 0 | 66 | 100% |
| v3.10 | 13 | ~39 | ~52 | 25% |
| v3.11 | 0 | ~62 | ~62 | 0% |
| v3.12 | 0 | ~62 | ~62 | 0% |
| v3.13 | 0 | ~35 | ~35 | 0% |
| v3.14 | 0 | ~25 | ~25 | 0% |
| **总计** | **145** | **~223** | **~368** | **39%** |

### 代码行数估算
- **已完成**：约 11,500 行
- **预计总计**：约 28,000 行

## ✅ 运行要求

- **推荐 Python 版本**：Python 3.14t (free-threading)
- **最低版本要求**：运行某版本示例时，建议使用匹配或更高版本
  - 例如：v3_10 示例请用 Python ≥ 3.10
- **虚拟环境**：强烈建议使用 `.venv314t`
- **操作系统**：支持 Windows、Linux、macOS

### 版本检查
```bash
# 运行版本检查脚本
python check_python_version.py
```

## 🤝 贡献指南

本项目目前处于开发阶段，欢迎：
- 报告示例代码中的 bug
- 建议更实用的应用场景
- 提供更好的示例代码
- 完善文档说明

详细的重构指南请参考 `CONTINUATION_PROMPT.md`。

## 📄 相关文档

- **PROGRESS.md** - 详细的开发进度报告
- **CONTINUATION_PROMPT.md** - 重构任务指南（给 AI 使用）
- **PROJECT_GUIDE.md** - 项目架构说明
- **env.md** - 环境配置详细指南

## 📜 许可

本项目内容用于学习与参考，可自由扩展与修改。

---

**🎓 祝学习愉快！逐步掌握 Python 3.8-3.14 的所有新特性！**

_最后更新：2025-10-17_
