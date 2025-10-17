"""
场景 3：数据库字段定义

应用：在 ORM 模型中使用 Annotated 附加数据库约束和元数据
"""

from typing import Annotated, get_type_hints
from dataclasses import dataclass
from datetime import datetime

# 定义数据库约束类
class DBField:
    """数据库字段约束"""
    def __init__(
        self,
        primary_key=False,
        unique=False,
        nullable=False,
        max_length=None,
        default=None,
        index=False
    ):
        self.primary_key = primary_key
        self.unique = unique
        self.nullable = nullable
        self.max_length = max_length
        self.default = default
        self.index = index
    
    def __repr__(self):
        attrs = []
        if self.primary_key:
            attrs.append("PK")
        if self.unique:
            attrs.append("UNIQUE")
        if not self.nullable:
            attrs.append("NOT NULL")
        if self.max_length:
            attrs.append(f"MAX_LEN={self.max_length}")
        if self.index:
            attrs.append("INDEX")
        return f"DBField({', '.join(attrs)})"

# ✅ 定义常用的数据库字段类型

PrimaryKey = Annotated[int, DBField(primary_key=True)]
UniqueString = lambda max_len: Annotated[str, DBField(unique=True, max_length=max_len)]
IndexedString = lambda max_len: Annotated[str, DBField(index=True, max_length=max_len)]
RequiredString = lambda max_len: Annotated[str, DBField(nullable=False, max_length=max_len)]
OptionalString = lambda max_len: Annotated[str | None, DBField(nullable=True, max_length=max_len)]

@dataclass
class User:
    """用户模型"""
    id: PrimaryKey
    username: Annotated[str, DBField(unique=True, nullable=False, max_length=50, index=True)]
    email: Annotated[str, DBField(unique=True, nullable=False, max_length=100)]
    password_hash: Annotated[str, DBField(nullable=False, max_length=255)]
    bio: Annotated[str | None, DBField(nullable=True, max_length=500)]
    created_at: Annotated[datetime, DBField(nullable=False)]
    is_active: Annotated[bool, DBField(nullable=False, default=True)]

@dataclass
class Article:
    """文章模型"""
    id: PrimaryKey
    title: Annotated[str, DBField(nullable=False, max_length=200, index=True)]
    slug: Annotated[str, DBField(unique=True, nullable=False, max_length=200)]
    content: Annotated[str, DBField(nullable=False)]
    author_id: Annotated[int, DBField(nullable=False, index=True)]
    published_at: Annotated[datetime | None, DBField(nullable=True)]
    view_count: Annotated[int, DBField(nullable=False, default=0)]

def generate_create_table_sql(model_class) -> str:
    """根据模型生成 CREATE TABLE SQL"""
    hints = get_type_hints(model_class, include_extras=True)
    table_name = model_class.__name__.lower()
    
    columns = []
    for field_name, field_type in hints.items():
        col_def = f"{field_name}"
        
        # 获取数据库约束
        if hasattr(field_type, '__metadata__'):
            for metadata in field_type.__metadata__:
                if isinstance(metadata, DBField):
                    # 类型推断
                    if field_type.__origin__ if hasattr(field_type, '__origin__') else field_type == int:
                        col_def += " INTEGER"
                    elif field_type.__origin__ if hasattr(field_type, '__origin__') else field_type == str:
                        if metadata.max_length:
                            col_def += f" VARCHAR({metadata.max_length})"
                        else:
                            col_def += " TEXT"
                    elif field_type.__origin__ if hasattr(field_type, '__origin__') else field_type == bool:
                        col_def += " BOOLEAN"
                    elif field_type.__origin__ if hasattr(field_type, '__origin__') else field_type == datetime:
                        col_def += " TIMESTAMP"
                    else:
                        # 处理 Union 类型（如 str | None）
                        col_def += " TEXT"
                    
                    # 约束
                    if metadata.primary_key:
                        col_def += " PRIMARY KEY"
                    if metadata.unique and not metadata.primary_key:
                        col_def += " UNIQUE"
                    if not metadata.nullable:
                        col_def += " NOT NULL"
                    if metadata.default is not None:
                        if isinstance(metadata.default, bool):
                            col_def += f" DEFAULT {'TRUE' if metadata.default else 'FALSE'}"
                        elif isinstance(metadata.default, (int, float)):
                            col_def += f" DEFAULT {metadata.default}"
                        else:
                            col_def += f" DEFAULT '{metadata.default}'"
        
        columns.append(col_def)
    
    sql = f"CREATE TABLE {table_name} (\n  " + ",\n  ".join(columns) + "\n);"
    return sql

def generate_create_index_sql(model_class) -> list[str]:
    """生成索引创建 SQL"""
    hints = get_type_hints(model_class, include_extras=True)
    table_name = model_class.__name__.lower()
    
    indexes = []
    for field_name, field_type in hints.items():
        if hasattr(field_type, '__metadata__'):
            for metadata in field_type.__metadata__:
                if isinstance(metadata, DBField) and metadata.index and not metadata.primary_key:
                    idx_name = f"idx_{table_name}_{field_name}"
                    sql = f"CREATE INDEX {idx_name} ON {table_name}({field_name});"
                    indexes.append(sql)
    
    return indexes

print("=" * 60)
print("场景 3：数据库字段定义")
print("=" * 60)

# 示例 1：User 表 SQL 生成
print("\n[示例 1] User 表 SQL 生成：\n")

user_sql = generate_create_table_sql(User)
print(user_sql)

# 示例 2：User 表索引生成
print("\n[示例 2] User 表索引生成：\n")

user_indexes = generate_create_index_sql(User)
for idx_sql in user_indexes:
    print(idx_sql)

# 示例 3：Article 表 SQL 生成
print("\n[示例 3] Article 表 SQL 生成：\n")

article_sql = generate_create_table_sql(Article)
print(article_sql)

# 示例 4：Article 表索引生成
print("\n[示例 4] Article 表索引生成：\n")

article_indexes = generate_create_index_sql(Article)
for idx_sql in article_indexes:
    print(idx_sql)

# 示例 5：字段约束分析
print("\n[示例 5] User 模型字段约束分析：\n")

hints = get_type_hints(User, include_extras=True)
for field_name, field_type in hints.items():
    print(f"{field_name}:")
    if hasattr(field_type, '__metadata__'):
        for metadata in field_type.__metadata__':
            if isinstance(metadata, DBField):
                print(f"  约束: {metadata}")

print("\n[数据库字段定义的优势]")
print("  ✅ 字段约束与模型定义在一起")
print("  ✅ 自动生成数据库迁移SQL")
print("  ✅ 类型和约束一致性保证")
print("  ✅ IDE 提示字段约束信息")

print("\n💡 总结：Annotated 让 ORM 模型包含数据库约束，便于自动化")

