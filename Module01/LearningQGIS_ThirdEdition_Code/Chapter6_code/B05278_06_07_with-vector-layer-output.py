##Learning QGIS=group
##input_layer=vector
##size=number 1000000
##squares=output vector
from qgis.core import *
from processing.tools.vector import VectorWriter
# get the input layer and its fields
my_layer = processing.getObject(input_layer)
fields = my_layer.dataProvider().fields()
# create the output vector writer with the same fields
writer = VectorWriter(squares, None, fields, QGis.WKBPolygon, my_layer.crs())
# create output features
feat = QgsFeature()
for input_feature in my_layer.getFeatures():
    # copy attributes from the input point feature
    attributes = input_feature.attributes()
    feat.setAttributes(attributes)
    # create square polygons
    point = input_feature.geometry().asPoint()
    xmin = point.x() - size/2
    ymin = point.y() - size/2
    square = QgsRectangle(xmin,ymin,xmin+size,ymin+size)
    feat.setGeometry(QgsGeometry.fromRect(square))
    writer.addFeature(feat)
del writer