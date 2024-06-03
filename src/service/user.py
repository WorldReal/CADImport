# self
from uuid import UUID
from config.log import console
from dao.user import UserDao
# lib
from fastapi import HTTPException
from do.user import User


class UsersService:
    '''文件服务'''
    @staticmethod
    async def add(user: User):
        try:
            console.log("test1 start!") 
            # 调用函数
            # if not user.time:user.time = datetime.now()
            return await UserDao.insert(user)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e)
    @staticmethod
    async def select_by_id(id:UUID):
        return UserDao.select_by_id(id)
        
    @staticmethod
    async def update_by_email(name: str,email:str):
        await UserDao.update_by_email(name,email)

