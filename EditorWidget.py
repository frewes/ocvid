import sys
from PyQt5 import QtWidgets as qtw
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class EditorWidget(qtw.QWidget):

    def __init__(self, parent):
        super(qtw.QWidget, self).__init__(parent)
        self.horizontalGroupBox = qtw.QGroupBox("Editor")
        self.data = parent.data

        self.buildEditor()
        windowLayout = qtw.QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)


    def buildEditor(self):
        layout = qtw.QVBoxLayout(self)

        self.header = qtw.QLabel(self);
        self.header.setText(self.data.preamble)
        layout.addWidget(self.header)
        self.editor = qtw.QTextEdit(self)
        self.editor.setText(self.data.code)
        layout.addWidget(self.editor)
        self.saveButton = qtw.QPushButton('Update!', self)
        layout.addWidget(self.saveButton)
        self.horizontalGroupBox.setLayout(layout)
