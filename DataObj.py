import sys
import cv2
import numpy as np


class DataObj():
    def __init__(self):
        self.preamble = preambleImage('resources/AA.png')
        self.code = codeExampleBasic()
        self.input = cv2.imread('resources/AA.png', cv2.IMREAD_COLOR)
        print(self.input)
        self.runCode()

    def runCode(self):
        _locals = locals()
        print("Executing")
        print(self.preamble+"\n"+self.code)
        try:
            exec(self.preamble+"\n"+self.code, globals(), _locals)
            self.output = _locals['output_rgb']
            self.updateViewer()
        except BaseException as inst:
            print("Failed to run code:", inst)
            self.setMessage("Failed to run code: {}".format(inst))
        else:
            self.setMessage("Updated")

    def updateCode(self, newCode):
        self.code = newCode
        self.runCode()

    def updateViewer(self):
        try:
            self.viewer.updateView()
        except:
            print("Can't update viewer")

    def setMessage(self, msg):
        try:
            self.app.setMessage(msg)
        except BaseException as inst:
            print("Failed to set message: {}".format(inst))


def preambleImage(filename):
    return """
import cv2
frame = cv2.imread(\'{filename}\',cv2.IMREAD_COLOR)
    """.format(filename=filename)


def codeExampleBasic():
    return """
temp = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
output_rgb = cv2.cvtColor(temp, cv2.COLOR_GRAY2RGB)
    """


if __name__ == "__main__":
    d = DataObj()
    cv2.imshow("Test", d.output)
    cv2.waitKey(0)
