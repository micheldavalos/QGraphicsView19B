from PySide2.QtWidgets import QMainWindow, QGraphicsScene
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen, QColor, QBrush
from random import randint

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.\
            clicked.connect(self.dibujar)
        self.ui.pushButton_2.\
            clicked.connect(self.limpiar)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)

        for i in range(0, 100):
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)

            pen.setColor(QColor(r, g, b))

            origen_x = randint(0, 300)
            origen_y = randint(0, 300)
            destino_x = randint(0, 300)
            destino_y = randint(0, 300)

            self.scene.\
                addEllipse(origen_x, origen_y, 6, 6, pen, QBrush(QColor(r, g, b)))
            self.scene.\
                addEllipse(destino_x, destino_y, 6, 6, pen, QBrush(QColor(r, g, b)))
            self.scene.\
                addLine(origen_x+3, origen_y+3,
                        destino_x+3, destino_y+3, pen)

    @Slot()
    def limpiar(self):
        self.scene.clear()