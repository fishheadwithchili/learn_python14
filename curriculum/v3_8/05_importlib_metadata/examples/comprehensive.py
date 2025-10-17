"""
importlib.metadata 实战示例：项目依赖健康检查工具

业务场景：
构建一个依赖审计工具，用于：
1. 检查关键依赖是否已安装
2. 验证依赖版本是否满足要求
3. 生成依赖许可证报告
4. 统计环境中的包信息

演示 importlib.metadata 在依赖管理中的应用。

运行要求：Python >= 3.8
"""

from importlib import metadata
from typing import Dict, List, Optional
import sys

# ============ 依赖配置 ============

# 项目的关键依赖要求
REQUIRED_DEPENDENCIES = {
    'pip': '20.0.0',      # 包管理器
    'setuptools': '50.0.0',  # 构建工具
}

# 可选依赖（用于特定功能）
OPTIONAL_DEPENDENCIES = {
    'requests': '2.25.0',    # HTTP 客户端
    'numpy': '1.20.0',       # 数值计算
    'pytest': '6.0.0',       # 测试框架
}


# ============ 依赖检查函数 ============

def check_package_installed(package_name: str) -> Optional[str]:
    """检查包是否已安装，返回版本号或 None"""
    try:
        return metadata.version(package_name)
    except metadata.PackageNotFoundError:
        return None


def compare_versions(installed: str, required: str) -> bool:
    """简单的版本比较（实际项目应使用 packaging 库）"""
    installed_parts = [int(x) for x in installed.split('.')[:3]]
    required_parts = [int(x) for x in required.split('.')[:3]]
    
    # 补齐到 3 位
    while len(installed_parts) < 3:
        installed_parts.append(0)
    while len(required_parts) < 3:
        required_parts.append(0)
    
    return installed_parts >= required_parts


def check_dependencies(deps: Dict[str, str], optional: bool = False) -> Dict:
    """检查一组依赖"""
    results = {
        'passed': [],
        'failed': [],
        'missing': []
    }
    
    for package, min_version in deps.items():
        installed_version = check_package_installed(package)
        
        if installed_version is None:
            results['missing'].append({
                'package': package,
                'required': min_version
            })
        elif not compare_versions(installed_version, min_version):
            results['failed'].append({
                'package': package,
                'installed': installed_version,
                'required': min_version
            })
        else:
            results['passed'].append({
                'package': package,
                'installed': installed_version,
                'required': min_version
            })
    
    return results


# ============ 元数据提取 ============

def get_package_info(package_name: str) -> Dict:
    """获取包的详细信息"""
    try:
        version = metadata.version(package_name)
        meta = metadata.metadata(package_name)
        
        return {
            'name': package_name,
            'version': version,
            'author': meta.get('Author', 'Unknown'),
            'license': meta.get('License', 'Unknown'),
            'homepage': meta.get('Home-page', 'N/A'),
            'summary': meta.get('Summary', 'N/A')
        }
    except metadata.PackageNotFoundError:
        return None


def scan_all_packages() -> List[Dict]:
    """扫描环境中所有已安装的包"""
    packages = []
    
    for dist in metadata.distributions():
        packages.append({
            'name': dist.name,
            'version': dist.version
        })
    
    return sorted(packages, key=lambda x: x['name'].lower())


def generate_license_report() -> Dict[str, List[str]]:
    """生成许可证报告"""
    license_map = {}
    
    for dist in metadata.distributions():
        meta = dist.metadata
        license_type = meta.get('License', 'Unknown')
        
        if license_type not in license_map:
            license_map[license_type] = []
        
        license_map[license_type].append(dist.name)
    
    return license_map


# ============ 报告生成 ============

def print_dependency_report():
    """打印完整的依赖报告"""
    print("=" * 70)
    print("项目依赖健康检查报告")
    print("=" * 70)
    print(f"Python 版本: {sys.version.split()[0]}")
    print(f"平台: {sys.platform}")
    
    # 检查必需依赖
    print("\n" + "─" * 70)
    print("[必需依赖检查]")
    print("─" * 70)
    
    required_results = check_dependencies(REQUIRED_DEPENDENCIES)
    
    if required_results['passed']:
        print("\n✅ 通过:")
        for item in required_results['passed']:
            print(f"  • {item['package']}: {item['installed']} "
                  f"(>= {item['required']})")
    
    if required_results['failed']:
        print("\n⚠️  版本过低:")
        for item in required_results['failed']:
            print(f"  • {item['package']}: {item['installed']} "
                  f"(需要 >= {item['required']})")
    
    if required_results['missing']:
        print("\n❌ 缺失:")
        for item in required_results['missing']:
            print(f"  • {item['package']} (需要 >= {item['required']})")
    
    # 检查可选依赖
    print("\n" + "─" * 70)
    print("[可选依赖检查]")
    print("─" * 70)
    
    optional_results = check_dependencies(OPTIONAL_DEPENDENCIES, optional=True)
    
    if optional_results['passed']:
        print("\n✅ 已安装:")
        for item in optional_results['passed']:
            print(f"  • {item['package']}: {item['installed']}")
    
    if optional_results['missing']:
        print("\n💡 未安装（可选）:")
        for item in optional_results['missing']:
            print(f"  • {item['package']}")
    
    # 包详细信息示例
    print("\n" + "─" * 70)
    print("[包详细信息示例]")
    print("─" * 70)
    
    sample_packages = ['pip', 'setuptools']
    for pkg_name in sample_packages:
        info = get_package_info(pkg_name)
        if info:
            print(f"\n{info['name']} ({info['version']}):")
            print(f"  作者: {info['author']}")
            print(f"  许可证: {info['license']}")
            print(f"  主页: {info['homepage']}")
    
    # 环境统计
    print("\n" + "─" * 70)
    print("[环境统计]")
    print("─" * 70)
    
    all_packages = scan_all_packages()
    print(f"\n已安装包总数: {len(all_packages)}")
    
    # 显示前 10 个包
    print(f"\n前 10 个包（按字母排序）:")
    for pkg in all_packages[:10]:
        print(f"  • {pkg['name']} ({pkg['version']})")
    
    if len(all_packages) > 10:
        print(f"  ... 还有 {len(all_packages) - 10} 个包")
    
    # 许可证报告
    print("\n" + "─" * 70)
    print("[许可证分布]")
    print("─" * 70)
    
    licenses = generate_license_report()
    print(f"\n共发现 {len(licenses)} 种许可证类型:")
    
    # 按包数量排序，显示前 5 个
    sorted_licenses = sorted(licenses.items(), 
                            key=lambda x: len(x[1]), 
                            reverse=True)[:5]
    
    for license_type, packages in sorted_licenses:
        print(f"\n{license_type}: {len(packages)} 个包")
        # 显示前 3 个
        for pkg in packages[:3]:
            print(f"  • {pkg}")
        if len(packages) > 3:
            print(f"  ... 还有 {len(packages) - 3} 个")
    
    # 总结
    print("\n" + "=" * 70)
    print("报告生成完成")
    print("=" * 70)
    
    # 给出建议
    all_failed = required_results['failed'] + required_results['missing']
    if all_failed:
        print("\n⚠️  发现问题！建议执行:")
        for item in all_failed:
            pkg = item['package']
            ver = item.get('required', item.get('installed', ''))
            print(f"  pip install --upgrade '{pkg}>={ver}'")
    else:
        print("\n✅ 所有必需依赖检查通过！")


# ============ 主函数 ============

def main():
    print_dependency_report()


if __name__ == "__main__":
    main()

