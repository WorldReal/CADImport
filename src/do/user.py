from sqlmodel import Field, SQLModel
from uuid import uuid4,UUID
from datetime import datetime

# 定义模型类，继承自基本类
class User(SQLModel, table=True):
    # 定义表结构
    # uuid 标准格式
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True, index=True, unique=True)
    name:str
    email:str
    created_at: datetime = Field(default=datetime.utcnow)
    
    # 可选：定义初始化方法
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    # 可选：定义对象的字符串表示形式
    def __repr__(self):
        return f"<User(name='{self.name}', age={self.email})>"