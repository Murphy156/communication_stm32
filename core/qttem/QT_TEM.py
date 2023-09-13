import sys
from PyQt6.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication,QMainWindow,QMenu)
from PyQt6.QtGui import QIcon, QAction


class QT_INIT(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        menubar = self.menuBar()
        fileMenu1 = menubar.addMenu('File')     #主菜单
        fileMenu2 = menubar.addMenu('Exit')


        impMenu = QMenu('Import', self)         #子菜单
        impAct = QAction('Import mail', self)   #从菜单动作
        impMenu.addAction(impAct)               #从子菜单进入到从菜单

        newAct = QAction('New', self)

        fileMenu1.addAction(newAct)
        fileMenu1.addMenu(impMenu)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Submenu')
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())


