import sys
from PyQt5 import QtWidgets as qtw
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class ViewerWidget(qtw.QWidget):

    def __init__(self, parent):
        super(qtw.QWidget, self).__init__(parent)
        self.horizontalGroupBox = qtw.QGroupBox("Result viewer")
        self.buildEditor()

        windowLayout = qtw.QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)


    def buildEditor(self):
        layout = qtw.QVBoxLayout()
        label1 = qtw.QLabel()
        label1.setText("Input")
        layout.addWidget(label1)
        self.input = qtw.QTextEdit()
        layout.addWidget(self.input)
        label2 = qtw.QLabel()
        label2.setText("Output")
        layout.addWidget(label2)
        self.output = qtw.QTextEdit()
        layout.addWidget(self.output)

        self.horizontalGroupBox.setLayout(layout)
