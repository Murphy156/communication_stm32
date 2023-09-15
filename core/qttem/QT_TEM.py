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

        self.setGeometry(300, 200, 10, 10)
        # 设置子窗口的背景颜色
        self.setStyleSheet("background-color: lightblue;")
        # 创建水平布局
        layout = QHBoxLayout()

        # 创建实线框架（QFrame）作为分隔区域
        separator1 = QFrame()
        separator1.setFrameShape(QFrame.Shape.Box)
        separator1.setFrameShadow(QFrame.Shadow.Sunken)

        # 向布局添加分隔区域和一些文本或其他控件
        layout.addWidget(separator1)
        layout.addWidget(QWidget())  # 用于占位的小部件
        layout.addWidget(QWidget())  # 用于占位的小部件

        # 将布局设置为子窗口的布局
        self.setLayout(layout)

class SubWindow2(QDialog):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 200, 10, 10)
        # 设置子窗口的背景颜色
        self.setStyleSheet("background-color: lightgreen;")
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

class SubWindow3(QDialog):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 200, 10, 10)
        # 设置子窗口的背景颜色
        self.setStyleSheet("background-color: lightblue;")
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

class SubWindow4(QDialog):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 200, 10, 10)
        # 设置子窗口的背景颜色
        self.setStyleSheet("background-color: lightgreen;")
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
        self.setGeometry(300, 200, 1000, 800)
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
        button1.setStyleSheet("background-color: gray; color: white;")
        button_layout.addWidget(button1)


        button2 = QPushButton("Flow Observation")
        button2.setFixedSize(300, 50)  # 设置按钮2的尺寸
        button2.clicked.connect(self.open_window2)
        button2.setStyleSheet("background-color: gray; color: white;")
        button_layout.addWidget(button2)

        button3 = QPushButton("Liquid Level Observation")
        button3.setFixedSize(300, 50)  # 设置按钮3的尺寸
        button3.clicked.connect(self.open_window3)
        button3.setStyleSheet("background-color: gray; color: white;")
        button_layout.addWidget(button3)

        button4 = QPushButton("PID Speed Debugging")
        button4.setFixedSize(300, 50)  # 设置按钮4的尺寸
        button4.clicked.connect(self.open_window4)
        button4.setStyleSheet("background-color: gray; color: white;")
        button_layout.addWidget(button4)


        # 添加水平布局到垂直布局
        main_layout.addLayout(button_layout)

        # # 创建一个伸展因子，将按钮推到窗口的顶部
        # spacer = QSpacerItem(1, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        # main_layout.addItem(spacer)

        # 设置主窗口容器的布局为垂直布局
        main_widget.setLayout(main_layout)

        # 设置主窗口的背景颜色
        self.setStyleSheet("background-color: lightblack;")

        # 创建一个堆叠窗口，用于显示子窗口
        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)

    def open_window1(self):
        sub_window1 = SubWindow1()
        self.stacked_widget.addWidget(sub_window1)
        self.stacked_widget.setCurrentWidget(sub_window1)
        self.setWindowTitle("General Control Interface")

    def open_window2(self):
        sub_window2 = SubWindow2()
        self.stacked_widget.addWidget(sub_window2)
        self.stacked_widget.setCurrentWidget(sub_window2)
        self.setWindowTitle("Flow Observation")


    def open_window3(self):
        sub_window3 = SubWindow3()
        self.stacked_widget.addWidget(sub_window3)
        self.stacked_widget.setCurrentWidget(sub_window3)
        self.setWindowTitle("Liquid Level Observation")

    def open_window4(self):
        sub_window4 = SubWindow4()
        self.stacked_widget.addWidget(sub_window4)
        self.stacked_widget.setCurrentWidget(sub_window4)
        self.setWindowTitle("PID Speed Debugging")










