# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MIPS_UI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("QPushButton {\n"
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
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
"")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 20, 901, 621))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(901, 621))
        self.tabWidget.setMaximumSize(QtCore.QSize(901, 621))
        self.tabWidget.setStyleSheet("QTabWidget {\n"
"    background-color : rgb(39, 40, 34); \n"
"}\n"
"\n"
"QTabWidget::pane { border: 0; }\n"
"\n"
"QTabBar::tab{\n"
"    min-height: 20px; \n"
"    min-width: 100px;\n"
"    background-color: rgb(71, 71, 71);\n"
"    font: 8pt \"Consolas\";\n"
"}\n"
"\n"
"QTabBar::tab::selected {\n"
"    background-color: rgb(102, 102, 102);\n"
"}\n"
"\n"
"QTabBar::tab::hover {\n"
"    background-color: rgb(90, 90, 90);\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.Assembler = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Assembler.sizePolicy().hasHeightForWidth())
        self.Assembler.setSizePolicy(sizePolicy)
        self.Assembler.setStyleSheet("QTabBar::tab{min-height: 30px; min-width: 80px;}")
        self.Assembler.setObjectName("Assembler")
        self.saveMIPS = QtWidgets.QPushButton(self.Assembler)
        self.saveMIPS.setGeometry(QtCore.QRect(440, 60, 101, 26))
        self.saveMIPS.setObjectName("saveMIPS")
        self.open = QtWidgets.QPushButton(self.Assembler)
        self.open.setGeometry(QtCore.QRect(310, 20, 97, 26))
        self.open.setStyleSheet("QPushButton {\n"
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
        self.open.setObjectName("open")
        self.saveCoe = QtWidgets.QPushButton(self.Assembler)
        self.saveCoe.setGeometry(QtCore.QRect(440, 20, 101, 26))
        self.saveCoe.setStyleSheet("QPushButton {\n"
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
        self.saveCoe.setObjectName("saveCoe")
        self.compile = QtWidgets.QPushButton(self.Assembler)
        self.compile.setGeometry(QtCore.QRect(310, 60, 97, 26))
        self.compile.setObjectName("compile")
        self.saveBin = QtWidgets.QPushButton(self.Assembler)
        self.saveBin.setGeometry(QtCore.QRect(560, 20, 111, 26))
        self.saveBin.setObjectName("saveBin")
        self.editor = QtWidgets.QTextEdit(self.Assembler)
        self.editor.setGeometry(QtCore.QRect(40, 110, 341, 431))
        self.editor.setStyleSheet("QTextEdit {\n"
"    background-color : rgb(39, 40, 34); \n"
"    color : rgb(252, 255, 255); \n"
"    font: \"Consolas\";\n"
"}\n"
"\n"
"")
        self.editor.setObjectName("editor")
        self.saveMIPSas = QtWidgets.QPushButton(self.Assembler)
        self.saveMIPSas.setGeometry(QtCore.QRect(560, 60, 111, 26))
        self.saveMIPSas.setObjectName("saveMIPSas")
        self.textList2 = QtWidgets.QListWidget(self.Assembler)
        self.textList2.setGeometry(QtCore.QRect(460, 110, 261, 431))
        self.textList2.setStyleSheet("QTextEdit {\n"
"    background-color : rgb(39, 40, 34); \n"
"    color : rgb(252, 255, 255); \n"
"    font: \"Consolas\";\n"
"}\n"
"")
        self.textList2.setObjectName("textList2")
        self.debugMode = QtWidgets.QPushButton(self.Assembler)
        self.debugMode.setGeometry(QtCore.QRect(180, 30, 97, 41))
        self.debugMode.setStyleSheet("QPushButton {\n"
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
        self.debugMode.setObjectName("debugMode")
        self.tabWidget.addTab(self.Assembler, "")
        self.Disassembler = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Disassembler.sizePolicy().hasHeightForWidth())
        self.Disassembler.setSizePolicy(sizePolicy)
        self.Disassembler.setObjectName("Disassembler")
        self.binEditor = QtWidgets.QTextEdit(self.Disassembler)
        self.binEditor.setGeometry(QtCore.QRect(40, 110, 341, 431))
        self.binEditor.setStyleSheet("QTextEdit {\n"
"    background-color : rgb(39, 40, 34); \n"
"    color : rgb(252, 255, 255); \n"
"    font: \"Consolas\";\n"
"}\n"
"")
        self.binEditor.setObjectName("binEditor")
        self.mipsCode = QtWidgets.QListWidget(self.Disassembler)
        self.mipsCode.setGeometry(QtCore.QRect(460, 110, 261, 431))
        self.mipsCode.setStyleSheet("QTextEdit {\n"
"    background-color : rgb(39, 40, 34); \n"
"    color : rgb(252, 255, 255); \n"
"    font: \"Consolas\";\n"
"}\n"
"")
        self.mipsCode.setObjectName("mipsCode")
        self.open2 = QtWidgets.QPushButton(self.Disassembler)
        self.open2.setGeometry(QtCore.QRect(300, 20, 97, 26))
        self.open2.setObjectName("open2")
        self.saveBin2 = QtWidgets.QPushButton(self.Disassembler)
        self.saveBin2.setGeometry(QtCore.QRect(420, 60, 97, 26))
        self.saveBin2.setObjectName("saveBin2")
        self.saveMIPS2 = QtWidgets.QPushButton(self.Disassembler)
        self.saveMIPS2.setGeometry(QtCore.QRect(420, 20, 97, 26))
        self.saveMIPS2.setObjectName("saveMIPS2")
        self.compile2 = QtWidgets.QPushButton(self.Disassembler)
        self.compile2.setGeometry(QtCore.QRect(300, 60, 97, 26))
        self.compile2.setObjectName("compile2")
        self.tabWidget.addTab(self.Disassembler, "")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(720, 0, 75, 23))
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
        self.miniButton = QtWidgets.QPushButton(self.centralwidget)
        self.miniButton.setGeometry(QtCore.QRect(640, 0, 75, 23))
        self.miniButton.setStyleSheet("QPushButton {\n"
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
        self.miniButton.setObjectName("miniButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 7, 161, 21))
        self.label.setStyleSheet("QLabel {\n"
"    font: 12pt \"Consolas\";\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p>Disassembler</p></body></html>"))
        self.saveMIPS.setText(_translate("MainWindow", "Save MIPS"))
        self.saveMIPS.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.open.setText(_translate("MainWindow", "Open"))
        self.open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.saveCoe.setText(_translate("MainWindow", "Save COE"))
        self.saveCoe.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.compile.setText(_translate("MainWindow", "Compile"))
        self.compile.setShortcut(_translate("MainWindow", "Ctrl+B"))
        self.saveBin.setText(_translate("MainWindow", "Save bin"))
        self.saveBin.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.saveMIPSas.setText(_translate("MainWindow", "Save MIPS as"))
        self.saveMIPSas.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.debugMode.setText(_translate("MainWindow", "Debug Mode"))
        self.debugMode.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Assembler), _translate("MainWindow", "Assembler"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.Assembler), _translate("MainWindow", "Assembler"))
        self.open2.setText(_translate("MainWindow", "Open"))
        self.open2.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.saveBin2.setText(_translate("MainWindow", "Save Bin"))
        self.saveBin2.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.saveMIPS2.setText(_translate("MainWindow", "Save MIPS"))
        self.saveMIPS2.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.compile2.setText(_translate("MainWindow", "Compile"))
        self.compile2.setShortcut(_translate("MainWindow", "Ctrl+B"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Disassembler), _translate("MainWindow", "Disassembler"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.Disassembler), _translate("MainWindow", "Disassembler"))
        self.closeButton.setText(_translate("MainWindow", "X"))
        self.miniButton.setText(_translate("MainWindow", "—"))
        self.label.setText(_translate("MainWindow", "MIPS Editor"))

