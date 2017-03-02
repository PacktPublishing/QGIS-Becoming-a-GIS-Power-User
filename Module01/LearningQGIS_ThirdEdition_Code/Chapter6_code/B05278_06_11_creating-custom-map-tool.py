class IdentifyFeatureTool(QgsMapToolIdentify):
    def __init__(self, canvas):
        QgsMapToolIdentify.__init__(self, canvas)
    def canvasReleaseEvent(self, mouseEvent):
        print "canvasReleaseEvent"
        # get features at the current mouse position
        results = self.identify(mouseEvent.x(),mouseEvent.y(), 
                        self.TopDownStopAtFirst, self.VectorLayer)
        if len(results) > 0:
            # signal that a feature was identified 
            self.emit( SIGNAL( "geomIdentified" ), 
                       results[0].mLayer, results[0].mFeature)

def initGui(self):
    # create the toolbar icon and menu entry
    icon_path = ':/plugins/MyFirstMapTool/icon.png'
    self.map_tool_action=self.add_action(
        icon_path,
        text=self.tr(u'My 1st Map Tool'),
        callback=self.map_tool_init,
        parent=self.iface.mainWindow())
    self.map_tool_action.setCheckable(True)

    
def map_tool_init(self):
    # this function is called when the map tool icon is clicked
    print "maptoolinit"
    canvas = self.iface.mapCanvas()
    if self.map_tool_action.isChecked():
        # when the user activates the tool
        self.prev_tool = canvas.mapTool()
        self.map_tool_action.setChecked( True )
        self.map_tool = IdentifyFeatureTool(canvas)
        QObject.connect(self.map_tool, SIGNAL("geomIdentified"),
                        self.do_something )
        canvas.setMapTool(self.map_tool)
        QObject.connect(canvas,SIGNAL("mapToolSet(QgsMapTool *)"),
                        self.map_tool_changed)
    else:
        # when the user deactivates the tool
        QObject.disconnect( canvas, SIGNAL( "mapToolSet(QgsMapTool *)" ),self.map_tool_changed)
        canvas.unsetMapTool(self.map_tool)
        print "restore prev tool %s" %(self.prev_tool)
        canvas.setMapTool(self.prev_tool) 

        
def do_something(self, layer, feature):
    print feature.attributes()

    
def map_tool_changed(self):
    print "maptoolchanged"
    canvas = self.iface.mapCanvas()
    QObject.disconnect(canvas, SIGNAL("mapToolSet(QgsMapTool *)"),
                       self.map_tool_changed)
    canvas.unsetMapTool(self.map_tool)
    self.map_tool_action.setChecked(False)


from qgis.core import *
from qgis.gui import *
from PyQt4.QtCore import *
    
    