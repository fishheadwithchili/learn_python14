"""
场景 6：命令行输入验证

应用：交互式程序中验证输入并存储，输入逻辑集中在循环条件
"""

import time

# 模拟用户输入（实际使用时会用 input()）
SIMULATED_INPUTS = ["5", "abc", "-1", "0", "3"]
input_index = 0

def mock_input(prompt):
    """模拟 input() 函数用于演示"""
    global input_index
    if input_index < len(SIMULATED_INPUTS):
        value = SIMULATED_INPUTS[input_index]
        input_index += 1
        print(f"{prompt}{value}")
        time.sleep(0.3)  # 模拟用户思考时间
        return value
    return "quit"

print("=" * 60)
print("命令行输入验证")
print("=" * 60)

print("\n📝 场景：让用户选择操作（1-3），输入无效时重新提示\n")

# ✅ 使用 walrus operator - 输入和验证合并
print("[Walrus Operator] 简洁的输入验证：\n")

valid_choices = ["1", "2", "3"]

while (choice := mock_input("请选择操作 (1-3): ")) not in valid_choices:
    print(f"  ❌ 无效选择: '{choice}'，请重新输入\n")

print(f"  ✅ 已选择操作: {choice}\n")

# 处理选择
operations = {
    "1": "查看数据",
    "2": "添加数据",
    "3": "删除数据"
}
print(f"正在执行: {operations[choice]}")

print("\n" + "=" * 60)
print("高级示例：密码验证（带次数限制）")
print("=" * 60)

# 模拟密码输入
PASSWORD_ATTEMPTS = ["wrong1", "wrong2", "correct"]
attempt_index = 0

def mock_password():
    global attempt_index
    if attempt_index < len(PASSWORD_ATTEMPTS):
        pw = PASSWORD_ATTEMPTS[attempt_index]
        attempt_index += 1
        print(f"请输入密码: {'*' * len(pw)}")
        time.sleep(0.2)
        return pw
    return ""

CORRECT_PASSWORD = "correct"
MAX_ATTEMPTS = 3
attempts = 0

print()
while (password := mock_password()) != CORRECT_PASSWORD and attempts < MAX_ATTEMPTS:
    attempts += 1
    print(f"  ❌ 密码错误！剩余尝试次数: {MAX_ATTEMPTS - attempts}\n")

if password == CORRECT_PASSWORD:
    print("  ✅ 密码正确，登录成功！")
else:
    print("  🔒 尝试次数过多，账户已锁定")

print("\n💡 总结：输入验证逻辑集中在循环条件，代码更紧凑")

