from CGgui import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    app = QApplication(sys.argv)

    mainwindow = QMainWindow()

    ui_components = Ui_MainWindow()
    ui_components.setupUi(mainwindow)

    mainwindow.show()

    sys.exit(app.exec_())
