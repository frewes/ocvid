import sys
import PyQt5 as qt
from PyQt5 import QtWidgets as qtw
from PyQt5 import Qsci

import syntax


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

        self.header = qtw.QLabel(self)
        self.header.setText(self.data.preamble)
        layout.addWidget(self.header)
        self.editor = PythonEditor(self)
        self.editor.setText(self.data.code)
        layout.addWidget(self.editor)
        self.saveButton = qtw.QPushButton('Update!', self)
        self.saveButton.clicked.connect(self.update)
        layout.addWidget(self.saveButton)
        self.horizontalGroupBox.setLayout(layout)

    def update(self):
        print("Update")
        self.data.updateCode(self.editor.text())


class PythonEditor(Qsci.QsciScintilla):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLexer(Qsci.QsciLexerPython(self))
