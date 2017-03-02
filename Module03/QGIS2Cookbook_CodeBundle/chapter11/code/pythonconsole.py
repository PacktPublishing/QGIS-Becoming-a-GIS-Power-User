# Chapter 11, Recipe 6 Python Console
layer = iface.activeLayer()
layer.featureCount()
dir(layer)
dir(QgsFeature)

for f in layer.getFeatures():
    print f[“featurenam”], f[‘elev_m”]
    
# Part 2    
import csv

layer = iface.activeLayer()
with open(‘c:\\temp\\export.csv’, ‘wb’) as outputFile:
    writer = csv.writer(outputFile)
    for feature in layer.getFeatures():
        geom = feature.geometry().exportToWkt()
        writer.writerow([geom, feature[“featurenam”], feature[‘elev_m”]])
