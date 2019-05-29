import cv2
import numpy as np


class DataObj():
    def __init__(self):
        print("Hi")
        self.preamble = preambleImage('media/AA.png')
        self.code = codeExampleBasic()
        self.input = cv2.imread('media/AA.png',cv2.IMREAD_COLOR)
        self.runCode()

    def runCode(self):
        _locals = locals()
        print("Executing")
        print(self.preamble+"\n"+self.code)
        exec(self.preamble+"\n"+self.code, globals(), _locals)
        print(_locals)
        self.output = _locals['output_rgb']

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
    cv2.imshow("Test",d.output)
    cv2.waitKey(0)
