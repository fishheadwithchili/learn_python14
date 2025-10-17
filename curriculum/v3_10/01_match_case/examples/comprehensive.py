"""
综合示例：命令行任务管理系统

场景：
使用 match/case 实现一个功能完整的任务管理 CLI 工具。
系统特点：
1. 多种命令处理（CRUD 操作）
2. 数据验证和错误处理
3. 状态转换逻辑
4. 复杂的查询和过滤

运行要求：Python >= 3.10
"""

from datetime import datetime, timedelta
from typing import List, Dict, Any

print("=" * 70)
print("综合示例：命令行任务管理系统（基于 match/case）")
print("=" * 70)

# ========== 任务类定义 ==========

class Task:
    """任务类"""
    
    def __init__(self, id: int, title: str, priority: str = "medium"):
        self.id = id
        self.title = title
        self.priority = priority
        self.status = "pending"
        self.created_at = datetime.now()
        self.tags = []
        self.description = ""
        self.due_date = None
    
    def to_dict(self):
        """转为字典"""
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "status": self.status,
            "tags": self.tags,
            "due_date": self.due_date.isoformat() if self.due_date else None
        }


# ========== 任务管理器 ==========

class TaskManager:
    """任务管理器"""
    
    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1
    
    def execute_command(self, command: List[str]) -> str:
        """执行命令（使用 match/case 路由）"""
        match command:
            # 创建任务
            case ["add", title]:
                return self.add_task(title)
            case ["add", title, "--priority", priority]:
                return self.add_task(title, priority)
            case ["add", title, "--priority", priority, "--tags", *tags]:
                return self.add_task(title, priority, tags)
            
            # 列出任务
            case ["list"]:
                return self.list_tasks()
            case ["list", "--status", status]:
                return self.list_tasks(status=status)
            case ["list", "--priority", priority]:
                return self.list_tasks(priority=priority)
            case ["list", "--tag", tag]:
                return self.list_tasks(tag=tag)
            
            # 查看任务详情
            case ["show", task_id]:
                return self.show_task(int(task_id))
            
            # 更新任务
            case ["update", task_id, "--title", new_title]:
                return self.update_task(int(task_id), title=new_title)
            case ["update", task_id, "--priority", new_priority]:
                return self.update_task(int(task_id), priority=new_priority)
            case ["update", task_id, "--status", new_status]:
                return self.update_task(int(task_id), status=new_status)
            
            # 删除任务
            case ["delete", task_id]:
                return self.delete_task(int(task_id))
            
            # 完成任务
            case ["complete", task_id]:
                return self.complete_task(int(task_id))
            
            # 搜索任务
            case ["search", query]:
                return self.search_tasks(query)
            
            # 统计信息
            case ["stats"]:
                return self.get_statistics()
            
            # 帮助
            case ["help"]:
                return self.get_help()
            
            # 未知命令
            case _:
                return f"❌ 未知命令: {' '.join(command)}\n使用 'help' 查看可用命令"
    
    def add_task(self, title: str, priority: str = "medium", tags: List[str] = None) -> str:
        """添加任务"""
        # 使用 match/case 验证优先级
        match priority:
            case "low" | "medium" | "high" | "urgent":
                task = Task(self.next_id, title, priority)
                if tags:
                    task.tags = tags
                self.tasks.append(task)
                self.next_id += 1
                
                icon = {"low": "🔵", "medium": "🟡", "high": "🟠", "urgent": "🔴"}[priority]
                return f"✅ 任务已创建：#{task.id} {task.title} {icon}"
            case _:
                return f"❌ 无效的优先级: {priority} (可选: low, medium, high, urgent)"
    
    def list_tasks(self, status: str = None, priority: str = None, tag: str = None) -> str:
        """列出任务"""
        filtered = self.tasks
        
        # 过滤状态
        if status:
            filtered = [t for t in filtered if t.status == status]
        
        # 过滤优先级
        if priority:
            filtered = [t for t in filtered if t.priority == priority]
        
        # 过滤标签
        if tag:
            filtered = [t for t in filtered if tag in t.tags]
        
        if not filtered:
            return "📭 没有找到任务"
        
        # 使用 match/case 格式化任务列表
        lines = [f"\n📋 任务列表（共 {len(filtered)} 个）:\n"]
        
        for task in filtered:
            # 使用 match/case 选择状态图标
            match task.status:
                case "pending":
                    status_icon = "⏳"
                case "in_progress":
                    status_icon = "🔄"
                case "completed":
                    status_icon = "✅"
                case "cancelled":
                    status_icon = "❌"
                case _:
                    status_icon = "❓"
            
            # 使用 match/case 选择优先级图标
            match task.priority:
                case "low":
                    priority_icon = "🔵"
                case "medium":
                    priority_icon = "🟡"
                case "high":
                    priority_icon = "🟠"
                case "urgent":
                    priority_icon = "🔴"
                case _:
                    priority_icon = "⚪"
            
            tags_str = f" [{', '.join(task.tags)}]" if task.tags else ""
            lines.append(
                f"  {status_icon} #{task.id:3d} {priority_icon} {task.title}{tags_str}"
            )
        
        return "\n".join(lines)
    
    def show_task(self, task_id: int) -> str:
        """显示任务详情"""
        task = self._find_task(task_id)
        
        match task:
            case None:
                return f"❌ 未找到任务 #{task_id}"
            case Task():
                age = datetime.now() - task.created_at
                age_str = f"{age.days} 天前" if age.days > 0 else "今天"
                
                return f"""
📄 任务详情 #{task.id}
{'=' * 50}
标题: {task.title}
状态: {task.status}
优先级: {task.priority}
标签: {', '.join(task.tags) if task.tags else '无'}
创建时间: {task.created_at.strftime('%Y-%m-%d %H:%M')} ({age_str})
描述: {task.description if task.description else '无'}
"""
    
    def update_task(self, task_id: int, **updates) -> str:
        """更新任务"""
        task = self._find_task(task_id)
        
        if not task:
            return f"❌ 未找到任务 #{task_id}"
        
        # 使用 match/case 处理不同的更新类型
        changes = []
        
        for key, value in updates.items():
            match (key, value):
                case ("title", str(new_title)):
                    task.title = new_title
                    changes.append(f"标题 -> {new_title}")
                
                case ("priority", priority) if priority in ["low", "medium", "high", "urgent"]:
                    task.priority = priority
                    changes.append(f"优先级 -> {priority}")
                
                case ("status", status) if status in ["pending", "in_progress", "completed", "cancelled"]:
                    task.status = status
                    changes.append(f"状态 -> {status}")
                
                case (field, invalid_value):
                    return f"❌ 无效的 {field} 值: {invalid_value}"
        
        if changes:
            return f"✅ 任务 #{task_id} 已更新:\n  " + "\n  ".join(changes)
        else:
            return f"⚠️  没有进行任何更改"
    
    def delete_task(self, task_id: int) -> str:
        """删除任务"""
        task = self._find_task(task_id)
        
        match task:
            case None:
                return f"❌ 未找到任务 #{task_id}"
            case Task(status="completed"):
                self.tasks.remove(task)
                return f"✅ 已删除已完成的任务 #{task_id}"
            case Task():
                # 使用 match/case 确认删除
                self.tasks.remove(task)
                return f"🗑️  已删除任务 #{task_id}: {task.title}"
    
    def complete_task(self, task_id: int) -> str:
        """完成任务"""
        task = self._find_task(task_id)
        
        match task:
            case None:
                return f"❌ 未找到任务 #{task_id}"
            case Task(status="completed"):
                return f"⚠️  任务 #{task_id} 已经是完成状态"
            case Task():
                task.status = "completed"
                return f"🎉 任务 #{task_id} 已完成: {task.title}"
    
    def search_tasks(self, query: str) -> str:
        """搜索任务"""
        results = [
            task for task in self.tasks
            if query.lower() in task.title.lower() or
               any(query.lower() in tag.lower() for tag in task.tags)
        ]
        
        match results:
            case []:
                return f"🔍 没有找到包含 '{query}' 的任务"
            case [single_task]:
                return f"🔍 找到 1 个任务:\n  #{single_task.id} {single_task.title}"
            case multiple_tasks:
                lines = [f"🔍 找到 {len(multiple_tasks)} 个任务:"]
                for task in multiple_tasks:
                    lines.append(f"  #{task.id} {task.title}")
                return "\n".join(lines)
    
    def get_statistics(self) -> str:
        """获取统计信息"""
        if not self.tasks:
            return "📊 还没有任务"
        
        # 按状态统计
        status_counts = {}
        for task in self.tasks:
            status_counts[task.status] = status_counts.get(task.status, 0) + 1
        
        # 按优先级统计
        priority_counts = {}
        for task in self.tasks:
            priority_counts[task.priority] = priority_counts.get(task.priority, 0) + 1
        
        # 格式化输出
        lines = [
            "\n📊 任务统计",
            "=" * 50,
            f"总任务数: {len(self.tasks)}",
            "",
            "按状态:",
        ]
        
        for status, count in status_counts.items():
            match status:
                case "pending":
                    icon = "⏳"
                case "in_progress":
                    icon = "🔄"
                case "completed":
                    icon = "✅"
                case _:
                    icon = "❓"
            lines.append(f"  {icon} {status}: {count}")
        
        lines.append("\n按优先级:")
        for priority in ["urgent", "high", "medium", "low"]:
            if priority in priority_counts:
                match priority:
                    case "urgent":
                        icon = "🔴"
                    case "high":
                        icon = "🟠"
                    case "medium":
                        icon = "🟡"
                    case "low":
                        icon = "🔵"
                    case _:
                        icon = "⚪"
                lines.append(f"  {icon} {priority}: {priority_counts[priority]}")
        
        return "\n".join(lines)
    
    def get_help(self) -> str:
        """获取帮助信息"""
        return """
📖 任务管理系统帮助

可用命令:

  add <title>                       添加任务
  add <title> --priority <level>    添加带优先级的任务
  add <title> --priority <level> --tags <tag1> <tag2>  添加带标签的任务
  
  list                              列出所有任务
  list --status <status>            按状态筛选
  list --priority <priority>        按优先级筛选
  list --tag <tag>                  按标签筛选
  
  show <id>                         显示任务详情
  
  update <id> --title <title>       更新标题
  update <id> --priority <level>    更新优先级
  update <id> --status <status>     更新状态
  
  complete <id>                     标记为完成
  delete <id>                       删除任务
  
  search <query>                    搜索任务
  stats                             显示统计信息
  help                              显示此帮助

优先级: low, medium, high, urgent
状态: pending, in_progress, completed, cancelled
"""
    
    def _find_task(self, task_id: int) -> Task | None:
        """查找任务"""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None


# ========== 演示 ==========

def main():
    """主函数"""
    manager = TaskManager()
    
    # 模拟一系列命令
    commands = [
        ["help"],
        ["add", "完成项目文档", "--priority", "high", "--tags", "文档", "项目"],
        ["add", "修复登录bug", "--priority", "urgent"],
        ["add", "代码审查", "--priority", "medium"],
        ["add", "更新依赖包", "--priority", "low"],
        ["add", "编写单元测试"],
        ["list"],
        ["list", "--priority", "high"],
        ["show", "1"],
        ["update", "3", "--status", "in_progress"],
        ["complete", "2"],
        ["list"],
        ["search", "bug"],
        ["stats"],
        ["delete", "2"],
        ["list"],
        ["stats"]
    ]
    
    print("\n" + "=" * 70)
    print("运行演示")
    print("=" * 70)
    
    for i, cmd in enumerate(commands, 1):
        cmd_str = " ".join(cmd)
        print(f"\n{'─' * 70}")
        print(f"命令 {i}: {cmd_str}")
        print("─" * 70)
        
        result = manager.execute_command(cmd)
        print(result)
        
        # 某些命令后暂停显示
        if cmd[0] in ["help"]:
            input("\n按回车继续...")

if __name__ == "__main__":
    main()

print("\n" + "=" * 70)
print("💡 综合示例总结")
print("=" * 70)
print("""
本示例展示了 match/case 在实际项目中的综合应用：

1. **命令路由** - 使用 match/case 解析和分发命令
2. **数据验证** - 使用守卫条件验证输入
3. **状态处理** - 匹配不同状态并执行相应操作
4. **模式组合** - 结合序列、映射、守卫等多种模式
5. **错误处理** - 优雅地处理无效输入和边界情况

match/case 的优势：
✓ 代码结构清晰，易于理解
✓ 添加新功能方便（只需添加新的 case）
✓ 类型安全（结合类型注解）
✓ 减少嵌套的 if/elif
✓ 更接近声明式编程风格
""")

