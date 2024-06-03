
# self
from uuid import UUID,uuid4
from config.db import Data
from do.user import User

class UserDao:

    @Data
    def insert(user:User,session=None):
        """插入一个新的用户"""
        return session.add(user)
        # 不需要显式调用 session.commit()，因为装饰器已经处理了
        
    @Data
    def select_by_id(id:UUID,session=None):
        # 快捷方式 id
        user = session.get(User, id)
        print(user)
        return user


    
    




