v_layer = iface.addVectorLayer(' C:/Users/anita/Documents/Geodata/qgis_sample_data/shapefiles/airports.shp','airports','ogr')

v_layer.name()
u'airports'

v_layer.featureCount()
76L

my_features = v_layer.getFeatures()
for feature in my_features:
    print feature.attributes()
[1, u'US00157', 78.0, u'Airport/Airfield', u'PA', u'NOATAK' ...
[2, u'US00229', 264.0, u'Airport/Airfield', u'PA', u'AMBLER'...
[3, u'US00186', 585.0, u'Airport/Airfield', u'PABT', u'BETTL...
...

for field in v_layer.fields():
    print field.name()
cat
NA3
ELEV
F_CODE
IKO
NAME
USE

for feature in v_layer.getFeatures():
    print feature.attribute('NAME')
NOATAK
AMBLER
BETTLES
...

sum([feature.attribute('ELEV') for feature in v_layer.getFeatures()])
22758.0

r_layer = iface.addRasterLayer('C:/Users/anita/Documents/Geodata/qgis_sample_data/raster/SR_50M_alaska_nad.tif','hillshade')
r_layer.name()
u'hillshade'

r_layer.width(), r_layer.height()
(1754, 1394)

r_layer.dataProvider().bandStatistics(1).maximumValue
251.0

help(r_layer.dataProvider().bandStatistics(1))



