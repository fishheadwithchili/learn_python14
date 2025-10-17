"""
场景 9：异常处理上下文

应用：捕获异常时记录完整上下文
"""

print("=" * 60)
print("异常上下文记录")
print("=" * 60)

def divide_data(data, divisor):
    """处理数据"""
    try:
        result = [x / divisor for x in data]
        return result
    except ZeroDivisionError as e:
        print(f"\n❌ 除零错误!")
        print(f"{type(e)=}")
        print(f"{str(e)=}")
        print(f"{data=}")
        print(f"{divisor=}")
        raise
    except TypeError as e:
        print(f"\n❌ 类型错误!")
        print(f"{type(e)=}")
        print(f"{data=}")
        print(f"{divisor=}")
        print(f"{type(data)=}")
        print(f"{type(divisor)=}")
        raise

print("\n正常情况：\n")
result = divide_data([10, 20, 30], 2)
print(f"{result=}")

print("\n异常情况 1：\n")
try:
    divide_data([10, 20], 0)
except ZeroDivisionError:
    pass

print("\n💡 总结：异常排查效率提升，上下文完整")

