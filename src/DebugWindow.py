from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from Debug_UI import Ui_DebugWindow
from PyQt5.QtCore import Qt, QPoint


class DebugWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_DebugWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.oldPos = self.pos()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
