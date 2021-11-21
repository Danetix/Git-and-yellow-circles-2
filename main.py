import sys
import random

from PyQt5 import uic, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI(self)

    def initUI(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(619, 459)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 30, 101, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 619, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Click to me"))

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        size = random.randint(10, 100)
        color_1 = random.randint(0, 255)
        color_2 = random.randint(0, 255)
        color_3 = random.randint(0, 255)

        qp.setBrush(QColor(color_1, color_2, color_3))
        qp.drawEllipse(random.randint(0, 200), random.randint(0, 200), size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
