# self
from config.log import console
from dao.index import TableDao

class TableService:
    # 更新数据库 静态方法
    @staticmethod
    async def create():
        # 调用函数
        await TableDao.create()