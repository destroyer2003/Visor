from PyQt5.QtCore import QFileInfo
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import *
import sys
from qgis.core import *
from qgis.gui import *


class Ventana(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ventana, self).__init__()
        uic.loadUi('visor.ui', self)
        # carga el diseño

        # establecer el frame como lienzo mapa
        self.mapa = QgsMapCanvas()
        self.mapa.setCanvasColor(QColor(255, 255, 255))
        self.mapa.enableAntiAliasing(True)
        self.mapa.show()
        self.layout = QtWidgets.QVBoxLayout(self.frame)
        self.layout.addWidget(self.mapa)

        # crear botones de accion
        self.botonAgragarCapa = QtWidgets.QAction(QIcon('iconos/Carpeta.png'), "Agregar Capa", self.frame)
        self.botonAgragarCapa.triggered.connect(self.AgregarCapa)

        self.botonMover = QtWidgets.QAction(QIcon('iconos/Mover.png'), "Mover", self.frame)
        self.botonMover.triggered.connect(self.MoverMapa)
        self.botonAcercar = QtWidgets.QAction(QIcon('iconos/zoomin.png'), "Acercar", self.frame)
        self.botonAlejar = QtWidgets.QAction(QIcon('iconos/zoomout.png'), "Alejar", self.frame)

        # crear barras de herramientas
        self.barra = self.addToolBar("Mapa")
        self.barra.addAction(self.botonAgragarCapa)
        self.barra.addAction(self.botonMover)
        self.barra.addAction(self.botonAlejar)
        self.barra.addAction(self.botonAcercar)

        #crear herramientas para el mapa
        self.herramientaMover=QgsMapToolPan(self.mapa)

        self.show()  # mostrar la ventana
    def MoverMapa(self):
        self.mapa.setMapTool(self.herramientaMover)
    # crear funcion agregar capa
    def AgregarCapa(self):
        #mandar mensaje de prueba
        ruta_capa = QtWidgets.QFileDialog.getOpenFileName(self, "Abrir archivo", ".", "*.shp")
        print(ruta_capa)
        capa_informacion = QFileInfo(ruta_capa[0])
        capa_proovedor = "ogr"
        capa = QgsVectorLayer(ruta_capa[0], capa_informacion.fileName(), capa_proovedor)
        QgsProject.instance().addMapLayer(capa)
        self.mapa.setExtent(capa.extent())
        self.mapa.setLayers([capa])
        self.mapa.show()
        self.mapa.refresh()

       # print("funciona la accion de agregar capa")

# se crea un objeto
aplicacion = QtWidgets.QApplication(sys.argv)
ruta_qgis = r'C:\Program Files\QGIS 3.32.2\apps\qgis'
QgsApplication.setPrefixPath(ruta_qgis)
QgsApplication.initQgis()
ventana = Ventana()
aplicacion.exec_()
QgsApplication.exitQgis()