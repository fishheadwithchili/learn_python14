"""
场景 8：路由系统

应用：Web 框架中的 URL 路由匹配和处理
运行要求：Python >= 3.10
"""

print("=" * 60)
print("场景 8：路由系统")
print("=" * 60)

# 示例 1：RESTful API 路由
print("\n[示例 1] RESTful API 路由匹配：\n")

def route_api_request(method, path_parts):
    """路由 API 请求"""
    match (method, path_parts):
        # 用户相关路由
        case ("GET", ["api", "users"]):
            return "📋 获取用户列表"
        case ("GET", ["api", "users", user_id]):
            return f"👤 获取用户 {user_id}"
        case ("POST", ["api", "users"]):
            return "➕ 创建新用户"
        case ("PUT", ["api", "users", user_id]):
            return f"✏️  更新用户 {user_id}"
        case ("DELETE", ["api", "users", user_id]):
            return f"🗑️  删除用户 {user_id}"
        
        # 文章相关路由
        case ("GET", ["api", "posts"]):
            return "📋 获取文章列表"
        case ("GET", ["api", "posts", post_id]):
            return f"📄 获取文章 {post_id}"
        case ("GET", ["api", "posts", post_id, "comments"]):
            return f"💬 获取文章 {post_id} 的评论"
        case ("POST", ["api", "posts"]):
            return "➕ 创建新文章"
        case ("POST", ["api", "posts", post_id, "comments"]):
            return f"💬 为文章 {post_id} 添加评论"
        
        # 搜索路由
        case ("GET", ["api", "search"]):
            return "🔍 执行搜索"
        
        # 404
        case _:
            return "❌ 404 Not Found"

# 测试路由
api_requests = [
    ("GET", ["api", "users"]),
    ("GET", ["api", "users", "123"]),
    ("POST", ["api", "users"]),
    ("PUT", ["api", "users", "456"]),
    ("DELETE", ["api", "users", "789"]),
    ("GET", ["api", "posts"]),
    ("GET", ["api", "posts", "42"]),
    ("GET", ["api", "posts", "42", "comments"]),
    ("POST", ["api", "posts"]),
    ("POST", ["api", "posts", "42", "comments"]),
    ("GET", ["api", "search"]),
    ("GET", ["api", "invalid", "route"])
]

for method, path in api_requests:
    path_str = "/" + "/".join(path)
    result = route_api_request(method, path)
    print(f"{method:6s} {path_str:35s} -> {result}")

# 示例 2：静态文件路由
print("\n[示例 2] 静态文件路由：\n")

def route_static_file(path_parts):
    """路由静态文件请求"""
    match path_parts:
        case ["static", "css", *rest]:
            filename = "/".join(rest)
            return f"🎨 CSS 文件: {filename}"
        case ["static", "js", *rest]:
            filename = "/".join(rest)
            return f"📜 JavaScript 文件: {filename}"
        case ["static", "images", *rest]:
            filename = "/".join(rest)
            return f"🖼️  图片文件: {filename}"
        case ["static", "fonts", *rest]:
            filename = "/".join(rest)
            return f"🔤 字体文件: {filename}"
        case ["favicon.ico"]:
            return "⭐ Favicon"
        case ["robots.txt"]:
            return "🤖 Robots.txt"
        case _:
            return "❌ 静态文件未找到"

# 测试静态文件路由
static_paths = [
    ["static", "css", "style.css"],
    ["static", "css", "themes", "dark.css"],
    ["static", "js", "app.js"],
    ["static", "js", "vendor", "jquery.min.js"],
    ["static", "images", "logo.png"],
    ["static", "images", "icons", "user.svg"],
    ["static", "fonts", "roboto.woff2"],
    ["favicon.ico"],
    ["robots.txt"],
    ["unknown.txt"]
]

for path in static_paths:
    path_str = "/" + "/".join(path)
    result = route_static_file(path)
    print(f"{path_str:45s} -> {result}")

# 示例 3：带参数的路由
print("\n[示例 3] 带查询参数的路由：\n")

def route_with_params(path_parts, params):
    """处理带参数的路由"""
    match (path_parts, params):
        case (["api", "search"], {"q": query, "page": int(page)}):
            return f"🔍 搜索 '{query}'，第 {page} 页"
        case (["api", "search"], {"q": query}):
            return f"🔍 搜索 '{query}'（第 1 页）"
        case (["api", "users"], {"role": role, "active": "true"}):
            return f"📋 获取活跃的 {role} 用户"
        case (["api", "posts"], {"category": cat, "sort": sort}):
            return f"📋 获取 {cat} 分类的文章，排序: {sort}"
        case _:
            return "❌ 无效的请求"

# 测试带参数的路由
param_requests = [
    (["api", "search"], {"q": "Python", "page": 2}),
    (["api", "search"], {"q": "JavaScript"}),
    (["api", "users"], {"role": "admin", "active": "true"}),
    (["api", "posts"], {"category": "tech", "sort": "date"}),
]

for path, params in param_requests:
    path_str = "/" + "/".join(path)
    param_str = "&".join([f"{k}={v}" for k, v in params.items()])
    result = route_with_params(path, params)
    print(f"{path_str}?{param_str}")
    print(f"  -> {result}\n")

# 示例 4：嵌套资源路由
print("[示例 4] 嵌套资源路由：\n")

def route_nested_resources(method, path_parts):
    """处理嵌套资源路由"""
    match (method, path_parts):
        # /users/:user_id/posts
        case ("GET", ["users", user_id, "posts"]):
            return f"📋 获取用户 {user_id} 的所有文章"
        case ("POST", ["users", user_id, "posts"]):
            return f"➕ 为用户 {user_id} 创建文章"
        
        # /users/:user_id/posts/:post_id
        case ("GET", ["users", user_id, "posts", post_id]):
            return f"📄 获取用户 {user_id} 的文章 {post_id}"
        case ("PUT", ["users", user_id, "posts", post_id]):
            return f"✏️  更新用户 {user_id} 的文章 {post_id}"
        case ("DELETE", ["users", user_id, "posts", post_id]):
            return f"🗑️  删除用户 {user_id} 的文章 {post_id}"
        
        # /posts/:post_id/comments
        case ("GET", ["posts", post_id, "comments"]):
            return f"💬 获取文章 {post_id} 的所有评论"
        case ("POST", ["posts", post_id, "comments"]):
            return f"💬 为文章 {post_id} 添加评论"
        
        # /posts/:post_id/comments/:comment_id
        case ("GET", ["posts", post_id, "comments", comment_id]):
            return f"💬 获取文章 {post_id} 的评论 {comment_id}"
        case ("DELETE", ["posts", post_id, "comments", comment_id]):
            return f"🗑️  删除文章 {post_id} 的评论 {comment_id}"
        
        case _:
            return "❌ 404 Not Found"

# 测试嵌套资源路由
nested_requests = [
    ("GET", ["users", "alice", "posts"]),
    ("POST", ["users", "alice", "posts"]),
    ("GET", ["users", "alice", "posts", "123"]),
    ("PUT", ["users", "alice", "posts", "123"]),
    ("DELETE", ["users", "alice", "posts", "123"]),
    ("GET", ["posts", "456", "comments"]),
    ("POST", ["posts", "456", "comments"]),
    ("GET", ["posts", "456", "comments", "789"]),
    ("DELETE", ["posts", "456", "comments", "789"])
]

for method, path in nested_requests:
    path_str = "/" + "/".join(path)
    result = route_nested_resources(method, path)
    print(f"{method:6s} {path_str:40s} -> {result}")

# 示例 5：版本化 API 路由
print("\n[示例 5] 版本化 API 路由：\n")

def route_versioned_api(version, method, path_parts):
    """处理版本化 API 路由"""
    match (version, method, path_parts):
        # v1 API
        case ("v1", "GET", ["users"]):
            return "📋 [V1] 获取用户列表（旧格式）"
        case ("v1", "GET", ["users", user_id]):
            return f"👤 [V1] 获取用户 {user_id}（旧格式）"
        
        # v2 API
        case ("v2", "GET", ["users"]):
            return "📋 [V2] 获取用户列表（新格式，包含更多字段）"
        case ("v2", "GET", ["users", user_id]):
            return f"👤 [V2] 获取用户 {user_id}（新格式，包含头像）"
        case ("v2", "GET", ["users", user_id, "profile"]):
            return f"📝 [V2] 获取用户 {user_id} 的详细资料（新功能）"
        
        # v3 API
        case ("v3", "GET", ["users"]):
            return "📋 [V3] 获取用户列表（最新格式，分页优化）"
        case ("v3", "GET", ["users", user_id]):
            return f"👤 [V3] 获取用户 {user_id}（GraphQL 风格）"
        
        case _:
            return f"❌ API {version} 不支持此路由"

# 测试版本化 API
versioned_requests = [
    ("v1", "GET", ["users"]),
    ("v1", "GET", ["users", "123"]),
    ("v2", "GET", ["users"]),
    ("v2", "GET", ["users", "123"]),
    ("v2", "GET", ["users", "123", "profile"]),
    ("v3", "GET", ["users"]),
    ("v3", "GET", ["users", "123"]),
    ("v1", "GET", ["users", "123", "profile"])
]

for version, method, path in versioned_requests:
    path_str = f"/{version}/" + "/".join(path)
    result = route_versioned_api(version, method, path)
    print(f"{method:6s} {path_str:35s} -> {result}")

# 示例 6：简单路由器类
print("\n[示例 6] 简单路由器类实现：\n")

class SimpleRouter:
    """简单的路由器"""
    
    def route(self, method, path):
        """路由请求"""
        # 解析路径
        parts = [p for p in path.split("/") if p]
        
        match (method, parts):
            case ("GET", []):
                return self.index()
            case ("GET", ["about"]):
                return self.about()
            case ("GET", ["contact"]):
                return self.contact()
            case ("GET", ["products"]):
                return self.products_list()
            case ("GET", ["products", product_id]):
                return self.product_detail(product_id)
            case ("POST", ["api", "orders"]):
                return self.create_order()
            case _:
                return self.not_found()
    
    def index(self):
        return "🏠 首页"
    
    def about(self):
        return "ℹ️  关于我们"
    
    def contact(self):
        return "📧 联系方式"
    
    def products_list(self):
        return "📦 产品列表"
    
    def product_detail(self, product_id):
        return f"📦 产品详情: {product_id}"
    
    def create_order(self):
        return "🛒 创建订单"
    
    def not_found(self):
        return "❌ 404 Page Not Found"

# 测试路由器
router = SimpleRouter()

routes = [
    ("GET", "/"),
    ("GET", "/about"),
    ("GET", "/contact"),
    ("GET", "/products"),
    ("GET", "/products/laptop-123"),
    ("POST", "/api/orders"),
    ("GET", "/nonexistent")
]

for method, path in routes:
    result = router.route(method, path)
    print(f"{method:6s} {path:25s} -> {result}")

print("\n💡 总结：match/case 使路由逻辑清晰直观，易于维护和扩展")

