"""
场景 7：表单验证

应用：Web 表单字段定义，包含验证和UI提示
"""

from typing import Annotated
from dataclasses import dataclass

class FormField:
    """表单字段元数据"""
    def __init__(self, label, placeholder="", help_text=""):
        self.label = label
        self.placeholder = placeholder
        self.help_text = help_text

# ✅ 定义表单字段
@dataclass
class RegisterForm:
    """注册表单"""
    username: Annotated[str, FormField("用户名", "请输入用户名", "3-20个字符")]
    email: Annotated[str, FormField("邮箱", "your@example.com")]
    password: Annotated[str, FormField("密码", "", "至少8位，包含字母和数字")]
    confirm_password: Annotated[str, FormField("确认密码")]

def render_form(form_class):
    """渲染表单 HTML（简化版）"""
    from typing import get_type_hints
    hints = get_type_hints(form_class, include_extras=True)
    
    print("<form>")
    for field_name, field_type in hints.items():
        if hasattr(field_type, '__metadata__'):
            for metadata in field_type.__metadata__:
                if isinstance(metadata, FormField):
                    print(f'  <div class="field">')
                    print(f'    <label>{metadata.label}:</label>')
                    input_type = "password" if "password" in field_name else "text"
                    print(f'    <input type="{input_type}" name="{field_name}" placeholder="{metadata.placeholder}" />')
                    if metadata.help_text:
                        print(f'    <span class="help">{metadata.help_text}</span>')
                    print(f'  </div>')
    print("</form>")

print("=" * 60)
print("场景 7：表单验证")
print("=" * 60)

print("\n[生成的表单 HTML]:\n")
render_form(RegisterForm)

print("\n💡 总结：Annotated 让表单定义包含 UI 信息，自动生成界面")

