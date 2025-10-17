"""
场景 2：命令行参数解析

应用：解析和处理命令行工具的各种命令格式
运行要求：Python >= 3.10
"""

print("=" * 60)
print("场景 2：命令行参数解析")
print("=" * 60)

# 示例 1：简单命令解析
print("\n[示例 1] 包管理器命令解析：\n")

def parse_package_command(args):
    """解析包管理器命令（类似 pip, npm）"""
    match args:
        case ["install", package]:
            return f"📦 安装包: {package}"
        case ["install", package, "--global"]:
            return f"🌍 全局安装包: {package}"
        case ["uninstall", package]:
            return f"🗑️  卸载包: {package}"
        case ["update", package]:
            return f"⬆️  更新包: {package}"
        case ["update"]:
            return "⬆️  更新所有包"
        case ["list"]:
            return "📋 列出所有包"
        case ["search", query]:
            return f"🔍 搜索: {query}"
        case _:
            return "❌ 无效命令。使用 'help' 查看帮助"

# 测试各种命令
commands = [
    ["install", "numpy"],
    ["install", "flask", "--global"],
    ["uninstall", "pandas"],
    ["update", "requests"],
    ["update"],
    ["list"],
    ["search", "tensorflow"],
    ["invalid"]
]

for cmd in commands:
    print(f"$ pkg {' '.join(cmd)}")
    print(f"  {parse_package_command(cmd)}\n")

# 示例 2：Git 风格命令解析
print("[示例 2] Git 风格命令（子命令 + 选项）：\n")

def parse_git_command(args):
    """解析 Git 风格的命令"""
    match args:
        case ["init"]:
            return "🆕 初始化仓库"
        case ["clone", url]:
            return f"📥 克隆仓库: {url}"
        case ["add", "."]:
            return "➕ 添加所有文件"
        case ["add", *files]:
            return f"➕ 添加文件: {', '.join(files)}"
        case ["commit", "-m", message]:
            return f"💾 提交: {message}"
        case ["push", remote, branch]:
            return f"⬆️  推送到 {remote}/{branch}"
        case ["push"]:
            return "⬆️  推送到默认远程"
        case ["pull"]:
            return "⬇️  拉取更新"
        case ["branch", "-d", branch]:
            return f"🗑️  删除分支: {branch}"
        case ["branch", name]:
            return f"🌿 创建分支: {name}"
        case ["checkout", branch]:
            return f"↔️  切换到分支: {branch}"
        case _:
            return "❌ 无效的 Git 命令"

# 测试 Git 命令
git_commands = [
    ["init"],
    ["clone", "https://github.com/user/repo.git"],
    ["add", "."],
    ["add", "file1.py", "file2.py"],
    ["commit", "-m", "Fix bug"],
    ["push", "origin", "main"],
    ["push"],
    ["pull"],
    ["branch", "feature/new"],
    ["checkout", "develop"],
    ["invalid", "command"]
]

for cmd in git_commands:
    print(f"$ git {' '.join(cmd)}")
    print(f"  {parse_git_command(cmd)}\n")

# 示例 3：带选项的命令解析
print("[示例 3] 服务器管理命令（带选项和参数）：\n")

def parse_server_command(args):
    """解析服务器管理命令"""
    match args:
        case ["start"]:
            return "🟢 启动服务器（默认端口 8000）"
        case ["start", "--port", port]:
            return f"🟢 启动服务器，端口: {port}"
        case ["start", "--port", port, "--host", host]:
            return f"🟢 启动服务器 {host}:{port}"
        case ["stop"]:
            return "🔴 停止服务器"
        case ["restart"]:
            return "🔄 重启服务器"
        case ["status"]:
            return "📊 查看服务器状态"
        case ["logs"]:
            return "📄 显示最新日志"
        case ["logs", "--tail", n]:
            return f"📄 显示最后 {n} 行日志"
        case ["config", "set", key, value]:
            return f"⚙️  设置配置: {key} = {value}"
        case ["config", "get", key]:
            return f"⚙️  获取配置: {key}"
        case _:
            return "❌ 未知命令"

# 测试服务器命令
server_commands = [
    ["start"],
    ["start", "--port", "3000"],
    ["start", "--port", "8080", "--host", "0.0.0.0"],
    ["stop"],
    ["restart"],
    ["status"],
    ["logs"],
    ["logs", "--tail", "50"],
    ["config", "set", "debug", "true"],
    ["config", "get", "database_url"]
]

for cmd in server_commands:
    print(f"$ server {' '.join(cmd)}")
    print(f"  {parse_server_command(cmd)}\n")

# 示例 4：复杂命令解析（带守卫条件）
print("[示例 4] 数据库命令（带验证）：\n")

def parse_db_command(args):
    """解析数据库命令（带参数验证）"""
    match args:
        case ["create", table_name] if table_name.isidentifier():
            return f"✅ 创建表: {table_name}"
        case ["create", invalid_name]:
            return f"❌ 无效的表名: {invalid_name}"
        case ["drop", table_name] if table_name.isidentifier():
            return f"⚠️  删除表: {table_name}"
        case ["insert", table, *values] if len(values) > 0:
            return f"➕ 向 {table} 插入 {len(values)} 个值"
        case ["select", "*", "from", table]:
            return f"📋 查询 {table} 的所有列"
        case ["select", *columns, "from", table]:
            return f"📋 查询 {table} 的列: {', '.join(columns)}"
        case ["update", table, "set", *pairs]:
            return f"✏️  更新 {table}: {len(pairs)//2} 个字段"
        case ["delete", "from", table]:
            return f"🗑️  删除 {table} 的所有记录"
        case _:
            return "❌ 无效的 SQL 命令"

# 测试数据库命令
db_commands = [
    ["create", "users"],
    ["create", "123invalid"],
    ["drop", "old_table"],
    ["insert", "users", "Alice", "25", "alice@example.com"],
    ["select", "*", "from", "users"],
    ["select", "name", "age", "from", "users"],
    ["update", "users", "set", "age", "26"],
    ["delete", "from", "users"]
]

for cmd in db_commands:
    print(f"$ db {' '.join(cmd)}")
    print(f"  {parse_db_command(cmd)}\n")

# 示例 5：子命令分发
print("[示例 5] 多级子命令（类似 docker）：\n")

def parse_docker_command(args):
    """解析 Docker 风格的多级命令"""
    match args:
        case ["container", "ls"]:
            return "📦 列出容器"
        case ["container", "start", container_id]:
            return f"▶️  启动容器: {container_id}"
        case ["container", "stop", container_id]:
            return f"⏹️  停止容器: {container_id}"
        case ["image", "ls"]:
            return "🖼️  列出镜像"
        case ["image", "pull", image]:
            return f"⬇️  拉取镜像: {image}"
        case ["image", "rm", image]:
            return f"🗑️  删除镜像: {image}"
        case ["volume", "create", name]:
            return f"💾 创建卷: {name}"
        case ["network", "create", name]:
            return f"🌐 创建网络: {name}"
        case ["run", *options]:
            return f"🏃 运行容器，选项: {len(options)} 个"
        case _:
            return "❌ 无效的 Docker 命令"

# 测试 Docker 命令
docker_commands = [
    ["container", "ls"],
    ["container", "start", "abc123"],
    ["container", "stop", "xyz789"],
    ["image", "ls"],
    ["image", "pull", "nginx:latest"],
    ["image", "rm", "old-image"],
    ["volume", "create", "data"],
    ["network", "create", "my-network"],
    ["run", "-d", "-p", "80:80", "nginx"]
]

for cmd in docker_commands:
    print(f"$ docker {' '.join(cmd)}")
    print(f"  {parse_docker_command(cmd)}\n")

print("💡 总结：match/case 非常适合解析结构化的命令行参数")

