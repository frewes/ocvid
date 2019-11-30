import sys
from PyQt5 import QtWidgets as qtw
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from MainWidget import MainWidget


class App(qtw.QMainWindow):

    def __init__(self, parentApp, data):
        super().__init__()
        self.title = 'OCVID OpenCV Integrated Development'
        self.left = 0
        self.top = 0
        self.width = 640
        self.height = 480
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.parent = parentApp
        self.setWindowIcon(QIcon('./opencv-logo.ico'))
        self.data = data
        self.data.app = self

        self.table_widget = MainWidget(self)
        self.setCentralWidget(self.table_widget)
        self.statusBar().showMessage('Loaded.')
        self.initMenu()
        self.show()

    def initMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        #streamMenu = mainMenu.addMenu('Stream')
        #helpMenu = mainMenu.addMenu('Help')

        for x in qtw.QStyleFactory.keys():
            styleAct = qtw.QAction(QIcon(''), x, self)
            styleAct.setStatusTip('Set style to ' + x)
            styleAct.triggered.connect(lambda checked, style=x: self.handleStyleChanged(
                qtw.QStyleFactory.create(style)))
            viewMenu.addAction(styleAct)

        saveAct = qtw.QAction(QIcon(''), "Save", self)
        saveAct.setStatusTip('Save current python code')
        saveAct.setShortcut('Ctrl+S')
        saveAct.triggered.connect(self.handleSave)
        saveAsAct = qtw.QAction(QIcon(''), "Save as...", self)
        saveAsAct.setStatusTip('Save current python code as...')
        saveAsAct.setShortcut('Ctrl+Shift+S')
        saveAsAct.triggered.connect(self.handleSaveAs)
        loadAct = qtw.QAction(QIcon(''), "Open", self)
        loadAct.setStatusTip('Open python file')
        loadAct.setShortcut('Ctrl+O')
        loadAct.triggered.connect(self.handleLoad)

        exitAct = qtw.QAction(QIcon('exit24.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)
        fileMenu.addAction(saveAct)
        fileMenu.addAction(saveAsAct)
        fileMenu.addAction(loadAct)
        fileMenu.addAction(exitAct)

        commentAct = qtw.QAction(QIcon(''), "Comment block", self)
        commentAct.setStatusTip('Comment line')
        commentAct.setShortcut('Ctrl+/')
        commentAct.triggered.connect(self.handleComment)
        editMenu.addAction(commentAct)

    def setMessage(self, log):
        print("Setting message", log)
        self.statusBar().showMessage(log)

    def handleStyleChanged(self, style):
        self.parent.setStyle(style)

    def handleSave(self):
        print("TODO save")

    def handleSaveAs(self):
        print("TODO save as")

    def handleLoad(self):
        print("TODO load")

    def handleComment(self):
        print("TODO comment")

    def closeEvent(self, event):
        self.data.stopVid()
        event.accept()  # let the window close
