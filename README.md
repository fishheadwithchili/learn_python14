Python 3.7 → 3.14 增量学习项目

## 概述

本项目面向已掌握 Python 3.7 的开发者，按 3.8→3.14 版本递进式学习关键语法、类型系统与标准库变化。

**特色**：
- ✅ **模块化结构**：每个特性独立目录，便于查找和学习
- ✅ **详尽场景说明**：每个功能提供 5-10+ 个实际应用场景
- ✅ **实用示例代码**：30-50 行的完整业务场景示例
- ✅ **清单式学习**：系统化掌握每个版本的新特性

## 快速开始

1. **配置环境**
   ```bash
   # 参考 env.md 配置多版本 Python 环境
   python3.8 -m venv venv38
   source venv38/bin/activate  # Windows: venv38\Scripts\activate
   ```

2. **开始学习**
   ```bash
   # 从 Python 3.8 开始
   cd curriculum/v3_8
   
   # 1. 阅读版本概览
   cat overview.md
   
   # 2. 学习第一个特性
   cd 01_walrus_operator
   cat feature.md          # 阅读功能说明和应用场景
   python example.py       # 运行实战示例
   
   # 3. 继续学习其他特性...
   ```

3. **学习一个特性的流程**
   - 📖 阅读 `feature.md`（功能详解 + 10 个场景）
   - 💻 运行 `example.py`（30-50 行实用示例）
   - ✅ 完成快速检查清单

## 版本结构说明

### ✨ Python 3.8（已重构 - 新结构示例）

```
curriculum/v3_8/
├── overview.md                      # 版本整体概览
├── 01_walrus_operator/              # 赋值表达式
│   ├── feature.md                   # 详细说明 + 10 个场景
│   └── example.py                   # 实战示例（日志分析）
├── 02_positional_only_params/       # 仅位置参数
│   ├── feature.md
│   └── example.py                   # 实战示例（API 设计）
├── 03_fstring_debug/                # f-string 调试
│   ├── feature.md
│   └── example.py                   # 实战示例（数据分析）
├── 04_cached_property/              # 缓存属性
│   ├── feature.md
│   └── example.py                   # 实战示例（文档解析）
└── 05_importlib_metadata/           # 包元数据
    ├── feature.md
    └── example.py                   # 实战示例（依赖检查）
```

**核心特性**：
- Walrus Operator (`:=`) - 表达式内赋值
- Positional-only Parameters (`/`) - API 设计保护
- f-string Debug (`f"{x=}"`) - 快速调试
- `cached_property` - 性能优化
- `importlib.metadata` - 依赖管理

### Python 3.9-3.14（待重构）

其他版本目前保持旧结构：`lesson.md` + `examples/` + `exercises/`

## 学习路径建议

- **第 1 周**：v3_8–v3_10（语法与常用库）+ 专题：typing 基础
- **第 2 周**：v3_11–v3_12（并发、性能、监控、打包）+ 专题：packaging
- **第 3 周**：v3_13–v3_14（前沿与稳定化）+ 专题：兼容性与迁移

## 完整目录结构

```
learn_python14/
├── README.md                        # 项目说明
├── env.md                           # 环境配置指南
├── curriculum/                      # 按版本组织的课程
│   ├── v3_8/                       # ✨ 已重构（新结构）
│   │   ├── overview.md
│   │   ├── 01_walrus_operator/
│   │   ├── 02_positional_only_params/
│   │   ├── 03_fstring_debug/
│   │   ├── 04_cached_property/
│   │   └── 05_importlib_metadata/
│   ├── v3_9/                       # 待重构（旧结构）
│   ├── v3_10/                      # 待重构
│   ├── v3_11/                      # 待重构
│   ├── v3_12/                      # 待重构
│   ├── v3_13/                      # 待重构
│   └── v3_14/                      # 待重构
├── topics/                          # 跨版本专题
│   ├── typing/                     # 类型系统演进
│   ├── packaging/                  # 打包与发布
│   ├── concurrency/                # 并发编程
│   ├── compatibility/              # 兼容性处理
│   └── debugging_monitoring/       # 调试与监控
└── tooling/                         # 工具配置
    ├── mypy_pyright.md
    └── pyproject_samples/
```

运行要求
- 运行某版本示例时，建议使用匹配或更高版本的 Python（如 v3_10 示例请用 Python ≥3.10）。
- Windows 可使用 Python Launcher：`py -3.11 -V`；Unix 系可通过 `pyenv`/包管理器安装多版本。

许可
- 本项目内容用于学习与参考，可自由扩展与修改。


