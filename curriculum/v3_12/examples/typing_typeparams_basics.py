"""PEP 695: native type parameter syntax.

Run with Python >=3.12
"""


class Box[T]:
    def __init__(self, value: T) -> None:
        self.value = value

    def get(self) -> T:
        return self.value


def identity[T](x: T) -> T:
    return x


print(Box(123).get())
print(identity("abc"))


