import processing
from processing.tools.vector import VectorWriter
from PyQt4.QtCore import *
from qgis.core import *
from qgis.networkanalysis import *
# create the graph
layer = processing.getObject('network_pgr')
director = QgsLineVectorLayerDirector(layer,-1,'','','',3)
director.addProperter(QgsDistanceArcProperter())
builder = QgsGraphBuilder(layer.crs())
from_point = QgsPoint(2.73343,3.00581)
to_point = QgsPoint(0.483584,2.01487)
tied_points = director.makeGraph(builder,[from_point,to_point])
graph = builder.graph()
# compute the route from from_id to to_id
from_id = graph.findVertex(tied_points[0])
to_id = graph.findVertex(tied_points[1])
(tree,cost) = QgsGraphAnalyzer.dijkstra(graph,from_id,0)
# assemble the route
route_points = []
curPos = to_id 
while (curPos != from_id):
    in_vertex = graph.arc(tree[curPos]).inVertex()
    route_points.append(graph.vertex(in_vertex).point())
    curPos = graph.arc(tree[curPos]).outVertex()
route_points.append(from_point) 
# write the results to a Shapefile 
result = 'C:\\temp\\route.shp'
writer = VectorWriter(result,None,[],2,layer.crs())
fet = QgsFeature()
fet.setGeometry(QgsGeometry.fromPolyline(route_points))
writer.addFeature(fet)
del writer
processing.load(result)
