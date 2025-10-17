# match/case - 结构化模式匹配

## 一句话总结

Python 3.10 引入的结构化模式匹配 (Structural Pattern Matching)，提供类似其他语言 switch/case 的功能，但更强大，支持序列、映射、类实例的结构解构和守卫条件。

## 功能详解

### 是什么？

`match/case` 是 Python 3.10 引入的新语法（PEP 634/635/636），用于对数据结构进行模式匹配和解构。它不仅仅是简单的值比较，还能：
- 解构序列和映射
- 匹配类实例的属性
- 使用守卫条件（`if` 子句）
- 捕获匹配的部分值
- 处理通配符模式

**基本语法格式**:
```python
match subject:
    case pattern1:
        # 处理 pattern1
    case pattern2 if condition:
        # 处理 pattern2（带守卫）
    case _:
        # 默认情况（通配符）
```

### 解决什么问题？

**问题 1: 复杂的 if/elif 链难以维护**
```python
# 旧代码 - 冗长且容易出错
if isinstance(data, tuple) and len(data) == 2:
    x, y = data
    # 处理二维点
elif isinstance(data, tuple) and len(data) == 3:
    x, y, z = data
    # 处理三维点
elif isinstance(data, dict) and 'type' in data:
    if data['type'] == 'user':
        # 处理用户
    elif data['type'] == 'admin':
        # 处理管理员
```

**问题 2: 数据结构解构繁琐**
```python
# 旧代码 - 需要手动检查和解包
if isinstance(command, list) and len(command) >= 2:
    action = command[0]
    if action == 'move':
        if len(command) == 3:
            direction, steps = command[1], command[2]
```

**问题 3: 缺少类型安全的分支处理**
```python
# 旧代码 - 类型检查和处理分离
if isinstance(node, BinOp):
    left = node.left
    op = node.op
    right = node.right
    # 处理二元操作
```

### 语法要点

1. **字面量模式**
   ```python
   match status:
       case 200:
           return "成功"
       case 404:
           return "未找到"
       case 500:
           return "服务器错误"
   ```

2. **序列模式**
   ```python
   match point:
       case [x, y]:  # 匹配两元素列表
           print(f"2D 点: ({x}, {y})")
       case [x, y, z]:  # 匹配三元素列表
           print(f"3D 点: ({x}, {y}, {z})")
   ```

3. **映射模式**
   ```python
   match data:
       case {"name": name, "age": age}:
           print(f"{name} 年龄 {age}")
       case {"id": user_id}:
           print(f"ID: {user_id}")
   ```

4. **类模式**
   ```python
   match shape:
       case Circle(radius=r):
           area = 3.14 * r * r
       case Rectangle(width=w, height=h):
           area = w * h
   ```

5. **守卫条件**
   ```python
   match value:
       case x if x > 0:
           print("正数")
       case x if x < 0:
           print("负数")
       case _:
           print("零")
   ```

6. **OR 模式**
   ```python
   match command:
       case "quit" | "exit" | "q":
           sys.exit()
   ```

7. **AS 模式（捕获）**
   ```python
   match point:
       case [x, y] as p:
           print(f"点 {p} 的坐标是 ({x}, {y})")
   ```

8. **通配符**
   ```python
   match value:
       case [first, *rest]:  # 捕获剩余元素
           print(f"第一个: {first}, 其余: {rest}")
       case _:  # 匹配任何值（但不捕获）
           print("默认情况")
   ```

## 核心应用场景

### 1. **命令行参数解析**
解析不同格式的命令行指令：
```python
match sys.argv[1:]:
    case ["install", package]:
        install_package(package)
    case ["remove", package]:
        remove_package(package)
```
**收益**: 代码清晰，易于添加新命令

### 2. **HTTP 响应处理**
根据状态码和响应内容处理不同情况：
```python
match response:
    case {"status": 200, "data": data}:
        process_data(data)
    case {"status": 404}:
        handle_not_found()
```
**收益**: 结构化处理 API 响应

### 3. **AST (抽象语法树) 访问器**
遍历和处理抽象语法树节点：
```python
match node:
    case BinOp(left, Add(), right):
        return eval_node(left) + eval_node(right)
    case UnaryOp(USub(), operand):
        return -eval_node(operand)
```
**收益**: 编译器、解释器开发更简洁

### 4. **配置文件验证**
验证和解析复杂的配置结构：
```python
match config:
    case {"database": {"host": h, "port": p}}:
        connect_db(h, p)
    case {"database": str(conn_string)}:
        connect_db_string(conn_string)
```
**收益**: 支持多种配置格式

### 5. **事件处理系统**
处理不同类型的事件消息：
```python
match event:
    case {"type": "click", "x": x, "y": y}:
        handle_click(x, y)
    case {"type": "keypress", "key": key}:
        handle_keypress(key)
```
**收益**: 事件分发逻辑清晰

### 6. **数据验证**
验证数据结构是否符合预期格式：
```python
match user_data:
    case {"username": str(name), "age": int(age)} if age >= 18:
        create_user(name, age)
    case _:
        raise ValueError("无效的用户数据")
```
**收益**: 类型检查和结构验证合一

### 7. **状态机实现**
实现复杂的状态转换逻辑：
```python
match (current_state, event):
    case ("idle", "start"):
        return "running"
    case ("running", "pause"):
        return "paused"
```
**收益**: 状态转换表达更直观

### 8. **路由系统**
Web 框架中的 URL 路由匹配：
```python
match path.split("/"):
    case ["", "users", user_id]:
        return get_user(user_id)
    case ["", "posts", post_id, "comments"]:
        return get_comments(post_id)
```
**收益**: 路由规则清晰可读

### 9. **JSON 数据处理**
处理不确定结构的 JSON 数据：
```python
match json_data:
    case {"type": "user", "data": {"id": uid, **rest}}:
        process_user(uid, rest)
    case {"type": "post", "data": post_data}:
        process_post(post_data)
```
**收益**: 适应多种 JSON 格式

### 10. **游戏逻辑**
处理游戏中的各种操作和碰撞检测：
```python
match (player_action, game_state):
    case ("jump", {"on_ground": True}):
        player.jump()
    case ("attack", {"enemy_nearby": True}):
        player.attack()
```
**收益**: 游戏规则表达清晰

## 示例代码说明

本目录的 `examples/` 包含 **10 个独立场景示例** 和 **1 个综合示例**。

运行示例：
```bash
cd curriculum/v3_10/01_match_case/examples
python 01_basic_patterns.py
```

**注意**: 所有示例需要 Python 3.10+。

## 注意事项

### ⚠️ 常见陷阱

1. **match 不是简单的 switch**
   ```python
   # match 会解构，不仅仅是比较值
   match [1, 2]:
       case [x, y]:  # ✅ 匹配并解构
           print(x, y)  # 输出: 1 2
   ```

2. **顺序很重要**
   ```python
   match value:
       case _:  # 通配符会匹配所有
           print("默认")
       case 1:  # ⚠️ 永远不会执行到这里
           print("一")
   ```

3. **字典模式不需要完全匹配**
   ```python
   match {"a": 1, "b": 2, "c": 3}:
       case {"a": x}:  # ✅ 只匹配部分键
           print(x)  # 输出: 1
   ```

4. **类模式需要 __match_args__**
   ```python
   class Point:
       __match_args__ = ("x", "y")  # 必须定义
       def __init__(self, x, y):
           self.x = x
           self.y = y
   
   match Point(1, 2):
       case Point(x, y):  # 现在可以按位置匹配
           print(x, y)
   ```

5. **守卫中不能赋值**
   ```python
   match x:
       case y if (z := y * 2) > 10:  # ✅ 可以使用 walrus operator
           print(z)
   ```

6. **变量捕获 vs 字面量**
   ```python
   MAX = 100
   match value:
       case MAX:  # ⚠️ 这会捕获到变量 MAX，而不是比较
           print("匹配")
   
   # 正确做法：使用守卫
   match value:
       case x if x == MAX:
           print("等于 MAX")
   ```

### ✅ 最佳实践

1. **使用 case _ 作为默认分支** - 避免遗漏情况
2. **守卫条件保持简单** - 复杂逻辑移到函数中
3. **优先使用结构匹配** - 而不是在 guard 中做类型检查
4. **为自定义类定义 __match_args__** - 支持位置模式
5. **利用 IDE 的穷尽性检查** - 确保覆盖所有情况
6. **复杂模式添加注释** - 提高可读性

## 与其他版本的关系

- **Python 3.9**: 不支持 match/case
- **Python 3.10+**: 完整支持
- **向后兼容**: match/case 是新语法，旧版本会语法错误

**迁移建议**:
```python
# 旧代码 (Python 3.9)
if command[0] == "move":
    direction, steps = command[1], command[2]
elif command[0] == "rotate":
    angle = command[1]

# 新代码 (Python 3.10+)
match command:
    case ["move", direction, steps]:
        ...
    case ["rotate", angle]:
        ...
```

## 扩展阅读

- [PEP 634 – Structural Pattern Matching: Specification](https://peps.python.org/pep-0634/)
- [PEP 635 – Structural Pattern Matching: Motivation and Rationale](https://peps.python.org/pep-0635/)
- [PEP 636 – Structural Pattern Matching: Tutorial](https://peps.python.org/pep-0636/)
- [Python 3.10 新特性文档](https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching)

## 快速检查清单

- [ ] 理解 match/case 和 switch/case 的区别
- [ ] 能够使用序列模式解构列表和元组
- [ ] 能够使用映射模式匹配字典
- [ ] 了解如何使用守卫条件
- [ ] 知道类模式需要 __match_args__
- [ ] 理解通配符 `_` 和 `*rest` 的用法
- [ ] 能够组合多种模式（OR、AS）
- [ ] 注意 case 分支的顺序

## 性能说明

match/case 的性能与等价的 if/elif 链基本相同：
- 编译器会进行优化
- 对于简单的字面量匹配，可能使用跳转表
- 复杂的结构匹配会转换为相应的类型检查和解构操作
- 不会有显著的性能开销

