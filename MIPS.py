from MIPS_UI import Ui_MainWindow
from DebugWindow import DebugWindow

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QDesktopWidget
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import Qt, QPoint

from Assembler import assembler
from Disassembler import disassembler
from Debug import run
from Utils import *
from SyntaxHighlight import MIPSHighlighter
import sys


current_color = QColor(56, 84, 107)
bk_color = QColor(39, 40, 34)
default_font = QFont('Consolas')


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.ui.tabWidget.setFrameShape(QMainWindow.NoFrame)

        # Assembler -------------

        # Debug Mode
        self.debug = DebugWindow()
        # self.debug.setWindowFlags(Qt.FramelessWindowHint)
        # self.debug.ui = Ui_DebugWindow()
        # self.debug.ui.setupUi(self.debug)
        self.debug.hide()

        # self.show()

        self.mips = None
        self.num_lines1 = 0
        self.num_lines2 = 0
        self.fname = None

        self.regs = {key: 0 for key in registers_table.keys()}
        self.current_line = 0
        self.debug_PC = None
        self.labels = {}

        self.ui.saveMIPS.clicked.connect(self.saveMIPS)
        self.ui.saveMIPSas.clicked.connect(self.saveMIPSas)
        self.ui.open.clicked.connect(self.openFile)
        self.ui.compile.clicked.connect(self.compile)
        self.ui.saveBin.clicked.connect(self.saveBin)
        self.ui.saveCoe.clicked.connect(self.saveCoe)

        # Debug --------------
        self.ui.debugMode.clicked.connect(self.startDebug)
        self.debug.ui.step.clicked.connect(self.step)
        self.debug.ui.closeButton.clicked.connect(self.closeDebug)
        self.debug.ui.reset.clicked.connect(self.startDebug)
        # self.debug_oldPos = self.debug.pos()

        # Disassembler ----------

        self.bins = None
        self.bin_fname = None
        self.codes = None
        self.num_lines11 = 0
        self.num_lines22 = 0

        self.ui.open2.clicked.connect(self.openBinFile)
        self.ui.compile2.clicked.connect(self.compile2)
        self.ui.saveBin2.clicked.connect(self.saveBin2)
        self.ui.saveMIPS2.clicked.connect(self.saveMIPS2)

        self.ui.closeButton.clicked.connect(self.closeWindow)
        self.ui.miniButton.clicked.connect(self.minimize)
        self.oldPos = self.pos()

        # set font -------------------------
        self.debug.ui.regsList.setFont(default_font)
        self.debug.ui.binList.setFont(default_font)
        self.ui.textList2.setFont(default_font)
        self.ui.mipsCode.setFont(default_font)
        self.ui.editor.setFont(default_font)
        self.ui.binEditor.setFont(default_font)

        # highlight -----------------------------
        self.highlight = MIPSHighlighter(self.ui.editor.document())
        # self.debug_highlight = MIPSHighlighter(self.debug.ui.binList.item(0).document())

    # debug ----------------------
    def startDebug(self):
        if self.mips is None:
            return

        textList = self.debug.ui.binList
        textList.clear()
        lines = self.mips.lines
        n = 0
        for line in lines:
            textList.addItem('{:<10d}'.format(n) + line)
            n += 1

        item = textList.item(0)
        item.setBackground(current_color)

        textList = self.debug.ui.regsList
        textList.clear()
        for reg in self.regs:
            self.regs[reg] = 0
            line = '{:<15}{:<15}'.format(reg, self.regs[reg])
            textList.addItem(line)

        self.labels = {}
        self.debug_PC = self.mips.base_addr
        self.current_line = 0
        self.debug.show()

    def step(self):
        bins = self.mips.codes
        n_lines = len(bins)
        if self.current_line < n_lines:
            self.regs, self.debug_PC = run(bins[self.current_line], self.regs, self.debug_PC, self.labels)
            # self.current_line += 1
            self.current_line = (self.debug_PC - self.mips.base_addr) // 4

        if self.current_line - 1 >= 0 and self.current_line < n_lines:
            item = self.debug.ui.binList.item(self.current_line - 1)
            item.setBackground(bk_color)

        if self.current_line < n_lines:
            for i in range(n_lines):
                item = self.debug.ui.binList.item(i)
                item.setBackground(bk_color)

            line_num = self.mips.line_table[self.current_line]
            item = self.debug.ui.binList.item(line_num)
            item.setBackground(current_color)

        textList = self.debug.ui.regsList
        textList.clear()
        for reg in self.regs:
            line = '{:<15}{:<15}'.format(reg, self.regs[reg])
            textList.addItem(line)

    def closeDebug(self):
        self.regs = {key: 0 for key in registers_table.keys()}
        self.current_line = 0
        self.debug_PC = None
        self.debug.hide()

    def closeWindow(self):
        self.debug.close()
        self.close()

    def minimize(self):
        self.setWindowState(Qt.WindowMinimized)

    # center
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

    # Disassembler ---------------------------------------

    def openBinFile(self):
        try:
            self.bin_fname = QFileDialog.getOpenFileName(self, 'Open File')[0]
            self.updateUI2()
        except FileNotFoundError as e:
            return

    def compile2(self):
        lines = self.ui.binEditor.toPlainText().split('\n')
        self.bins = lines
        self.codes = disassembler(self.bins)
        self.num_lines11 = 0
        self.num_lines22 = 0
        self.loadText2(self.codes, mode='D')

    def updateUI2(self):
        self.num_lines1 = 0
        self.num_lines2 = 0
        with open(self.bin_fname) as f:
            line = f.readline()
        self.bins = []
        for i in range(len(line) // 32):
            self.bins.append(line[i * 32:(i + 1) * 32] + '\n')
        self.loadText1(self.bins, 'D')

    # def saveBin2(self):
    #     bins = ''
    #     for line in self.bins:
    #         bins += line
    #     try:
    #         fname = QFileDialog.getSaveFileName(self, 'Save Binary Code')[0]
    #         with open(fname, 'w') as f:
    #             f.write(bins)
    #     except FileNotFoundError as e:
    #         return

    def saveBin2(self):
        bins = ''
        lines = self.ui.binEditor.toPlainText().split('\n')
        for line in lines:
            bins += line
        if self.bin_fname is None:
            self.bin_fname = QFileDialog.getSaveFileName(self, 'Save Bin ...')[0]
        f = open(self.bin_fname, 'w')
        f.write(bins)
        f.close()

    def saveMIPS2(self):
        mips = ''
        for code in self.codes:
            mips += code + '\n'
        fname = QFileDialog.getSaveFileName(self, 'Save MIPS ...')[0]
        f = open(fname, 'w')
        f.write(mips)
        f.close()

    def loadText1(self, lines, mode='A'):
        text = ''
        if mode == 'A':
            editor = self.ui.editor
        else:
            editor = self.ui.binEditor

        for line in lines:
            text += line
        editor.setText(text)

    def loadText2(self, lines, mode='A'):
        if mode == 'A':
            textList = self.ui.textList2
            num_lines2 = self.num_lines2
        else:
            textList = self.ui.mipsCode
            num_lines2 = self.num_lines22

        textList.clear()
        for line in lines:
            textList.addItem('{:<10d}'.format(num_lines2) + line)
            num_lines2 += 1

    # Assembler --------------------------------------------

    def setFname(self, fname):
        self.fname = fname

    def saveMIPS(self):
        if self.fname is None:
            self.fname = QFileDialog.getSaveFileName(self, 'Save MIPS ...')[0]
        f = open(self.fname, 'w')
        f.write(self.ui.editor.toPlainText())
        f.close()

    def saveMIPSas(self):
        try:
            fname = QFileDialog.getSaveFileName(self, 'Save MIPS as ...')[0]
            f = open(fname, 'w')
            f.write(self.ui.editor.toPlainText())
            f.close()
        except FileNotFoundError as e:
            return

    def openFile(self):
        try:
            self.fname = QFileDialog.getOpenFileName(self, 'Open File')[0]
            self.updateUI()
        except FileNotFoundError as e:
            return

    def compile(self):
        lines = self.ui.editor.toPlainText().split('\n')
        self.num_lines1 = 0
        self.num_lines2 = 0
        self.mips = assembler(lines)
        self.loadText2(self.mips.hexs())

    def updateUI(self):
        self.num_lines1 = 0
        self.num_lines2 = 0
        with open(self.fname) as f:
            lines = list(f.readlines())
        self.mips = assembler(lines)
        self.loadText1(lines)
        self.loadText2(self.mips.hexs())

    def saveBin(self):
        bins = ''
        for line in self.mips.codes:
            bins += line
        try:
            fname = QFileDialog.getSaveFileName(self, 'Save Binary Code')[0]
            with open(fname, 'w') as f:
                f.write(bins)
        except FileNotFoundError as e:
            return

    def saveCoe(self):
        hexs = self.mips.hexs()
        coe = 'memory_initialization_radix = 16;\nmemory_initialization_vector = \n'
        for line in hexs:
            coe += line + ',\n'
        try:
            fname = QFileDialog.getSaveFileName(self, 'Save coe File')[0]
            with open(fname, 'w') as f:
                f.write(coe)
        except FileNotFoundError as e:
            return


if __name__ == '__main__':
    # fname = '/home/deng/Documents/code/python3/MIPS/01.txt'
    # with open(fname) as f:
    #     lines = list(f.readlines())
    # mips = assembler(lines)
    app = QApplication(sys.argv)
    win = MainWindow()
    # win.setFname(fname)
    # win.updateUI()
    win.show()

    sys.exit(app.exec())
