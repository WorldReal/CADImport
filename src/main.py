import json
import uuid
from config.log import console

# 标准库
import asyncio
import os

# cad库
import ezdxf
from ezdxf.math import bbox
from ezdxf.addons import odafc

# geojson 空间格式库
import geojson
from config import db,path,log
# from config.log import console

# 文件路径规范
from config.path import path_base
from do.feature import Feature
from dao.feature import FeatureDao
from dao.index import TableDao,BaseDao
from dao.user import UserDao
from do.user import User
from service.index import TableService

# 工具类
from utils.dxf2geojson import dxf_to_geojson

from shapely.geometry import shape,LineString
from geoalchemy2 import functions

async def main():
    # 目录根路径
    print('path_base',path_base)

    # cad 文件夹路径
    path_cad = os.path.join(path_base, 'source', 'cad')

    '''读取cad的dwg文件获取包围盒'''
    # # 通过修改win_exec_path的值为自定义安装路径  !!过时   直接在 ezdxf\addons文件内 path更改
    # odafc.win_exec_path = r'D:\a_code_lib\cadlib\ODAFileConverter\ODAFileConverter.exe'
    # 1 读取dwg文件
    doc = odafc.readfile(os.path.join(path_cad, 'test_feicui','Drawing1.dwg')) # dwg文件名或者路径)
    # 2 转换保存 DXF 文件留档
    # doc.saveas(os.path.join(path_cad, 'test_feicui','Drawing1.dxf'))

    # 3 DXF内图形转换geojson
    feature_collection = dxf_to_geojson(doc)
    # print(feature_collection)

    # 4 存入空间数据库
    # 初始化数据库表
    await TableService.create()
    # # new User
    # user = User(name='test', email='test11111@qq.com')
    # await UserDao.insert(user)
    uuid_pwg =uuid.uuid4()
    
    #test单条数据插入
    await FeatureDao.insert(Feature(
            pid = uuid_pwg,
            geometry=functions.ST_GeomFromGeoJSON(str(feature_collection.features[0].geometry)),
            properties=feature_collection.features[0].properties),
          )
    #test单条数据插入
    # await FeatureDao.insert(Feature(
    #         geometry=functions.ST_GeomFromGeoJSON(str(feature_collection.features[0].geometry)),
    #         properties=feature_collection.features[0].properties),
    #         pid = uuid_pwg)
    # # 多条
    # db_features = []
    # for geojson_data in feature_collection.features:
    #     db_features.append(
    #         Feature(
    #             geometry=functions.ST_GeomFromGeoJSON(str(geojson_data.geometry)),
    #             properties=geojson_data.properties)   
    #     )
    # await FeatureDao.insert_batch(db_features)
    
    # 查询
    await BaseDao.test("select * from public.user")
  
asyncio.run(main())





