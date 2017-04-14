#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import pexpect
import locale
import sys
from imp import reload
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QCoreApplication

reload(sys)
locale.setlocale(locale.LC_ALL, '')

lbl = 'Router reboot'


class TestGui(QWidget):
    def __init__(self):
        QDialog.__init__(self)
        fntMyFont2 = QtGui.QFont("Arial")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.red)
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.blue)
        fntMyFont2.setItalic(False)
        fntMyFont2.setBold(True)
        fntMyFont2.setPixelSize(26)
        self.setGeometry(800, 450, 194, 32)
        color = QColor(0, 0, 0)
        btnQuit = QPushButton(lbl, self)
        btnQuit.setGeometry(2, 2, 190, 28)
        btnQuit.setFont(fntMyFont2)
        btnQuit.setPalette(palette)
        btnQuit.clicked.connect(some_func)
        btnQuit.clicked.connect(QCoreApplication.instance().quit)
        self.show()


def some_func():
    child = pexpect.spawn('telnet 192.168.0.1')
    child.expect('ogin: ')
    child.sendline('******')  # Собственно логин
    child.expect('assword:')
    child.sendline('******')  # Пароль
    child.sendline('echo работает')  # ЗДЕСЬ команда. В данном случае reboot
    child.sendline('exit')
    child.expect(pexpect.EOF)
    lbl = child.before.decode('utf-8')
    print(lbl)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestGui()
    window.setWindowTitle("D'Link")
    window.setWindowIcon(QtGui.QIcon('/home/fil/pictures/icons/dlink.png'))
    window.show()
    sys.exit(app.exec_())