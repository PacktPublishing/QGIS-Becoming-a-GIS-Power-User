import processing
from processing.tools.vector import VectorWriter
from PyQt4.QtCore import *
from qgis.core import *
from qgis.networkanalysis import *

layer = processing.getObject('network_pgr')
director = QgsLineVectorLayerDirector(layer,-1,'','','',3)
director.addProperter(QgsDistanceArcProperter())
builder = QgsGraphBuilder(layer.crs())
additional_points = [QgsPoint(3.63715,3.60401),QgsPoint(3.86250,1.58906),QgsPoint(0.42913,2.26512)]
tied_points = director.makeGraph(builder,additional_points)

print tied_points

result = 'C:\\temp\\matched_pts.shp'
writer = VectorWriter(result,None,[],1,layer.crs())
fet = QgsFeature()

for pt in tied_points:
    fet.setGeometry(QgsGeometry.fromPoint(pt))
    writer.addFeature(fet)

del writer
processing.load(result)