from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QTimer
from PySide2.QtGui import QImage, QPixmap
import cv2

class Camera():
    def __init__(self):
        qfile_states = QFile("./UI/main.ui")
        qfile_states.open(QFile.ReadOnly)
        qfile_states.close()
        self.ui = QUiLoader().load(qfile_states)   

        self.ui.btn_connect_camera.clicked.connect(self.camera_init)
        self.camera_timer = QTimer()
        self.camera_timer.timeout.connect(self.read_img)

    def camera_init(self):
        self.cap = cv2.VideoCapture(0)
        self.camera_timer.start(30)

    def read_img(self):
        ret, img = self.cap.read()
        if ret:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            qimg = QImage(img, img.shape[1], img.shape[0], img.strides[0], QImage.Format_RGB888)
            self.ui.lb_img.setPixmap(QPixmap.fromImage(qimg))

if __name__ == '__main__':
    app = QApplication([])
    camera = Camera()
    camera.ui.show()
    app.exec_()