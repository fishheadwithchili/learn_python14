"""
场景 6：序列化/反序列化提示

应用：为字段附加序列化规则和格式化信息
"""

from typing import Annotated
from dataclasses import dataclass
from datetime import datetime
import json

class SerializeAs:
    """序列化格式"""
    def __init__(self, format_type):
        self.format_type = format_type

# ✅ 定义序列化类型
ISODateTime = Annotated[datetime, SerializeAs("iso8601")]
CurrencyUSD = Annotated[float, SerializeAs("currency_usd")]
Percentage = Annotated[float, SerializeAs("percentage")]

@dataclass
class Product:
    """产品"""
    id: int
    name: str
    price: CurrencyUSD
    discount: Percentage
    created_at: ISODateTime

def serialize_product(product: Product) -> dict:
    """序列化产品"""
    return {
        "id": product.id,
        "name": product.name,
        "price": f"${product.price:.2f}",
        "discount": f"{product.discount:.1f}%",
        "created_at": product.created_at.isoformat()
    }

print("=" * 60)
print("场景 6：序列化/反序列化")
print("=" * 60)

# 示例
product = Product(
    id=1,
    name="Python 编程",
    price=99.99,
    discount=15.0,
    created_at=datetime.now()
)

print(f"\n原始对象: {product}\n")

serialized = serialize_product(product)
print("序列化结果:")
print(json.dumps(serialized, indent=2, ensure_ascii=False))

print("\n💡 总结：Annotated 定义序列化格式，确保数据输出一致")

