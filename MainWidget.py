from PyQt5 import QtWidgets as qtw
from PyQt5.QtCore import pyqtSlot

from EditorWidget import EditorWidget
from ViewerWidget import ViewerWidget


class MainWidget(qtw.QWidget):

    def __init__(self, parent):
        super(qtw.QWidget, self).__init__(parent)
        self.setLayout(qtw.QHBoxLayout())
        self.editor = EditorWidget(self)
        self.layout().addWidget(self.editor)
        self.viewer = ViewerWidget(self)
        self.layout().addWidget(self.viewer)


    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

