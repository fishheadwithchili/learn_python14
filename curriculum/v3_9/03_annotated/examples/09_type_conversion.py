"""
场景 9：数据类型转换提示

应用：为类型附加转换规则，实现自动类型转换
"""

from typing import Annotated, get_type_hints
from dataclasses import dataclass
from datetime import datetime

class ConvertFrom:
    """类型转换规则"""
    def __init__(self, from_type, converter):
        self.from_type = from_type
        self.converter = converter

# ✅ 定义带转换的类型
UserId = Annotated[int, ConvertFrom(str, int)]
Price = Annotated[float, ConvertFrom(str, lambda x: float(x.replace(',', '').replace('$', '')))]
Timestamp = Annotated[datetime, ConvertFrom(str, datetime.fromisoformat)]
YesNo = Annotated[bool, ConvertFrom(str, lambda x: x.lower() in ['yes', 'true', '1'])]

@dataclass
class Order:
    """订单"""
    id: UserId
    total: Price
    created_at: Timestamp
    is_paid: YesNo

def auto_convert(data: dict, model_class):
    """自动类型转换"""
    hints = get_type_hints(model_class, include_extras=True)
    converted = {}
    
    for field_name, field_type in hints.items():
        value = data.get(field_name)
        
        if hasattr(field_type, '__metadata__'):
            for metadata in field_type.__metadata__:
                if isinstance(metadata, ConvertFrom) and value is not None:
                    value = metadata.converter(value)
                    break
        
        converted[field_name] = value
    
    return model_class(**converted)

print("=" * 60)
print("场景 9：类型转换")
print("=" * 60)

# 原始数据（全是字符串）
raw_data = {
    "id": "12345",
    "total": "$1,234.56",
    "created_at": "2023-06-15T10:30:00",
    "is_paid": "yes"
}

print("\n[原始数据]:")
for key, value in raw_data.items():
    print(f"  {key}: {value} (类型: {type(value).__name__})")

# 自动转换
order = auto_convert(raw_data, Order)

print("\n[转换后]:")
print(f"  id: {order.id} (类型: {type(order.id).__name__})")
print(f"  total: {order.total} (类型: {type(order.total).__name__})")
print(f"  created_at: {order.created_at} (类型: {type(order.created_at).__name__})")
print(f"  is_paid: {order.is_paid} (类型: {type(order.is_paid).__name__})")

print("\n💡 总结：Annotated 定义转换规则，实现自动类型转换")

