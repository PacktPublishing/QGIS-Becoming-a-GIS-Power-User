iface.mapCanvas().saveAsImage('C:/temp/simple_export.png')

from PyQt4.QtGui import QImage, QPainter
from PyQt4.QtCore import QSize
# configure the output image
width = 800
height = 600
dpi = 92
img = QImage(QSize(width, height), QImage.Format_RGB32)
img.setDotsPerMeterX(dpi / 25.4 * 1000)
img.setDotsPerMeterY(dpi / 25.4 * 1000)
# get the map layers and extent
layers = [ layer.id() for layer in iface.legendInterface().layers() ]
extent = iface.mapCanvas().extent()
# configure map settings for export
mapSettings = QgsMapSettings()
mapSettings.setMapUnits(0)
mapSettings.setExtent(extent)
mapSettings.setOutputDpi(dpi)
mapSettings.setOutputSize(QSize(width, height))
mapSettings.setLayers(layers)
mapSettings.setFlags(QgsMapSettings.Antialiasing | QgsMapSettings.UseAdvancedEffects | QgsMapSettings.ForceVectorOutput | QgsMapSettings.DrawLabeling)
# configure and run painter
p = QPainter()
p.begin(img)
mapRenderer = QgsMapRendererCustomPainterJob(mapSettings, p)
mapRenderer.start()
mapRenderer.waitForFinished()
p.end()
# save the result
img.save("C:/temp/custom_export.png","png")
