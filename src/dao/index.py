from sqlalchemy import text
from config.log import console
from config.db import engine
from sqlmodel import SQLModel

class TableDao:
    '''数据库基础操作类'''
    # def create():
    #     '''创建所有未创建的表格'''
    #     # BaseDaoManager.metadata.create_all(engine)
    #     SQLModel.metadata.create_all(engine)
        
    async def create():
        async with engine.begin() as conn:
            # await conn.run_sync(SQLModel.metadata.drop_all)
            await conn.run_sync(SQLModel.metadata.create_all)
            

        
class BaseDao:
    async def test(sql_str):
        async with engine.begin() as conn:
            # await conn.run_sync(SQLModel.metadata.drop_all)
            # return await conn.execute(sql_str)
            result_proxy =await conn.execute(text(sql_str))  # 返回值为ResultProxy类型
            result = result_proxy.fetchall() # 获取查询结果
            for item in result:
                print(item._mapping)
                print(item._mapping.id)

console.log('...基础sql配置完成')