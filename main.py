# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
from functools import partial
import random

from PySide6.QtWidgets import QApplication, QWidget , QMessageBox
# ya mishe hamaru ba * import kard
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.game = [[None for i in range(3)] for j in range(3)]
        self.game[0][0] = self.ui.btn_00
        self.game[0][1] = self.ui.btn_01
        self.game[0][2] = self.ui.btn_02
        self.game[1][0] = self.ui.btn_10
        self.game[1][1] = self.ui.btn_11
        self.game[1][2] = self.ui.btn_12
        self.game[2][0] = self.ui.btn_20
        self.game[2][1] = self.ui.btn_21
        self.game[2][2] = self.ui.btn_22
        self.ui.show()
        self.player = 1
        self.player1_wins = 0
        self.player2_wins = 0
        self.draw = 0
        for i in range(3):
            for j in range(3):
                self.game[i][j].clicked.connect(partial(self.play, i, j))

        self.ui.btn_new.clicked.connect(self.new)
        self.ui.setWindowTitle('Tic Tac Toe')

    def play(self, i, j):
        if self.game[i][j].text() == "":
            if self.player == 1:
                self.game[i][j].setText('X')
                self.game[i][j].setStyleSheet('color :blue ; background-color: #CCFFFF')
                self.player = 2
                if self.ui.rb_p_vs_cpu.isChecked():
                    while True:
                        r = random.randint(0,2)
                        c = random.randint(0,2)
                        if self.game[r][c].text() == "":
                            self.game[r][c].setText('O')
                            self.game[r][c].setStyleSheet('color :red ; background-color : #FFCCCC')
                            self.player = 1
                            break


            elif self.player == 2:
                if self.ui.rb_p_vs_p.isChecked():
                    self.game[i][j].setText('O')
                    self.game[i][j].setStyleSheet('color :red ; background-color : #FFCCCC')
                    self.player = 1


                    # msg_box = QMessageBox()
                    # msg_box.setText('در دست تعمیر')
                    # msg_box.exec_()
        self.check()

    def check(self):
        # if self.game[0][0] == "X" and self.game[0][1] == "X" and self.game[0][2] == "X":

        if all(self.game[0][i].text() == 'X' for i in range(3)) or \
                all(self.game[1][i].text() == 'X' for i in range(3)) or \
                all(self.game[2][i].text() == 'X' for i in range(3)) or \
                all(self.game[i][0].text() == 'X' for i in range(3)) or \
                all(self.game[i][1].text() == 'X' for i in range(3)) or \
                all(self.game[i][2].text() == 'X' for i in range(3)) or \
                self.game[0][2].text() == 'X' and self.game[1][1].text() == 'X' and self.game[2][0].text() == 'X' \
                or self.game[0][0].text() == 'X' and self.game[1][1].text() == 'X' and self.game[2][2].text() == 'X':
            self.player1_wins +=1
            self.ui.lbl_scr0.setText(str(self.player1_wins))
            msg_box = QMessageBox()
            msg_box.setText('بازیکن شماره ۱ برنده شد!')

            msg_box.exec_()
            self.newgame()
        elif all(self.game[0][i].text() == 'O' for i in range(3)) or \
                all(self.game[1][i].text() == 'O' for i in range(3)) or \
                all(self.game[2][i].text() == 'O' for i in range(3)) or \
                all(self.game[i][0].text() == 'O' for i in range(3)) or \
                all(self.game[i][1].text() == 'O' for i in range(3)) or \
                all(self.game[i][2].text() == 'O' for i in range(3)) or \
                self.game[0][2].text() == 'O' and self.game[1][1].text() == 'O' and self.game[2][0].text() == 'O' \
                or self.game[0][0].text() == 'O' and self.game[1][1].text() == 'O' and self.game[2][2].text() == 'O':
            self.player2_wins +=1
            self.ui.lbl_scr2.setText(str(self.player2_wins))
            msg_box = QMessageBox()
            msg_box.setText('بازیکن شماره 2 برنده شد!')
            msg_box.exec_()
            self.newgame()

        elif all([self.game[0][i].text()!='' for i in range(3)]) and \
            all([self.game[1][i].text()!='' for i in range(3)]) and \
            all([self.game[2][i].text() != '' for i in range(3)]):
            self.draw += 1
            self.ui.lbl_scr1.setText(str(self.draw))
            msg_box = QMessageBox()
            msg_box.setText('بازی مساوی شد!')
            msg_box.exec_()
            self.newgame()


    def newgame(self):
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText("")
                self.game[i][j].setStyleSheet('background-color : #FFFFFF')

        # for i in range(3):
        #     for j in range(3):
        #         self.game[i][j].setStylesheet("background-color:red")
        #         self.game[i][j].setText('s')

    def new(self):
        self.player = 1
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText("")
                self.game[i][j].setStyleSheet('background-color : #FFFFFF')
                self.player1_wins = 0
                self.player2_wins = 0
                self.draw = 0
                self.ui.lbl_scr0.setText(str(self.player1_wins))
                self.ui.lbl_scr1.setText(str(self.draw))
                self.ui.lbl_scr2.setText(str(self.player2_wins))






        # for i in range(3):
        #     for j in range(3):
        #         self.game[i][j].setText("")
        #         self.game[i][j].setStyleSheet('background-color : #FFFFFF')
        # self.player1_wins = 0
        # self.player2_wins = 0
        # self.draw = 0

if __name__ == "__main__":
    app = QApplication([])
    widget = Main()
    sys.exit(app.exec_())
