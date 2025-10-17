# Learn Python 3.14 项目完整使用指南

> 本项目是一个系统化学习 Python 3.7→3.14 增量特性的教程项目

---

## 📁 项目结构总览

```
learn_python14/
│
├── 📖 README.md                    # 项目总览（你的入口文档）
├── 📖 PROJECT_GUIDE.md             # 本文件：详细使用指南
├── 📖 env.md                       # 环境配置指南（多版本 Python 管理）
│
├── 🐍 python-3.14.0-amd64.exe      # Python 3.14 安装包（可删除）
├── 📁 python314/                   # Python 3.14 标准安装目录
├── 📁 .venv314t/                   # Python 3.14t 虚拟环境（free-threading）
│
├── 🔧 check_python_version.py      # 环境检测工具（验证是否为 3.14t）
│
├── 📚 curriculum/                  # 核心学习内容（按版本组织）
│   ├── v3_8/                       ✅ 已重构（新结构）
│   ├── v3_9/                       📝 待重构
│   ├── v3_10/                      📝 待重构
│   ├── v3_11/                      📝 待重构
│   ├── v3_12/                      📝 待重构
│   ├── v3_13/                      📝 待重构
│   ├── v3_14/                      📝 待完善
│   └── v3_14_free_threading/       🆕 3.14t 专题（无 GIL）
│
├── 🎓 topics/                      # 跨版本专题（深入某个领域）
│   ├── typing/                     类型系统演进
│   ├── packaging/                  打包与发布
│   ├── concurrency/                并发编程
│   ├── compatibility/              兼容性处理
│   └── debugging_monitoring/       调试与监控
│
├── 🛠️ tooling/                     # 开发工具配置
│   ├── mypy_pyright.md             静态类型检查工具
│   ├── mypy.ini                    mypy 配置文件
│   └── pyproject_samples/          项目配置示例
│
└── 🎯 capstone/                    # 结业项目（综合应用）
    ├── README.md                   项目说明
    └── src/                        源代码目录
```

---

## 🎯 各部分详解

### 1️⃣ **curriculum/** - 核心学习内容（按版本组织）

**用途**：按 Python 版本递进学习，每个版本的新特性独立讲解

#### ✨ 已完成：v3_8/（新结构示例）

```
v3_8/
├── overview.md                     # 版本整体概览，先读这个！
├── 01_walrus_operator/             # 每个特性一个目录
│   ├── feature.md                  # 详细说明 + 10 个应用场景
│   └── example.py                  # 30-50 行实战示例
├── 02_positional_only_params/
├── 03_fstring_debug/
├── 04_cached_property/
└── 05_importlib_metadata/
```

**如何学习**：
```bash
# 1. 阅读版本概览
cd curriculum/v3_8
cat overview.md        # 或在 PyCharm 中打开

# 2. 按顺序学习每个特性
cd 01_walrus_operator
cat feature.md         # 阅读功能说明和 10 个场景
python example.py      # 运行实战示例

# 3. 完成后继续下一个
cd ../02_positional_only_params
```

**学习时长**：每个特性 30-60 分钟，整个版本 3-5 小时

#### 📝 待重构：v3_9/ - v3_13/（旧结构）

```
v3_9/
├── lesson.md          # 单一的讲解文档
├── examples/          # 所有示例在一个目录
│   ├── example1.py
│   └── example2.py
└── exercises/         # 练习题
```

**特点**：内容比较简洁，等待重构为新结构

#### 🆕 v3_14_free_threading/（专题）

**用途**：深入学习 Python 3.14t 的无 GIL 特性

```
v3_14_free_threading/
├── README.md          # 专题学习路径（12 个主题）
├── 01_gil_basics/     # GIL 历史与原理
├── 03_cpu_bound_parallel/  # CPU 密集型加速
├── 06_thread_safety/  # 线程安全
└── 12_capstone_project/  # 综合项目
```

**特殊要求**：必须使用 `python3.14t.exe`（free-threading 构建）

---

### 2️⃣ **topics/** - 跨版本专题（深入某个领域）

**用途**：某些特性跨越多个版本演进，这里汇总讲解

```
topics/
├── typing/              # 类型系统专题
│   ├── README.md        # 从 3.8 到 3.14 的类型系统演进
│   └── example_self_typeparam.py
│
├── packaging/           # 打包与发布专题
│   ├── setup.py vs pyproject.toml 演进
│   └── 如何发布到 PyPI
│
├── concurrency/         # 并发编程专题
│   ├── threading vs asyncio vs multiprocessing
│   └── 最佳实践选择
│
├── compatibility/       # 兼容性专题
│   └── 如何编写同时支持多版本的代码
│
└── debugging_monitoring/  # 调试监控专题
    └── 3.12 的 sys.monitoring 等
```

**何时学习**：
- 当你学完某几个版本后，想深入理解某个主题
- 例如学完 3.9-3.12 后，可以系统学习 `typing/` 专题

---

### 3️⃣ **tooling/** - 开发工具配置

**用途**：配置静态类型检查、代码质量工具等

```
tooling/
├── mypy_pyright.md     # mypy 和 pyright 使用指南
├── mypy.ini            # mypy 配置文件（可复制到项目）
└── pyproject_samples/  # pyproject.toml 配置示例
```

**使用场景**：
- 学习类型系统后，想在自己项目中启用类型检查
- 需要配置项目的打包和依赖管理

---

### 4️⃣ **capstone/** - 结业项目

**用途**：综合应用所学特性，完成一个实战项目

```
capstone/
├── README.md           # 项目需求说明
└── src/
    ├── main.py         # 主程序（待完成）
    └── config.toml     # 配置文件
```

**项目要求**：
- 使用 `tomllib` 读取配置（3.11+）
- 使用 `match/case` 解析命令（3.10+）
- 使用 `asyncio.TaskGroup` 并发（3.11+）
- 应用完整的类型注解

**何时开始**：学完 3.8-3.12 后的综合练习

---

### 5️⃣ **根目录文件**

#### 📖 README.md
- **用途**：项目总览，快速了解项目特色和学习路径
- **何时阅读**：项目第一次使用前

#### 📖 env.md
- **用途**：教你如何安装和管理多个 Python 版本
- **何时阅读**：配置环境时（特别是需要测试多版本兼容性）

#### 🔧 check_python_version.py
- **用途**：检测当前 Python 是否为 3.14t free-threading 版本
- **使用**：`python check_python_version.py`

#### 🐍 python-3.14.0-amd64.exe
- **用途**：Python 3.14 安装包（已安装后可删除）
- **建议**：移到其他地方或删除（节省空间）

#### 📁 python314/ 和 .venv314t/
- **python314/**：Python 3.14 标准版安装目录
- **.venv314t/**：Python 3.14t 虚拟环境（你正在用的）

---

## 🚀 三种使用方式

### 方式 1：系统化学习（推荐新手）

**适合**：想全面掌握 Python 3.7→3.14 的演进

**路径**：
```
第 1 周：Python 3.8 基础
  → 学习 curriculum/v3_8/ （5 个特性）
  
第 2 周：Python 3.9-3.10
  → 学习 curriculum/v3_9/ 和 v3_10/
  
第 3 周：Python 3.11-3.12
  → 学习 curriculum/v3_11/ 和 v3_12/
  
第 4 周：深入专题
  → 学习 topics/typing/（类型系统）
  → 学习 topics/concurrency/（并发编程）
  
第 5 周：3.14t 专题
  → 学习 curriculum/v3_14_free_threading/
  
第 6 周：综合项目
  → 完成 capstone/ 结业项目
```

### 方式 2：目标驱动学习（推荐有经验者）

**适合**：只想学特定特性，已有 Python 基础

**路径**：
```
明确目标 → 直接跳到对应章节 → 按需补充前置知识

例如：
- 想学 free-threading → curriculum/v3_14_free_threading/
- 想学类型系统 → topics/typing/
- 想学并发 → topics/concurrency/
```

### 方式 3：查阅式使用（推荐实践者）

**适合**：实际项目中遇到问题，来查阅某个特性

**路径**：
```
遇到问题 → README.md 查目录 → 找到对应章节 → 阅读 feature.md

例如：
- 代码中看到 := 不懂 → curriculum/v3_8/01_walrus_operator/
- 想优化属性计算 → curriculum/v3_8/04_cached_property/
- 多线程性能差 → curriculum/v3_14_free_threading/03_cpu_bound_parallel/
```

---

## 📝 学习每个特性的标准流程

### Step 1：阅读版本概览
```bash
cd curriculum/v3_8
cat overview.md    # 了解这个版本的整体变化
```

### Step 2：学习单个特性
```bash
cd 01_walrus_operator
cat feature.md     # 详细阅读（包含 10 个应用场景）
```

**feature.md 结构**：
- 一句话总结
- 功能详解（是什么、解决什么问题）
- 10 个核心应用场景
- 示例代码说明
- 注意事项（陷阱 + 最佳实践）
- 快速检查清单

### Step 3：运行实战示例
```bash
python example.py  # 查看实际效果
```

**example.py 特点**：
- 30-50 行实用代码
- 模拟真实业务场景
- 带详细注释

### Step 4：完成检查清单
打开 `feature.md` 最后的"快速检查清单"，确认自己已掌握

### Step 5：尝试修改和实验
- 修改 `example.py` 的参数
- 尝试应用到自己的场景
- 编写自己的测试用例

---

## 🎯 你当前应该这样开始

基于你的环境（已配置 3.14t）：

### 选项 A：快速体验（30 分钟）

```bash
# 1. 快速过一遍 Python 3.8 的第一个特性
cd curriculum/v3_8/01_walrus_operator
python example.py

# 2. 看看 3.14t 专题规划
cd ../../v3_14_free_threading
cat README.md
```

### 选项 B：系统学习（推荐）

```bash
# 从头开始，打好基础
cd curriculum/v3_8
cat overview.md

# 然后逐个学习 5 个特性
cd 01_walrus_operator
cat feature.md
python example.py
```

### 选项 C：直奔主题（激进）

```bash
# 直接学习 free-threading（你的主要目标）
cd curriculum/v3_14_free_threading
cat README.md

# 后续我会为你创建具体内容
```

---

## 💡 PyCharm 中如何使用

### 1. 打开项目
- PyCharm → Open → 选择 `learn_python14` 目录

### 2. 配置解释器
- 右下角点击 Python 版本
- 选择 `.venv314t/Scripts/python3.14t.exe`

### 3. 学习流程
```
左侧文件树
  → 找到 curriculum/v3_8/overview.md
  → 双击阅读
  → 展开 01_walrus_operator/
  → 打开 feature.md 阅读
  → 右键 example.py → Run 'example'
```

### 4. 做笔记
可以在项目中创建 `my_notes/` 目录记录学习笔记

---

## ❓ 常见问题

### Q1: 我应该从哪个版本开始学？
**A**: 如果有 Python 基础 → 从 3.8 开始快速过一遍  
     如果是新手 → 建议先学 Python 基础再来

### Q2: v3_9-v3_13 还是旧结构，能用吗？
**A**: 能用，但内容比较简洁。我可以继续重构它们

### Q3: topics/ 和 curriculum/ 有什么区别？
**A**: 
- **curriculum/**: 按版本组织，学单个版本的新特性
- **topics/**: 按主题组织，学跨版本的演进（如类型系统）

### Q4: capstone/ 是必做的吗？
**A**: 不是必须，但强烈推荐。它是检验学习成果的最佳方式

### Q5: 我只想学 3.14t，其他的要学吗？
**A**: 建议至少快速过一遍 3.8-3.10 的基础特性（1-2 天），
     否则你会遇到很多不懂的语法和概念

---

## 🎁 下一步建议

### 立即行动：
```bash
# 1. 运行环境检测（确认配置正确）
python check_python_version.py

# 2. 快速体验（5 分钟）
cd curriculum/v3_8/01_walrus_operator
python example.py

# 3. 开始系统学习或直奔 3.14t
```

### 获取帮助：
- 如果需要我继续重构其他版本，随时告诉我
- 如果需要创建 3.14t 的具体内容，我可以立即开始
- 如果有不懂的概念，可以问我

---

**现在你应该清楚项目结构了！下一步想做什么？** 🚀

