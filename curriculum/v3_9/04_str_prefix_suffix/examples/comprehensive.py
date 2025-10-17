"""
综合示例：文本处理工具集

场景：构建一个通用的文本处理工具集，整合路径处理、URL解析、
配置解析、数据清洗等功能，展示 removeprefix/removesuffix 的综合应用。
"""

import re
from typing import Optional

# ============= 路径工具 =============

class PathUtils:
    """路径处理工具"""
    
    @staticmethod
    def make_relative(path: str, base: str) -> str:
        """将绝对路径转为相对路径"""
        # 确保 base 以斜杠结尾
        if not base.endswith("/"):
            base += "/"
        return path.removeprefix(base)
    
    @staticmethod
    def remove_extension(filename: str, extension: str = None) -> str:
        """移除文件扩展名"""
        if extension:
            return filename.removesuffix(extension)
        # 移除任意扩展名
        if "." in filename:
            return filename.rsplit(".", 1)[0]
        return filename
    
    @staticmethod
    def normalize_path(path: str) -> str:
        """规范化路径（移除尾部斜杠）"""
        return path.removesuffix("/").removesuffix("\\")


# ============= URL工具 =============

class URLUtils:
    """URL 处理工具"""
    
    @staticmethod
    def remove_protocol(url: str) -> str:
        """移除协议前缀"""
        protocols = ["https://", "http://", "ftp://", "ws://", "wss://"]
        for protocol in protocols:
            url = url.removeprefix(protocol)
        return url
    
    @staticmethod
    def extract_domain(url: str) -> str:
        """提取域名"""
        url_without_protocol = URLUtils.remove_protocol(url)
        return url_without_protocol.split("/")[0]
    
    @staticmethod
    def extract_path(url: str) -> str:
        """提取路径部分"""
        url_without_protocol = URLUtils.remove_protocol(url)
        parts = url_without_protocol.split("/", 1)
        return "/" + parts[1] if len(parts) > 1 else "/"
    
    @staticmethod
    def to_https(url: str) -> str:
        """转换为 HTTPS"""
        url = URLUtils.remove_protocol(url)
        return "https://" + url


# ============= 配置工具 =============

class ConfigUtils:
    """配置处理工具"""
    
    @staticmethod
    def parse_env_var(key: str, value: str, prefix: str = "APP_") -> tuple[str, any]:
        """解析环境变量"""
        clean_key = key.removeprefix(prefix).lower()
        
        # 类型转换
        if value.lower() in ["true", "false"]:
            typed_value = value.lower() == "true"
        else:
            try:
                typed_value = int(value)
            except ValueError:
                try:
                    typed_value = float(value)
                except ValueError:
                    typed_value = value
        
        return clean_key, typed_value
    
    @staticmethod
    def parse_ini_line(line: str) -> Optional[tuple[str, str]]:
        """解析 INI 配置行"""
        line = line.strip()
        
        # 移除注释
        if line.startswith("#") or line.startswith(";"):
            return None
        
        # 解析键值对
        if "=" in line:
            key, value = line.split("=", 1)
            return key.strip(), value.strip()
        
        return None


# ============= 数据清洗工具 =============

class DataCleanUtils:
    """数据清洗工具"""
    
    @staticmethod
    def remove_prefix_tag(text: str, tags: list[str]) -> str:
        """移除标签前缀"""
        for tag in tags:
            text = text.removeprefix(tag).strip()
        return text
    
    @staticmethod
    def extract_numeric_value(text: str, units: list[str]) -> tuple[Optional[float], Optional[str]]:
        """提取数值和单位"""
        for unit in sorted(units, key=len, reverse=True):
            if text.endswith(unit):
                numeric_part = text.removesuffix(unit)
                try:
                    return float(numeric_part), unit
                except ValueError:
                    pass
        return None, None
    
    @staticmethod
    def clean_quotes(text: str) -> str:
        """移除引号"""
        return text.strip().removeprefix('"').removesuffix('"').removeprefix("'").removesuffix("'")


# ============= 日志工具 =============

class LogUtils:
    """日志处理工具"""
    
    @staticmethod
    def parse_log_level(log_line: str) -> tuple[Optional[str], str]:
        """提取日志级别"""
        levels = ["[ERROR]", "[WARNING]", "[INFO]", "[DEBUG]"]
        
        for level in levels:
            if level in log_line:
                level_name = level.removeprefix("[").removesuffix("]")
                message = log_line.split(level, 1)[1].strip()
                return level_name, message
        
        return None, log_line


# ============= 主程序演示 =============

def main():
    print("=" * 70)
    print("综合示例：文本处理工具集")
    print("=" * 70)
    
    # 演示 1：路径处理
    print("\n[演示 1] 路径处理\n")
    
    base_path = "/home/user/projects/myapp"
    full_paths = [
        "/home/user/projects/myapp/src/main.py",
        "/home/user/projects/myapp/tests/test_main.py"
    ]
    
    print(f"项目根目录: {base_path}")
    for path in full_paths:
        relative = PathUtils.make_relative(path, base_path)
        print(f"  {path}")
        print(f"  → {relative}")
    
    # 文件扩展名
    filename = "document.pdf"
    basename = PathUtils.remove_extension(filename, ".pdf")
    print(f"\n文件: {filename} → 基础名: {basename}")
    
    # 演示 2：URL 处理
    print("\n[演示 2] URL 处理\n")
    
    test_url = "http://api.example.com/v1/users/123"
    
    print(f"原始 URL: {test_url}")
    print(f"  域名: {URLUtils.extract_domain(test_url)}")
    print(f"  路径: {URLUtils.extract_path(test_url)}")
    print(f"  HTTPS: {URLUtils.to_https(test_url)}")
    
    # 演示 3：配置解析
    print("\n[演示 3] 配置解析\n")
    
    env_vars = [
        ("APP_DATABASE_URL", "postgresql://localhost/mydb"),
        ("APP_DEBUG", "true"),
        ("APP_PORT", "8000")
    ]
    
    print("环境变量解析:")
    config = {}
    for key, value in env_vars:
        clean_key, typed_value = ConfigUtils.parse_env_var(key, value)
        config[clean_key] = typed_value
        print(f"  {key} = {value}")
        print(f"    → {clean_key}: {typed_value} ({type(typed_value).__name__})")
    
    # 演示 4：数据清洗
    print("\n[演示 4] 数据清洗\n")
    
    # 移除标签
    tagged_messages = [
        "[URGENT] Server down",
        "[INFO] User logged in"
    ]
    
    tags = ["[URGENT]", "[INFO]", "[ERROR]"]
    
    print("移除标签:")
    for msg in tagged_messages:
        clean = DataCleanUtils.remove_prefix_tag(msg, tags)
        print(f"  {msg} → {clean}")
    
    # 提取数值
    measurements = ["100px", "50%", "2.5kg"]
    units = ["px", "%", "kg", "sec"]
    
    print("\n提取数值和单位:")
    for measurement in measurements:
        value, unit = DataCleanUtils.extract_numeric_value(measurement, units)
        if value is not None:
            print(f"  {measurement} → 数值: {value}, 单位: {unit}")
    
    # 演示 5：日志解析
    print("\n[演示 5] 日志解析\n")
    
    log_lines = [
        "[2023-06-15 10:30:00] [ERROR] Database connection failed",
        "[2023-06-15 10:30:01] [INFO] Retry successful"
    ]
    
    print("解析日志:")
    for log in log_lines:
        level, message = LogUtils.parse_log_level(log)
        print(f"  [{level}] {message}")
    
    # 演示 6：综合处理流程
    print("\n[演示 6] 综合处理流程\n")
    
    # 场景：处理 API 日志，提取关键信息
    api_log = "https://api.example.com/v1/users?page=1"
    
    print(f"API 请求日志: {api_log}")
    
    # 步骤 1：移除协议
    step1 = URLUtils.remove_protocol(api_log)
    print(f"  1. 移除协议: {step1}")
    
    # 步骤 2：提取域名
    step2 = URLUtils.extract_domain(api_log)
    print(f"  2. 提取域名: {step2}")
    
    # 步骤 3：提取路径
    step3 = URLUtils.extract_path(api_log)
    print(f"  3. 提取路径: {step3}")
    
    # 步骤 4：移除查询参数
    if "?" in step3:
        path_only = step3.split("?")[0]
        print(f"  4. 纯路径: {path_only}")
    
    # 总结
    print("\n" + "=" * 70)
    print("💡 总结")
    print("=" * 70)
    print()
    print("removeprefix/removesuffix 的综合应用：")
    print("  ✅ 路径处理 - 相对路径转换、扩展名移除")
    print("  ✅ URL 解析 - 协议移除、域名提取")
    print("  ✅ 配置解析 - 前缀移除、类型转换")
    print("  ✅ 数据清洗 - 标签移除、单位提取")
    print("  ✅ 日志处理 - 级别提取、消息解析")
    print()
    print("优势：")
    print("  • 代码简洁明了")
    print("  • 避免手动切片错误")
    print("  • 意图清晰")
    print("  • 易于维护")


if __name__ == "__main__":
    main()

