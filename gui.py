import sys
from PyQt5 import QtWidgets as qtw
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from DataObj import DataObj
from App import App

# Credit: "AA.mp4" downloaded from https://www.youtube.com/watch?v=dzvnSapnzBA
#     -> Footage of Einstein final 1-3 in 2014 Aerial Assist
# Credit: "DD.mp4" footage captured by Fred Westling at the 2019 Destination: Deep Space Southern Cross Regional

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    app.setStyle('Fusion')
    data = DataObj()
    ex = App(app, data)
    sys.exit(app.exec_())
