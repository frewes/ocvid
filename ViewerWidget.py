import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QImage, QPixmap, QPainter


class ViewerWidget(qtw.QWidget):

    def __init__(self, parent):
        super(qtw.QWidget, self).__init__(parent)
        self.horizontalGroupBox = qtw.QGroupBox("Result viewer")
        self.data = parent.data
        self.data.viewer = self  # gross data incest but whatever
        self.buildView()

        windowLayout = qtw.QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.data.updateViewer = self.updateView

    def updateView(self):
        print("Update view")
        height, width, colors = self.data.output.shape
        bytesPerLine = width*3
        imageG = QImage(self.data.output.data, width, height,
                        bytesPerLine, QImage.Format_RGB888)

        self.outputView.setPixmap(QPixmap(imageG))

    def buildView(self):
        layout = qtw.QVBoxLayout()
        label1 = qtw.QLabel()
        label1.setText("Input")
        layout.addWidget(label1)
        height, width, colors = self.data.input.shape
        bytesPerLine = 3 * width
        image = QImage(self.data.input.data, width, height,
                       bytesPerLine, QImage.Format_RGB888)

        image = image.rgbSwapped()
        self.inputView = qtw.QLabel(self)
        self.inputView.setScaledContents(True)
        pixmap = QPixmap(image)
        self.inputView.setPixmap(pixmap)

        layout.addWidget(self.inputView)

        label2 = qtw.QLabel()
        label2.setText("Output")
        layout.addWidget(label2)

        self.outputView = qtw.QLabel(self)
        self.outputView.setScaledContents(True)
        height, width, colors = self.data.output.shape
        bytesPerLine = width*3
        imageG = QImage(self.data.output.data, width, height,
                        bytesPerLine, QImage.Format_RGB888)

        self.outputView.setPixmap(QPixmap(imageG))
        layout.addWidget(self.outputView)

        self.buttonPanel = qtw.QGroupBox("VideoControls")
        self.buttonPanel.setLayout(qtw.QHBoxLayout())

        self.buildControls()

        layout.addWidget(self.buttonPanel)

        self.horizontalGroupBox.setLayout(layout)

    def buildControls(self):
        playBtn = qtw.QPushButton("Play", self)
        stepBtn = qtw.QPushButton("Step", self)
        stopBtn = qtw.QPushButton("Stop", self)
        restartBtn = qtw.QPushButton("Restart", self)

        self.buttonPanel.layout().addWidget(playBtn)
        self.buttonPanel.layout().addWidget(stepBtn)
        self.buttonPanel.layout().addWidget(stopBtn)
        self.buttonPanel.layout().addWidget(restartBtn)

        self.buttonPanel.setDisabled(True)
