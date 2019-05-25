import sys
from PyQt5 import QtWidgets as qtw
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from App import App

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = App(app)
    sys.exit(app.exec_())
