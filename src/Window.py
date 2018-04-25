# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textList2 = QtWidgets.QListWidget(self.centralwidget)
        self.textList2.setGeometry(QtCore.QRect(470, 100, 261, 431))
        self.textList2.setObjectName("textList2")
        self.open = QtWidgets.QPushButton(self.centralwidget)
        self.open.setGeometry(QtCore.QRect(230, 20, 97, 26))
        self.open.setObjectName("open")
        self.saveMIPS = QtWidgets.QPushButton(self.centralwidget)
        self.saveMIPS.setGeometry(QtCore.QRect(360, 60, 101, 26))
        self.saveMIPS.setObjectName("saveMIPS")
        self.saveCoe = QtWidgets.QPushButton(self.centralwidget)
        self.saveCoe.setGeometry(QtCore.QRect(360, 20, 101, 26))
        self.saveCoe.setObjectName("saveCoe")
        self.editor = QtWidgets.QTextEdit(self.centralwidget)
        self.editor.setGeometry(QtCore.QRect(50, 100, 371, 431))
        self.editor.setObjectName("editor")
        self.saveBin = QtWidgets.QPushButton(self.centralwidget)
        self.saveBin.setGeometry(QtCore.QRect(480, 20, 111, 26))
        self.saveBin.setObjectName("saveBin")
        self.compile = QtWidgets.QPushButton(self.centralwidget)
        self.compile.setGeometry(QtCore.QRect(230, 60, 97, 26))
        self.compile.setObjectName("compile")
        self.saveMIPSas = QtWidgets.QPushButton(self.centralwidget)
        self.saveMIPSas.setGeometry(QtCore.QRect(480, 60, 111, 26))
        self.saveMIPSas.setObjectName("saveMIPSas")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open.setText(_translate("MainWindow", "Open"))
        self.saveMIPS.setText(_translate("MainWindow", "Save MIPS"))
        self.saveCoe.setText(_translate("MainWindow", "Save coe"))
        self.saveBin.setText(_translate("MainWindow", "Save bin"))
        self.compile.setText(_translate("MainWindow", "Compile"))
        self.saveMIPSas.setText(_translate("MainWindow", "Save MIPS as"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))

