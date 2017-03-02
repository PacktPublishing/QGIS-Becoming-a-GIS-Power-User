##Cookbook=group
##Filter polygons by size=name
##Vector_layer=vector
##Area=number 1
##Output=output vector

layer = processing.getObject(Vector_layer)
provider = layer.dataProvider()
writer = processing.VectorWriter(Output, None, provider.fields(),    provider.geometryType(), layer.crs())

for feature in processing.features(layer):
    print feature.geometry().area()
    if feature.geometry().area() > Area:
        writer.addFeature(feature)
    
del writer
