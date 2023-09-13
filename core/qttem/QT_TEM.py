import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

#from PyQt6.QtCore import Qt
# from PyQt6.QtWidgets import (QWidget, QToolTip,QPushButton, QApplication,QMainWindow,QMenu,QFrame,QVBoxLayout, QSplitter)
# from PyQt6.QtGui import QIcon, QAction


class QT_INIT(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.createLeftMenu()

    def initUI(self):
        self.setWindowTitle('Peristaltic pump flow control interface')
        self.setGeometry(300, 300, 1000, 800)

        # 创建左侧菜单栏
        left_menu = self.createLeftMenu()

        # 创建内容窗口
        content_frame = QFrame(self)
        content_frame.setStyleSheet("background-color: #2E4053;")

        # 创建一个分割窗口，左侧是菜单栏，右侧是内容窗口
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(left_menu)
        splitter.addWidget(content_frame)
        # 设置分割条的位置
        splitter.setSizes([150, 200])

        self.setCentralWidget(splitter)

        self.show()











