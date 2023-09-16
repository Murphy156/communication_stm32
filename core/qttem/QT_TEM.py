import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget

from PyQt6.QtGui import *

class SubWindow1(QDialog):
    def __init__(self):
        super().__init__()

        # 创建一个子界面容器
        sub_widget = QWidget()

        # 设置子窗口的背景颜色
        self.setStyleSheet("background-color: lightblue;")

        # 创建子界面的主水平布局
        MainLayout = QHBoxLayout()

        sub_widget.setLayout(MainLayout)

        # 创建控制框的垂直布局
        ControlLayout = QVBoxLayout()

        MainLayout.addLayout(ControlLayout)

        lable1 = QLabel("Serial Port Configuration")
        ControlLayout.addWidget(lable1)

#####################
        # 串口布局安排
        PortLayout = QHBoxLayout()

        lable2 = QLabel("port")
        PortLayout.addWidget(lable2)

        # 串口的下拉选框
        COM = QComboBox(self)
        COM.addItem('COM1')
        COM.addItem('COM2')
        COM.addItem('COM3')
        COM.addItem('COM4')
        COM.addItem('COM5')
        COM.addItem('COM6')
        COM.setMinimumWidth(80)
        COM.setMaximumWidth(80)
        PortLayout.addWidget(COM)

        # 将PortLayout放在ControlLayout
        ControlLayout.addLayout(PortLayout)

#####################




        # 创建串口框架
        SerFrame = QFrame()
        SerFrame.setFrameShape(QFrame.Shape.Box)
        SerFrame.setFrameShadow(QFrame.Shadow.Raised)
        SerFrame.setLineWidth(1)
        SerFrame.setStyleSheet("background-color: orange;")
        SerFrame.setFixedSize(200, 150)
        ControlLayout.addWidget(SerFrame)

        # 创建控制框架
        ConFrame = QFrame()
        ConFrame.setFrameShape(QFrame.Shape.Box)
        ConFrame.setFrameShadow(QFrame.Shadow.Raised)
        ConFrame.setLineWidth(1)
        ConFrame.setStyleSheet("background-color: red;")
        ConFrame.setFixedSize(200, 525)
        ControlLayout.addWidget(ConFrame)

        # 创建显示框架
        Dis_Frame = QFrame()
        Dis_Frame.setFrameShape(QFrame.Shape.Box)
        Dis_Frame.setFrameShadow(QFrame.Shadow.Raised)
        Dis_Frame.setLineWidth(1)
        Dis_Frame.setStyleSheet("background-color: green;")
#        Dis_Frame.setFixedSize(Dis_Frame_width,Dis_Frame_height)

        # 现将控制端放在左边
        MainLayout.addWidget(Dis_Frame)
        self.setLayout(MainLayout)

        # # 将布局设置为子窗口的布局
        # self.setLayout(layout)

class SubWindow2(QDialog):
    def __init__(self):
        super().__init__()

        self.setFixedSize(300, 200)
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

        # 设置主窗口容器的布局为垂直布局
        main_widget.setLayout(main_layout)

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

        # 设置主窗口的背景颜色
        self.setStyleSheet("background-color: lightblack;")

        # 创建一个堆叠窗口，用于显示子窗口
        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)

    def open_window1(self):
        sub_window1 = SubWindow1()
        # # 创建子界面的主水平布局
        # MainLayout = QWidget()
        # MainLayout.setLayout(QHBoxLayout())
        # MainLayout.layout().addLayout(sub_window1.layout())
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









