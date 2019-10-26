from PySide2.QtWidgets import QApplication
import sys
from mainwindow import MainWindow

app = QApplication()
window = MainWindow()
window.show()
sys.exit(app.exec_())
