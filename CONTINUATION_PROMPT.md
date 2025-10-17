# Python 3.9-3.14 版本重构任务 - 上下文提示词

> 📋 本文档用于在新对话中继续完成 Python 3.9-3.14 版本的重构工作

---

## 📚 项目背景

### 项目目标
创建一个系统化的 Python 3.7→3.14 增量学习项目，帮助开发者掌握每个版本的新特性。

### 项目路径
```
C:\Users\WDAGUtilityAccount\Desktop\comfyui_src\unsafe_project\learn_python14
```

### 已完成工作

✅ **Python 3.8 版本** - 100% 完成（5个特性，66个文件）
- 01_walrus_operator/ - 完成
- 02_positional_only_params/ - 完成
- 03_fstring_debug/ - 完成
- 04_cached_property/ - 完成
- 05_importlib_metadata/ - 完成

✅ **Python 3.9 版本** - 100% 完成（5个特性，66个文件）
- 01_dict_merge_operators/ - 完成
- 02_builtin_generic_types/ - 完成
- 03_annotated/ - 完成
- 04_str_prefix_suffix/ - 完成
- 05_zoneinfo/ - 完成 ⭐ 本次新增示例文件

🚧 **Python 3.10 版本** - 25% 进行中（4个特性）
- overview.md - ✅ 完成
- 01_match_case/ - ✅ 完成（12个文件：feature.md + 10个示例 + comprehensive.py + README.md）
- 02_union_types/ - ⏳ 待完成
- 03_paramspec/ - ⏳ 待完成
- 04_zip_strict/ - ⏳ 待完成

---

## 🎯 待完成任务

按优先级顺序完成以下版本的重构：

### 1. ~~Python 3.9~~（优先级：高）✅ 已完成
~~**主要特性**（需要重构的）：~~
1. ~~字典合并运算符 `|` 和 `|=` (PEP 584)~~ ✅
2. ~~内置泛型 `list[int]`, `dict[str, int]` (PEP 585)~~ ✅
3. ~~`typing.Annotated` (PEP 593)~~ ✅
4. ~~字符串方法 `removeprefix` / `removesuffix` (PEP 616)~~ ✅
5. ~~`zoneinfo` 时区支持~~ ✅

### 2. Python 3.10（优先级：高）🚧 进行中 - 25% 完成
**主要特性**：
1. ~~结构化模式匹配 `match/case` (PEP 634-636)~~ ✅ 已完成
2. 联合类型简写 `X | Y` (PEP 604) ⏳ 待完成
3. `ParamSpec` (PEP 612) ⏳ 待完成
4. `zip(strict=True)` (PEP 618) ⏳ 待完成

### 3. Python 3.11（优先级：中）
**主要特性**：
1. `ExceptionGroup` 和 `except*` (PEP 654)
2. `tomllib` (PEP 680)
3. `typing.Self` (PEP 673)
4. 可变参数泛型 `TypeVarTuple` (PEP 646)
5. `asyncio.TaskGroup`

### 4. Python 3.12（优先级：中）
**主要特性**：
1. 类型参数语法 `class Box[T]` (PEP 695)
2. f-string 增强 (PEP 701)
3. `sys.monitoring` API (PEP 669)
4. `TypedDict` for `**kwargs` (PEP 692)
5. `typing.override` (PEP 698)

### 5. Python 3.13-3.14（优先级：低）
**主要特性**：
- 无 GIL 自由线程（实验性）
- 其他待定特性

---

## 📐 标准结构模板

### 每个版本的目录结构
```
curriculum/v3_X/
├── overview.md                          # 版本整体概览
├── 01_feature_name/
│   ├── feature.md                       # 详细说明
│   └── examples/
│       ├── 01_scenario_name.py          # 场景1
│       ├── 02_scenario_name.py          # 场景2
│       ├── ...                          # 场景3-10
│       ├── comprehensive.py             # 综合示例
│       └── README.md                    # 目录说明
├── 02_feature_name/                     # 重复上述结构
└── ...
```

### 每个特性需要创建的文件
1. **feature.md**（1个）
   - 一句话总结
   - 功能详解（是什么、解决什么问题、语法要点）
   - **10个核心应用场景**（详细描述，2-3句话）
   - 示例代码说明
   - 注意事项（常见陷阱 + 最佳实践）
   - 版本关系、扩展阅读、快速检查清单

2. **场景示例**（10个）
   - 文件名：`01-10_场景名.py`
   - 代码行数：10-30行
   - 聚焦单一场景
   - 包含完整测试数据
   - 可直接运行
   - 统一格式：场景说明 → 传统方式 → 新特性方式 → 总结

3. **综合示例**（1个）
   - 文件名：`comprehensive.py`
   - 代码行数：30-50行
   - 模拟真实业务场景
   - 展示特性的综合应用

4. **README.md**（1个）
   - 示例列表（表格形式）
   - 快速开始指南
   - 核心概念总结

5. **overview.md**（每个版本1个）
   - 版本背景介绍
   - 核心特性速览（表格）
   - 学习路径建议
   - 与其他版本的关系

---

## ✅ 质量标准

### 代码示例要求
- ✅ 每个示例 10-50 行，不要太长
- ✅ 包含完整的测试数据（模拟真实场景）
- ✅ 可直接运行（无需额外依赖）
- ✅ 代码清晰注释
- ✅ 输出格式统一（使用分割线、emoji）

### 场景选择要求
- ✅ 实用性强（真实业务场景）
- ✅ 覆盖面广（不同领域）
- ✅ 难度递进（从简单到复杂）
- ✅ 对比明显（展示新特性优势）

### 文档写作要求
- ✅ 全中文（专业术语保留英文）
- ✅ 简洁明了（避免冗长描述）
- ✅ 格式统一（参考已完成的 3.8）
- ✅ 包含示例（代码片段说明）

---

## 📋 具体执行步骤

### 开始新版本重构时：

#### Step 1：研究版本特性
查询该版本的官方文档和 PEP，确定 3-5 个核心特性。

#### Step 2：创建 overview.md
参考 Python 3.8 的 overview.md 格式。

#### Step 3：逐个特性重构
对每个特性：
1. 创建目录 `0X_feature_name/`
2. 编写 `feature.md`
3. 创建 `examples/` 目录
4. 编写 10 个场景示例 + 1 个综合示例
5. 编写 `examples/README.md`

#### Step 4：验证完整性
- 检查目录结构是否完整
- 运行几个示例验证是否正常
- 确认文件数量正确（每个特性 12 个文件）

---

## 🎨 参考模板（基于 Python 3.8）

### feature.md 模板结构
```markdown
# 特性名称

## 一句话总结
简洁说明这个特性加了什么

## 功能详解
### 是什么？
### 解决什么问题？
### 语法要点

## 核心应用场景
### 1. 场景名称
描述（2-3句话）
**收益**: 具体收益

### 2-10. ...

## 示例代码说明
指向 examples/ 目录的说明

## 注意事项
### ⚠️ 常见陷阱
### ✅ 最佳实践

## 与其他版本的关系
## 扩展阅读
## 快速检查清单
```

### 场景示例代码模板
```python
"""
场景 X：场景名称

应用：具体应用场景描述
"""

# 测试数据
data = [...]

print("=" * 60)
print("场景标题")
print("=" * 60)

# ❌ 传统方式
print("\n[传统方式] 说明：\n")
# 旧代码

# ✅ 使用新特性
print("\n[新特性] 说明：\n")
# 新代码

print("\n💡 总结：一句话总结收益")
```

---

## 🔧 环境信息

- **Python 版本**: 3.14t (free-threading)
- **虚拟环境**: `.venv314t`
- **项目路径**: `C:\Users\WDAGUtilityAccount\Desktop\comfyui_src\unsafe_project\learn_python14`
- **工作目录**: `curriculum/`

---

## 📝 特别注意事项

### 1. Python 版本特定特性
某些特性只能在特定版本运行，需要在示例开头注明：
```python
"""
运行要求：Python >= 3.10
"""
```

### 2. 避免外部依赖
所有示例只使用标准库，不依赖第三方包（除非该特性本身就是标准库新增的）。

### 3. Windows 路径处理
注意 Windows 路径使用反斜杠，使用 `Move-Item` 而不是 `mv`。

### 4. 保持一致性
严格参考 Python 3.8 已完成的结构和风格，保持整个项目的一致性。

---

## 🚀 开始命令示例

### 复制以下内容到新对话：

```
你好！我需要继续完成一个 Python 学习项目的重构工作。

项目路径：C:\Users\WDAGUtilityAccount\Desktop\comfyui_src\unsafe_project\learn_python14

已完成：Python 3.8 版本（5个特性，61个文件）
待完成：Python 3.9-3.14 版本

请按照以下优先级完成：
1. Python 3.9（优先）- 5个主要特性
2. Python 3.10（优先）- 4个主要特性
3. Python 3.11-3.14（后续）

具体要求参考项目根目录的 CONTINUATION_PROMPT.md 文件。

请先读取以下文件了解已完成的结构：
1. curriculum/v3_8/overview.md
2. curriculum/v3_8/01_walrus_operator/feature.md
3. curriculum/v3_8/01_walrus_operator/examples/README.md
4. curriculum/v3_8/01_walrus_operator/examples/01_loop_condition.py

然后开始 Python 3.9 的重构。每个特性需要：
- 1个 feature.md（详细说明 + 10个场景）
- 10个场景示例（每个10-30行）
- 1个综合示例（30-50行）
- 1个 examples/README.md

请确认理解后开始执行。
```

---

## 📊 工作量统计

### 已完成工作量（本次会话）
- **修复文件**: v3.9/05_zoneinfo（7个文件）
- **新增文件**: v3.10/overview.md + 01_match_case（13个文件）
- **本次总计**: 20个文件
- **代码行数**: 约 4,500 行
- **实际用时**: 约 1 小时

### 每个版本预计
- **文件数**: 40-60 个
- **代码行数**: 3000-5000 行
- **完成时间**: 每个版本约 1-2 小时

### 总计（3.9-3.14）
- **总文件数**: 约 250-350 个
- **总代码行数**: 约 20,000-30,000 行
- **预计总时间**: 6-12 小时
- **当前进度**: 约 40% （v3.8, v3.9 完成，v3.10 进行中）

---

## ✅ 验收标准

每个版本完成后应包含：
- [ ] overview.md - 版本概览
- [ ] 每个特性的 feature.md - 详细说明
- [ ] 每个特性的 10 个场景示例
- [ ] 每个特性的 1 个综合示例
- [ ] 每个特性的 examples/README.md
- [ ] 所有示例可正常运行
- [ ] 文档格式统一
- [ ] 与 Python 3.8 结构一致

---

## 🎯 成功标志

项目最终应该达到：
- ✅ 7个 Python 版本（3.8-3.14）全部重构
- ✅ 每个版本结构一致
- ✅ 所有示例可直接运行
- ✅ 文档清晰完整
- ✅ 学习路径明确

---

**祝顺利完成！有任何问题随时调整策略。** 🚀

