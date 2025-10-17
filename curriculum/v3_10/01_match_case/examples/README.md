# match/case 示例代码

本目录包含 **match/case（结构化模式匹配）** 的 10 个独立场景示例和 1 个综合示例。

## 📋 示例列表

| 文件 | 场景 | 难度 | 核心知识点 |
|------|------|------|-----------|
| `01_basic_patterns.py` | 基本模式匹配 | ⭐ | 字面量、序列、映射、OR、AS、守卫 |
| `02_command_parser.py` | 命令行参数解析 | ⭐⭐ | 序列模式、通配符、多级命令 |
| `03_http_response.py` | HTTP 响应处理 | ⭐⭐ | 映射模式、嵌套结构、守卫条件 |
| `04_config_validation.py` | 配置文件验证 | ⭐⭐⭐ | 数据验证、类型检查、嵌套配置 |
| `05_event_handler.py` | 事件处理系统 | ⭐⭐⭐ | 事件分发、多类型事件、上下文处理 |
| `06_data_validation.py` | 数据验证 | ⭐⭐⭐ | 表单验证、复杂规则、守卫组合 |
| `07_state_machine.py` | 状态机实现 | ⭐⭐⭐⭐ | 状态转换、元组模式、业务逻辑 |
| `08_router.py` | 路由系统 | ⭐⭐⭐⭐ | URL 路由、RESTful API、嵌套资源 |
| `09_json_processing.py` | JSON 数据处理 | ⭐⭐⭐ | 不确定结构、嵌套数据、类型分发 |
| `10_game_logic.py` | 游戏逻辑 | ⭐⭐⭐⭐ | 碰撞检测、技能系统、装备系统 |
| `comprehensive.py` | 综合示例 | ⭐⭐⭐⭐ | 命令行任务管理系统 |

## 🚀 快速开始

### 环境要求

- **Python 版本**: 3.10+
- **无需额外依赖**: 所有示例只使用标准库

### 运行示例

```bash
# 进入示例目录
cd curriculum/v3_10/01_match_case/examples

# 运行单个示例
python 01_basic_patterns.py

# 运行综合示例
python comprehensive.py
```

## 📚 核心概念

### 1. 基本语法

```python
match subject:
    case pattern1:
        # 处理 pattern1
    case pattern2:
        # 处理 pattern2
    case _:
        # 默认情况
```

### 2. 模式类型

#### 字面量模式
```python
match status_code:
    case 200:
        return "成功"
    case 404:
        return "未找到"
```

#### 序列模式
```python
match point:
    case [x, y]:
        print(f"2D 点: ({x}, {y})")
    case [x, y, z]:
        print(f"3D 点: ({x}, {y}, {z})")
```

#### 映射模式
```python
match user:
    case {"name": name, "role": "admin"}:
        print(f"管理员: {name}")
```

#### 类模式
```python
match shape:
    case Circle(radius=r):
        area = 3.14 * r * r
```

### 3. 高级特性

#### OR 模式
```python
match command:
    case "quit" | "exit" | "q":
        sys.exit()
```

#### 守卫条件
```python
match value:
    case x if x > 0:
        print("正数")
```

#### AS 模式（捕获）
```python
match point:
    case [x, y] as p:
        print(f"点 {p} 的坐标是 ({x}, {y})")
```

#### 通配符
```python
match items:
    case [first, *rest]:
        print(f"首元素: {first}, 其余: {rest}")
```

## 🎯 学习路径

### 初学者（2-3 小时）

1. **基础模式** - `01_basic_patterns.py`
   - 了解各种基本模式
   - 理解 match/case 的基本用法
   - 掌握常见陷阱

2. **简单应用** - `02_command_parser.py`, `03_http_response.py`
   - 学习实际应用场景
   - 理解序列和映射模式

### 进阶学习（3-4 小时）

3. **数据处理** - `04_config_validation.py`, `06_data_validation.py`
   - 掌握守卫条件的使用
   - 学习数据验证技巧

4. **事件系统** - `05_event_handler.py`, `09_json_processing.py`
   - 理解事件分发模式
   - 处理不确定的数据结构

### 高级应用（3-4 小时）

5. **复杂逻辑** - `07_state_machine.py`, `08_router.py`
   - 实现状态机
   - 构建路由系统

6. **游戏开发** - `10_game_logic.py`
   - 游戏逻辑实现
   - 复杂规则处理

### 综合实践

7. **完整项目** - `comprehensive.py`
   - 任务管理系统
   - 综合运用所有技巧

## ⚠️ 常见陷阱

### 1. 顺序很重要

```python
# ❌ 错误 - 通配符会匹配所有
match value:
    case _:
        print("默认")
    case 1:  # 永远不会执行
        print("一")

# ✅ 正确
match value:
    case 1:
        print("一")
    case _:
        print("默认")
```

### 2. 变量捕获 vs 常量匹配

```python
MAX = 100

# ⚠️  这会捕获变量，而不是比较
match value:
    case MAX:  # MAX 会被赋值为 value
        print("匹配")

# ✅ 正确 - 使用守卫
match value:
    case x if x == MAX:
        print("等于 MAX")
```

### 3. 字典模式是部分匹配

```python
# ✅ 可以只匹配部分键
match {"a": 1, "b": 2, "c": 3}:
    case {"a": x}:  # 匹配成功，x = 1
        print(x)
```

### 4. 类模式需要 __match_args__

```python
class Point:
    __match_args__ = ("x", "y")  # 必须定义
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 现在可以使用位置匹配
match Point(1, 2):
    case Point(x, y):
        print(x, y)
```

## ✅ 最佳实践

### 1. 使用有意义的变量名

```python
# ❌ 不好
match data:
    case {"a": x, "b": y}:
        ...

# ✅ 好
match user_data:
    case {"name": username, "age": user_age}:
        ...
```

### 2. 保持 case 分支简洁

```python
# ❌ 不好 - case 内逻辑太复杂
match event:
    case {"type": "click", "x": x, "y": y}:
        # 100 行代码...
        ...

# ✅ 好 - 提取到函数
match event:
    case {"type": "click", "x": x, "y": y}:
        handle_click(x, y)
```

### 3. 利用守卫进行验证

```python
# ✅ 好 - 在守卫中验证
match user:
    case {"age": int(age)} if 18 <= age <= 100:
        process_adult(age)
    case {"age": int(age)} if age < 18:
        process_minor(age)
```

### 4. 添加默认分支

```python
# ✅ 总是包含默认分支
match command:
    case ["add", item]:
        ...
    case ["remove", item]:
        ...
    case _:
        print("未知命令")
```

## 🔗 相关资源

- [PEP 634 – Structural Pattern Matching: Specification](https://peps.python.org/pep-0634/)
- [PEP 635 – Structural Pattern Matching: Motivation](https://peps.python.org/pep-0635/)
- [PEP 636 – Structural Pattern Matching: Tutorial](https://peps.python.org/pep-0636/)
- [Python 3.10 新特性](https://docs.python.org/3/whatsnew/3.10.html)

## 💡 小贴士

### 1. 调试 match 语句

```python
# 添加打印查看匹配情况
match value:
    case pattern as matched:
        print(f"匹配成功: {matched}")
        ...
```

### 2. 组合多个模式

```python
# 使用 OR 组合
match value:
    case 0 | 1 | 2:
        print("0-2")
```

### 3. 嵌套匹配

```python
# 可以嵌套使用
match data:
    case {"user": {"name": name, "role": role}}:
        print(f"{name} is {role}")
```

### 4. 性能考虑

- match/case 的性能与等价的 if/elif 链相似
- 对于简单的字面量匹配，可能使用跳转表优化
- 不要过早优化，优先考虑代码可读性

## 📊 示例统计

| 类型 | 数量 | 代码行数（估计） |
|------|------|-----------------|
| 基础示例 | 3 | ~300 |
| 中级示例 | 4 | ~600 |
| 高级示例 | 3 | ~800 |
| 综合示例 | 1 | ~400 |
| **总计** | **11** | **~2100** |

## 📝 练习建议

### 初级练习

1. 修改 `01_basic_patterns.py`，添加更多模式类型
2. 在 `02_command_parser.py` 中添加新命令
3. 扩展 `03_http_response.py`，处理更多状态码

### 中级练习

4. 实现一个配置文件加载器（基于 `04_config_validation.py`）
5. 创建一个简单的事件总线（基于 `05_event_handler.py`）
6. 构建一个表单验证库（基于 `06_data_validation.py`）

### 高级练习

7. 实现一个完整的状态机库（基于 `07_state_machine.py`）
8. 创建一个 Web 微框架（基于 `08_router.py`）
9. 开发一个简单的 RPG 游戏（基于 `10_game_logic.py`）

### 综合练习

10. 扩展 `comprehensive.py`，添加更多功能：
    - 任务优先级自动调整
    - 定时提醒功能
    - 数据持久化（JSON/SQLite）
    - 任务依赖关系
    - 子任务支持

---

**下一步**: 查看 `../feature.md` 了解 match/case 的详细特性说明

