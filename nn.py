from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import *
import sys
from qgis.core import *
from qgis.gui import *


class Ventana(QtWidgets.QMainWindow):
    def _init_(self):
        super(Ventana, self)._init_()
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
        self.botonAcercar = QtWidgets.QAction(QIcon('iconos/zoomin.png'), "Acercar", self.frame)
        self.botonAlejar = QtWidgets.QAction(QIcon('iconos/zoomout.png'), "Alejar", self.frame)

        # crear barras de herramientas
        self.barra = self.addToolBar("Mapa")
        self.barra.addAction(self.botonAgragarCapa)
        self.barra.addAction(self.botonMover)
        self.barra.addAction(self.botonAlejar)
        self.barra.addAction(self.botonAcercar)



        self.show()  # mostrar la ventana

    # crear funcion agregar capa
    def AgregarCapa(self):
        #mandar mensaje de prueba
        ruta_capa = QtWidgets.QFileDialog.getOpenFileName(self, "Abrir archivo", ".", "Shapefile (*.shp)")
        print(ruta_capa)

        print("funciona la accion de agregar capa")

# se crea un objeto
aplicacion = QtWidgets.QApplication(sys.argv)
ventana = Ventana()
aplicacion.exec_()