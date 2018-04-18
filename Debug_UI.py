# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Debug_UI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DebugWindow(object):
    def setupUi(self, DebugWindow):
        DebugWindow.setObjectName("DebugWindow")
        DebugWindow.resize(700, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DebugWindow.sizePolicy().hasHeightForWidth())
        DebugWindow.setSizePolicy(sizePolicy)
        DebugWindow.setMaximumSize(QtCore.QSize(700, 500))
        DebugWindow.setStyleSheet("QPushButton {\n"
"    border-style: solid;\n"
"    border-width: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(62, 62, 62);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(DebugWindow)
        self.centralwidget.setStyleSheet("QWidget {\n"
"    background-color : rgb(39, 40, 34); \n"
"    color : rgb(252, 255, 255); \n"
"}\n"
"\n"
"QPushButton {\n"
"    border-style: solid;\n"
"    border-width: 0px;\n"
"    border-radius: 5px;\n"
"    background-color: rgb(58, 58, 58);\n"
"    font: 8pt \"Consolas\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(70, 70, 70);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QWidget#centralwidget {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(161, 161, 161);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(620, 3, 75, 23))
        self.closeButton.setStyleSheet("QPushButton {\n"
"    border-style: solid;\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"    background-color: rgb(58, 58, 58);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(70, 70, 70);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(220, 220, 220);\n"
"}\n"
"")
        self.closeButton.setObjectName("closeButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 10, 161, 21))
        self.label.setStyleSheet("QLabel {\n"
"    font: 12pt \"Consolas\";\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")
        self.step = QtWidgets.QPushButton(self.centralwidget)
        self.step.setGeometry(QtCore.QRect(250, 50, 97, 26))
        self.step.setStyleSheet("QPushButton {\n"
"    border-style: solid;\n"
"    border-width: 0px;\n"
"    border-radius: 5px;\n"
"    background-color: rgb(58, 58, 58);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(70, 70, 70);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(220, 220, 220);\n"
"}\n"
"")
        self.step.setObjectName("step")
        self.regsList = QtWidgets.QListWidget(self.centralwidget)
        self.regsList.setGeometry(QtCore.QRect(400, 100, 251, 381))
        self.regsList.setStyleSheet("QListWidget {\n"
"    background-color : rgb(39, 40, 34); \n"
"    color : rgb(252, 255, 255); \n"
"    font: \"Consolas\";\n"
"}\n"
"")
        self.regsList.setObjectName("regsList")
        self.binList = QtWidgets.QListWidget(self.centralwidget)
        self.binList.setGeometry(QtCore.QRect(50, 100, 291, 381))
        self.binList.setStyleSheet("QListWidget {\n"
"    background-color : rgb(39, 40, 34); \n"
"    color : rgb(252, 255, 255); \n"
"    font: \"Consolas\";\n"
"}\n"
"\n"
"")
        self.binList.setObjectName("binList")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(370, 50, 97, 26))
        self.reset.setStyleSheet("QPushButton {\n"
"    border-style: solid;\n"
"    border-width: 0px;\n"
"    border-radius: 5px;\n"
"    background-color: rgb(58, 58, 58);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(70, 70, 70);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(220, 220, 220);\n"
"}\n"
"")
        self.reset.setObjectName("reset")
        DebugWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DebugWindow)
        QtCore.QMetaObject.connectSlotsByName(DebugWindow)

    def retranslateUi(self, DebugWindow):
        _translate = QtCore.QCoreApplication.translate
        DebugWindow.setWindowTitle(_translate("DebugWindow", "MainWindow"))
        self.closeButton.setText(_translate("DebugWindow", "X"))
        self.label.setText(_translate("DebugWindow", "Debug Mode"))
        self.step.setText(_translate("DebugWindow", "Step"))
        self.step.setShortcut(_translate("DebugWindow", "Ctrl+B"))
        self.reset.setText(_translate("DebugWindow", "Reset"))
        self.reset.setShortcut(_translate("DebugWindow", "Ctrl+B"))

