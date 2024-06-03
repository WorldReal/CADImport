import ezdxf
import geojson
def dxf_to_geojson(doc):
    # 读取 DXF 文件
    # doc = ezdxf.readfile(dxf_path)
    msp = doc.modelspace()

    features = []

    # 处理 LINE 实体
    for line in msp.query("LINE"):
        start = line.dxf.start
        end = line.dxf.end
        line_coords = [(start.x, start.y), (end.x, end.y)]
        feature = geojson.Feature(
            geometry=geojson.LineString(line_coords),
            properties={}
        )
        features.append(feature)

    # 处理 LWPOLYLINE 实体
    for lwpolyline in msp.query("LWPOLYLINE"):
        points = lwpolyline.get_points("xy")
        line_coords = [(x, y) for x, y in points]
        feature = geojson.Feature(
            geometry=geojson.LineString(line_coords),
            properties={}
        )
        features.append(feature)

    # 处理 POLYLINE 实体
    for polyline in msp.query("POLYLINE"):
        points = [vertex.dxf.location for vertex in polyline.vertices]
        line_coords = [(point.x, point.y) for point in points]
        feature = geojson.Feature(
            geometry=geojson.LineString(line_coords),
            properties={}
        )
        features.append(feature)

    # 创建 FeatureCollection
    feature_collection = geojson.FeatureCollection(features)

    # # 保存为 GeoJSON 文件
    # with open(geojson_path, "w") as f:
    #     geojson.dump(feature_collection, f)

    # print(f"GeoJSON file saved as {geojson_path}")
    
    return feature_collection