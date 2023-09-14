import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

#from PyQt6.QtCore import Qt
# from PyQt6.QtWidgets import (QWidget, QToolTip,QPushButton, QApplication,QMainWindow,QMenu,QFrame,QVBoxLayout, QSplitter)
# from PyQt6.QtGui import QIcon, QAction

class SubWindow1(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("子窗口")
        self.setGeometry(300, 300, 1000, 800)

# 创建垂直布局
        layout = QVBoxLayout()

        # 创建实线框架（QFrame）作为分隔区域
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.Box)
        separator.setFrameShadow(QFrame.Shadow.Sunken)

        # 向布局添加分隔区域和一些文本或其他控件
        layout.addWidget(separator)
        layout.addWidget(QWidget())  # 用于占位的小部件
        layout.addWidget(QWidget())  # 用于占位的小部件

        # 将布局设置为子窗口的布局
        self.setLayout(layout)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Peristaltic Pump Debugging Assistant")
        self.setGeometry(300, 300, 1000, 800)
        # 创建一个主界面容器
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # 创建垂直布局
        main_layout = QVBoxLayout()

        # 创建按钮布局
        button_layout = QHBoxLayout()

        # 创建四个按钮
        button1 = QPushButton("General Control Interface")
        button1.setFixedSize(300, 50)  # 设置按钮1的尺寸
        button1.clicked.connect(self.open_window1)

        button2 = QPushButton("Flow Observation")
        button2.setFixedSize(300, 50)  # 设置按钮2的尺寸

        button3 = QPushButton("Liquid Level Observation")
        button3.setFixedSize(300, 50)  # 设置按钮3的尺寸

        button4 = QPushButton("PID Speed Debugging")
        button4.setFixedSize(300, 50)  # 设置按钮4的尺寸

        # 使用样式表设置按钮的背景颜色和字体颜色
        button1.setStyleSheet("background-color: gray; color: white;")
        button2.setStyleSheet("background-color: gray; color: white;")
        button3.setStyleSheet("background-color: gray; color: white;")
        button4.setStyleSheet("background-color: gray; color: white;")

        # 将按钮添加到按钮布局中
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        button_layout.addWidget(button3)
        button_layout.addWidget(button4)

        # 添加水平布局到垂直布局
        main_layout.addLayout(button_layout)

        # 创建一个伸展因子，将按钮推到窗口的顶部
        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        main_layout.addItem(spacer)

        # 设置主窗口容器的布局为垂直布局
        main_widget.setLayout(main_layout)

        # 设置主窗口的背景颜色
        self.setStyleSheet("background-color: lightblack;")

        # 连接按钮的点击事件到相应的槽函数
        button2.clicked.connect(self.open_window2)
        button3.clicked.connect(self.open_window3)
        button4.clicked.connect(self.open_window4)

        # 创建一个堆叠窗口，用于显示子窗口
        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)

    def open_window1(self):
        sub_window1 = SubWindow1()
        self.stacked_widget.addWidget(sub_window1)
        self.stacked_widget.setCurrentWidget(sub_window1)

    def open_window2(self):
        # 打开窗口2的代码
        pass

    def open_window3(self):
        # 打开窗口3的代码
        pass

    def open_window4(self):
        # 打开窗口4的代码
        pass










