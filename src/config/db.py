# self
from config.log import console
# lib
from functools import wraps
# from sqlalchemy import create_engine
# import aiosqlite # 依赖写全防止找不到
import asyncpg # 依赖写全防止找不到
from sqlmodel import create_engine, Session
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.pool import QueuePool

engine = create_async_engine( 
                       "postgresql+asyncpg://postgres:123456@localhost:5432/main",
                       echo=True, # 控制台打印SQL
                       )
        
def Data(f):
    '''装饰器_负责创建执行和关闭'''
    @wraps(f)
    async def wrapper(*args, **kwargs):   
        try:
            # 创建一个配置过的Session类
            async with AsyncSession(engine) as session:# 确保 session 总是被关闭
                kwargs['session'] = session  # 将 session 作为关键字参数传递给 f
                f(*args, **kwargs)
                await session.commit()  # 提交事务
        except Exception as e:
            # console.exception("数据库问题:"+str(e.orig))
            console.error("数据库问题:"+str(e.orig))
            raise e
    return wrapper



console.log('...数据库配置完成')