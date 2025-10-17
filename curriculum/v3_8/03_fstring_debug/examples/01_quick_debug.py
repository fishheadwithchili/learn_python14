"""
场景 1：快速调试变量值

应用：开发过程中快速查看变量值，节省重复输入变量名
"""

print("=" * 60)
print("快速调试变量值")
print("=" * 60)

# 模拟一些计算
user_id = 12345
username = "alice"
is_active = True
score = 87.5

print("\n❌ 传统方式 - 需要重复写变量名：\n")
print(f"user_id: {user_id}")
print(f"username: {username}")
print(f"is_active: {is_active}")
print(f"score: {score}")

print("\n✅ f-string 调试语法 - 自动显示变量名：\n")
print(f"{user_id=}")
print(f"{username=}")
print(f"{is_active=}")
print(f"{score=}")

print("\n" + "=" * 60)
print("多个变量一行显示")
print("=" * 60)

x, y, z = 10, 20, 30

print("\n一行显示多个变量：\n")
print(f"{x=}, {y=}, {z=}")

print("\n计算表达式：\n")
print(f"{x + y=}")
print(f"{x * z=}")
print(f"{(x + y) / z=:.2f}")

print("\n💡 总结：调试输出代码量减少 50%，提升开发效率")

