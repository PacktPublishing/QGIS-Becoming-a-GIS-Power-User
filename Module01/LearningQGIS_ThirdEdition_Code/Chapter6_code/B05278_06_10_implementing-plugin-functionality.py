def run(self):
    """Run method that performs all the real work"""
    # show the dialog
    self.dlg.show()
    # clear the combo box to list only current layers
    self.dlg.layerCombo.clear()
    # get the layers and add them to the combo box
    layers = QgsMapLayerRegistry.instance().mapLayers().values()
    for layer in layers:
        if layer.type() == QgsMapLayer.VectorLayer:
            self.dlg.layerCombo.addItem( layer.name(), layer )
    # Run the dialog event loop
    result = self.dlg.exec_()
    # See if OK was pressed
    if result:
        # Check which layer was selected 
        index = self.dlg.layerCombo.currentIndex()
        layer = self.dlg.layerCombo.itemData(index)
        # Display information about the layer 
        QMessageBox.information(self.iface.mainWindow(),"Learning QGIS","%s has %d features." %(layer.name(),layer.featureCount()))

        
from qgis.core import *
from PyQt4.QtGui import QMessageBox

