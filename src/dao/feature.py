
from config.db import Data
from do.feature import Feature
from uuid import UUID

class FeatureDao:
    @Data
    def insert(feature:Feature,session=None):
            return session.add(feature)
        # 不需要显式调用 session.commit()，因为装饰器已经处理了
    @Data
    def insert_batch(features:[Feature],session=None):
            for feature in features:
                session.add(feature)
        
    @Data
    def select_by_id(id:UUID,session=None):
        # 快捷方式 id
        feature = session.get(Feature, id)
        print(feature)
        return feature
        
        
        
        
            # geojson = session.exec(
            #     select(ga.functions.ST_AsGeoJSON(db_feature.geometry))
            # ).one()


# def read_feature(feature_id: uuid.UUID):
#     with Session(engine) as session:
#         db_feature = session.get(Feature, feature_id)
#         if db_feature is None:
#             raise HTTPException(status_code=404, detail="Feature not found")
#         geojson = session.exec(
#             select(ga.functions.ST_AsGeoJSON(db_feature.geometry))
#         ).one()
#     response = FeatureRead(
#         id=db_feature.id,
#         geometry=GeoJSONGeometry.model_validate_json(geojson),
#         properties=db_feature.properties,
#     )
#     return response