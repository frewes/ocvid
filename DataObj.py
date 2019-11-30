import sys
import cv2
import numpy as np

import threading


class DataObj():
    def __init__(self):
        self.frame_no = 0
        self.stoppedVid = False
        self.videoFile = 'resources/AA.mp4'
        self.preamble = preambleVideoDisplay(self.videoFile, self.frame_no)
        self.code = codeExampleBasic()

        self.vidCap = cv2.VideoCapture(self.videoFile)
        self.number_of_frames = int(
            self.vidCap.get(cv2.CAP_PROP_FRAME_COUNT))
        (res, self.input) = self.vidCap.read()
        #self.input = cv2.imread('resources/AA.png', cv2.IMREAD_COLOR)
        print(self.input)
        self.runCode()

    def runCode(self):
        _locals = locals()
        # print("Executing")
        # print(self.preamble+"\n"+self.code)
        self.vidCap.set(cv2.CAP_PROP_POS_FRAMES, self.frame_no-1)
        res, self.input = self.vidCap.read()
        try:
            exec(preambleVideoActual(self.videoFile, self.frame_no) +
                 "\n"+self.code, globals(), _locals)
            self.output = _locals['output_rgb']
        except BaseException as inst:
            print("Failed to run code:", inst)
            self.setMessage("Failed to run code: {}".format(inst))
        else:
            self.setMessage("Updated")
        self.updateViewer()

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

    def playVid(self):
        if (self.frame_no > self.number_of_frames):
            if (self.stoppedVid):
                self.frame_no = 0
            else:
                self.stoppedVid = True
                return
        self.timer = threading.Timer(0.01, self.advVid)
        self.timer.start()  # after 60 seconds, 'callback' will be called
        self.stoppedVid = False

    def advVid(self):
        self.stepVid()
        if (not self.stoppedVid):
            self.playVid()

    def stepVid(self):
        self.frame_no = self.frame_no + 1
        self.preamble = preambleVideoActual(self.videoFile, self.frame_no)
        self.runCode()

    def stopVid(self):
        self.timer.cancel()
        self.stoppedVid = True

    def restartVid(self):
        self.frame_no = 0
        self.runCode()


def preambleImage(filename):
    return """
import cv2
frame = cv2.imread(\'{filename}\',cv2.IMREAD_COLOR)
    """.format(filename=filename)


def preambleVideoDisplay(filename, frame_no):
    return """
import cv2
cap = cv2.VideoCapture(\'{filename}\')
while(True):
    res, frame = cap.read()
    """.format(filename=filename, frame_no=frame_no)


def preambleVideoActual(filename, frame_no):
    return """
import cv2
cap = cv2.VideoCapture(\'{filename}\')
frame_number = {frame_no}
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number-1)
res, frame = cap.read()
    """.format(filename=filename, frame_no=frame_no)


def codeExampleBasic():
    return """
temp = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
output_rgb = cv2.cvtColor(temp, cv2.COLOR_GRAY2RGB)
    """


if __name__ == "__main__":
    d = DataObj()
    cv2.imshow("Test", d.output)
    cv2.waitKey(0)
