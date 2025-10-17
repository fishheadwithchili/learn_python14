# `importlib.metadata`

## 一句话总结

标准库提供的包元数据查询接口，用于读取已安装 Python 包的版本、入口点、依赖等信息。

## 功能详解

### 是什么？

`importlib.metadata` 是 Python 3.8 引入的标准库模块，提供了访问已安装 Python 发行版（distribution）元数据的 API。它可以查询包的版本号、依赖关系、入口点、许可证等信息。

**语法格式**:
```python
from importlib import metadata

# 查询包版本
version = metadata.version('requests')

# 查询包的所有元数据
meta = metadata.metadata('requests')

# 查询入口点
entry_points = metadata.entry_points()
```

### 解决什么问题？

**问题 1: 版本检查依赖第三方库**
```python
# 旧方式 - 需要安装 pkg_resources（setuptools 的一部分，启动慢）
import pkg_resources
version = pkg_resources.get_distribution('requests').version

# 新方式 - 标准库，启动快
from importlib import metadata
version = metadata.version('requests')
```

**问题 2: 运行时依赖检查**
```python
# 应用启动时需要验证依赖版本
required_version = '2.28.0'
installed = metadata.version('requests')
if installed < required_version:
    raise RuntimeError(f"需要 requests >= {required_version}")
```

**问题 3: 插件系统实现**
```python
# 旧方式 - 需要硬编码或配置文件
plugins = [Plugin1, Plugin2, Plugin3]

# 新方式 - 通过入口点自动发现
for ep in metadata.entry_points(group='myapp.plugins'):
    plugin_class = ep.load()
    plugins.append(plugin_class())
```

### 语法要点

1. **查询包版本**
   ```python
   from importlib import metadata
   
   version = metadata.version('numpy')
   print(version)  # '1.24.3'
   ```

2. **查询所有元数据**
   ```python
   meta = metadata.metadata('requests')
   print(meta['Author'])        # 'Kenneth Reitz'
   print(meta['License'])       # 'Apache 2.0'
   print(meta['Home-page'])     # 'https://...'
   ```

3. **查询依赖关系**
   ```python
   requires = metadata.requires('flask')
   # ['Werkzeug>=2.0', 'Jinja2>=3.0', ...]
   ```

4. **查询入口点**
   ```python
   # Python 3.10+ 推荐用法
   eps = metadata.entry_points(group='console_scripts')
   
   # Python 3.8-3.9 用法
   eps = metadata.entry_points()
   console_scripts = eps.get('console_scripts', [])
   ```

5. **列出所有已安装包**
   ```python
   distributions = metadata.distributions()
   for dist in distributions:
       print(f"{dist.name} {dist.version}")
   ```

6. **异常处理**
   ```python
   try:
       ver = metadata.version('nonexistent')
   except metadata.PackageNotFoundError:
       print("包未安装")
   ```

## 核心应用场景

### 1. **CLI 工具显示版本信息**
命令行工具需要 `--version` 选项：
```python
import argparse
from importlib import metadata

parser = argparse.ArgumentParser()
parser.add_argument('--version', action='version',
                    version=f"%(prog)s {metadata.version('myapp')}")
```
**收益**: 版本号自动从包元数据读取，无需硬编码

### 2. **依赖健康检查**
应用启动时验证关键依赖的版本：
```python
def check_dependencies():
    required = {
        'django': '4.2.0',
        'celery': '5.3.0',
        'redis': '4.5.0'
    }
    
    for package, min_version in required.items():
        try:
            installed = metadata.version(package)
            if installed < min_version:
                raise RuntimeError(f"{package} 版本过低")
        except metadata.PackageNotFoundError:
            raise RuntimeError(f"{package} 未安装")
```
**收益**: 早期发现依赖问题

### 3. **插件系统实现**
应用支持第三方插件扩展：
```python
def discover_plugins():
    plugins = []
    for ep in metadata.entry_points(group='myapp.plugins'):
        try:
            plugin_class = ep.load()
            plugins.append(plugin_class())
        except Exception as e:
            print(f"加载插件 {ep.name} 失败: {e}")
    return plugins
```
**收益**: 插件自动发现，无需配置文件

### 4. **许可证合规审计**
扫描项目依赖的许可证信息：
```python
def audit_licenses():
    licenses = {}
    for dist in metadata.distributions():
        meta = dist.metadata
        licenses[dist.name] = meta.get('License', 'Unknown')
    return licenses
```
**收益**: 快速生成依赖许可证报告

### 5. **兼容性检测工具**
检查包是否支持当前 Python 版本：
```python
import sys

def check_python_version(package):
    meta = metadata.metadata(package)
    requires_python = meta.get('Requires-Python')
    
    if requires_python:
        # 解析版本约束并检查
        print(f"{package} 需要 Python {requires_python}")
        print(f"当前版本: {sys.version}")
```
**收益**: 提前发现兼容性问题

### 6. **依赖图生成**
可视化项目的依赖关系树：
```python
def build_dependency_tree(package, level=0):
    indent = "  " * level
    print(f"{indent}{package} ({metadata.version(package)})")
    
    try:
        requires = metadata.requires(package)
        if requires:
            for req in requires:
                dep_name = req.split()[0]  # 提取包名
                build_dependency_tree(dep_name, level + 1)
    except Exception:
        pass
```
**收益**: 理解依赖复杂度

### 7. **环境诊断工具**
DevOps 脚本收集环境信息：
```python
def dump_environment():
    print("已安装的包:")
    for dist in metadata.distributions():
        print(f"  {dist.name}=={dist.version}")
```
**收益**: 快速诊断环境差异

### 8. **动态导入验证**
运行时检查可选依赖是否安装：
```python
def get_feature(name):
    feature_deps = {
        'plotting': 'matplotlib',
        'web': 'flask',
        'async': 'aiohttp'
    }
    
    dep = feature_deps.get(name)
    try:
        metadata.version(dep)
        return import_module(dep)
    except metadata.PackageNotFoundError:
        raise RuntimeError(f"功能 {name} 需要安装 {dep}")
```
**收益**: 友好的可选依赖提示

### 9. **包管理器实现**
自定义的包管理工具：
```python
def list_outdated():
    # 列出所有包并检查是否有新版本（需要结合 PyPI API）
    for dist in metadata.distributions():
        current = dist.version
        # 查询 PyPI 获取最新版本
        print(f"{dist.name}: {current}")
```
**收益**: 构建自动化工具

### 10. **测试环境验证**
CI/CD 管道中验证测试环境：
```python
def validate_test_environment():
    required_packages = ['pytest', 'coverage', 'mypy']
    
    missing = []
    for pkg in required_packages:
        try:
            metadata.version(pkg)
        except metadata.PackageNotFoundError:
            missing.append(pkg)
    
    if missing:
        raise RuntimeError(f"缺少测试依赖: {missing}")
```
**收益**: 确保测试环境一致性

## 示例代码说明

本目录的 `example.py` 演示了一个**依赖健康检查工具**的实际应用场景：

- **业务背景**: 构建一个项目依赖审计工具，检查版本、许可证和安全性
- **技术点**:
  - 使用 `metadata.version()` 查询版本
  - 使用 `metadata.metadata()` 提取元数据
  - 使用 `metadata.distributions()` 遍历所有包
  - 演示异常处理和报告生成
- **代码规模**: 约 50 行，模拟真实的依赖管理场景

运行示例：
```bash
python 05_importlib_metadata/example.py
```

## 注意事项

### ⚠️ 常见陷阱

1. **包名和导入名不一致**
   ```python
   # ❌ 错误 - 使用导入名
   metadata.version('PIL')  # PackageNotFoundError
   
   # ✅ 正确 - 使用发行版名称
   metadata.version('Pillow')  # '9.5.0'
   ```

2. **性能考虑**
   ```python
   # ❌ 在循环中重复调用
   for _ in range(1000):
       version = metadata.version('numpy')  # 每次都查询文件系统
   
   # ✅ 缓存结果
   version = metadata.version('numpy')
   for _ in range(1000):
       use_version(version)
   ```

3. **入口点 API 变化**
   ```python
   # Python 3.8-3.9 返回字典
   eps = metadata.entry_points()
   console_scripts = eps.get('console_scripts', [])
   
   # Python 3.10+ 推荐新 API
   eps = metadata.entry_points(group='console_scripts')
   ```

4. **虚拟环境隔离**
   ```python
   # 只能查询当前环境已安装的包
   # 如果在虚拟环境中，看不到系统包（除非使用 --system-site-packages）
   ```

5. **可编辑安装的元数据**
   ```python
   # pip install -e . 的包可能元数据不完整
   try:
       meta = metadata.metadata('myproject')
   except Exception:
       # 可编辑安装可能缺少某些元数据字段
       pass
   ```

### ✅ 最佳实践

1. **使用异常处理**
   ```python
   def safe_version(package, default='0.0.0'):
       try:
           return metadata.version(package)
       except metadata.PackageNotFoundError:
           return default
   ```

2. **缓存频繁查询的结果**
   ```python
   from functools import lru_cache
   
   @lru_cache(maxsize=128)
   def get_version(package):
       return metadata.version(package)
   ```

3. **兼容多个 Python 版本**
   ```python
   import sys
   if sys.version_info >= (3, 10):
       eps = metadata.entry_points(group='console_scripts')
   else:
       eps = metadata.entry_points().get('console_scripts', [])
   ```

4. **记录包名规范化**
   ```python
   # PyPI 包名会被规范化（大写转小写，_ 转 -）
   # 但 metadata API 通常能处理这些变体
   metadata.version('Django')    # OK
   metadata.version('django')    # OK
   metadata.version('some_package')  # OK
   metadata.version('some-package')  # OK
   ```

## 与其他版本的关系

- **Python 3.7**: 不存在，需要使用 `pkg_resources` 或安装 `importlib_metadata` backport
- **Python 3.8+**: 标准库支持
- **Python 3.10**: 改进了 `entry_points()` API
- **替代方案**: `pkg_resources` (重量级，启动慢), `importlib_metadata` (3.7 的 backport)

## 性能对比

```python
import time

# pkg_resources（旧方式）
start = time.time()
import pkg_resources
pkg_resources.get_distribution('requests').version
print(f"pkg_resources: {time.time() - start:.4f}s")
# 输出: ~0.05s（首次导入慢）

# importlib.metadata（新方式）
start = time.time()
from importlib import metadata
metadata.version('requests')
print(f"importlib.metadata: {time.time() - start:.4f}s")
# 输出: ~0.01s（快 5 倍）
```

## 常见包名映射

一些常见的包名和导入名不一致的情况：

| 导入名 | 包名（发行版名） |
|--------|------------------|
| `PIL` | `Pillow` |
| `cv2` | `opencv-python` |
| `yaml` | `PyYAML` |
| `sklearn` | `scikit-learn` |

查找方法：
```python
# 通过导入模块查找对应的发行版
import PIL
dist = metadata.distribution('Pillow')
print(dist.read_text('top_level.txt'))  # PIL
```

## 扩展阅读

- [PEP 566 – Metadata for Python Software Packages 2.1](https://peps.python.org/pep-0566/)
- [importlib.metadata 官方文档](https://docs.python.org/3/library/importlib.metadata.html)
- [Packaging User Guide](https://packaging.python.org/en/latest/)
- [setuptools 入口点文档](https://setuptools.pypa.io/en/latest/userguide/entry_point.html)

## 快速检查清单

学完本特性后，你应该能回答：

- [ ] `importlib.metadata` 和 `pkg_resources` 有什么区别？
- [ ] 如何查询一个包的版本号？
- [ ] 包名和导入名不一致时如何处理？
- [ ] 什么是入口点（entry points）？
- [ ] 如何列出当前环境的所有已安装包？

