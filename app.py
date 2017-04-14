import sys
import os

try:
    from qgis import core as qgisCore
    from qgis import gui as qgisGui
except:
    pass

from PyQt4 import QtCore, QtGui


#############################################################################

class MapViewer(QtGui.QMainWindow):
    def __init__(self, shapefile):
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle("Map Viewer")

        canvas = qgisGui.QgsMapCanvas()
        canvas.useImageToRender(False)
        canvas.setCanvasColor(QtCore.Qt.white)
        canvas.show()

        layer = qgisCore.QgsVectorLayer(shapefile, "layer1", "ogr")
        if not layer.isValid():
            raise IOError("Invalid shapefile")

        qgisCore.QgsMapLayerRegistry.instance().addMapLayer(layer)
        canvas.setExtent(layer.extent())
        canvas.setLayerSet([qgisGui.QgsMapCanvasLayer(layer)])

        layout = QtGui.QVBoxLayout()
        layout.addWidget(canvas)

        contents = QtGui.QWidget()
        contents.setLayout(layout)
        self.setCentralWidget(contents)

#############################################################################

def main():
    """  Our main program.
    """
    app = QtGui.QApplication(sys.argv)

    if getattr(sys, 'frozen', False):
        print "Running In An Application Bundle"
        bundle_dir = sys._MEIPASS
        qgis_prefix_path = bundle_dir
        qgis_plugin_path = bundle_dir + '\qgis_plugins'
    else:
        print "Running In A Normal Python Environment"
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
        qgis_prefix_path = os.getenv("QGIS_PREFIX")
        qgis_plugin_path = qgis_prefix_path + '\plugins'
    qgisCore.QgsApplication.setPrefixPath(qgis_prefix_path, True)
    qgisCore.QgsApplication.setPluginPath(qgis_plugin_path)
    qgisCore.QgsApplication.initQgis()
    registry = qgisCore.QgsProviderRegistry.instance()
    if not 'ogr' in registry.providerList():
        print 'ERROR: Missing OGR provider'

    #QgsApplication.setPrefixPath(os.environ['QGIS_PREFIX'], True)
    #QgsApplication.initQgis()

    viewer = MapViewer("data/gilroy_simple.shp")
    viewer.show()

    app.exec_()

    qgisCore.QgsApplication.exitQgis()

#############################################################################

if __name__ == "__main__":
    main()