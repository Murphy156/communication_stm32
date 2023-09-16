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

        # 创建串口和波特率的选择
        self.selected_port = None
        self.selected_baud = None

        # 设置子窗口的背景颜色
        self.setStyleSheet("background-color: lightblue;")

        # 创建子界面的主水平布局
        MainLayout = QHBoxLayout()

        sub_widget.setLayout(MainLayout)

        # 创建控制框的垂直布局
        ControlLayout = QVBoxLayout()

        # 将控制框的界面放入到主框的左边
        MainLayout.addLayout(ControlLayout)

        # 创建控制框中的串口设置垂直分布布局
        ContSeriLayout = QVBoxLayout()

        # 将串口设置布局放入控制框中的垂直分布中
        ControlLayout.addLayout(ContSeriLayout)

        # 创建控制框中的电机控制面板设置的垂直分布
        ContMotCLayout = QVBoxLayout()

        # 将电机控制面板设置放入控制框中的垂直分布
        ControlLayout.addLayout(ContMotCLayout)

        # program start 这里是设置串口设置的布局
        lable1 = QLabel("Serial Port Configuration")
        lable1.setFixedSize(200, 20)

        # 创建一个字体对象
        font1 = QFont()
        font1.setPointSize(15)  # 设置字体大小
        font1.setBold(True)  # 设置为粗体
        lable1.setFont(font1)
        # 将第一个文本框放在串口设置布局中
        ContSeriLayout.addWidget(lable1)

        # 串口布局安排
        PortLayout = QHBoxLayout()
        lable2 = QLabel("Port")

        font2 = QFont()
        font2.setPointSize(13)  # 设置字体大小
        font2.setBold(True)  # 设置为粗体
        lable2.setFont(font2)

        PortLayout.addWidget(lable2)

        # 串口的下拉选框
        COM = QComboBox(self)
        COM.addItem('COM1')
        COM.addItem('COM2')
        COM.addItem('COM3')
        COM.addItem('COM4')
        COM.addItem('COM5')
        COM.addItem('COM6')
        COM.setMinimumWidth(90)
        COM.setMaximumWidth(90)
        PortLayout.addWidget(COM)
        # 将COM和BAUD作为类的成员变量
        self.COM = COM

        # 将PortLayout放在ControlLayout
        ContSeriLayout.addLayout(PortLayout)

        # 波特率布局安排
        BaudLayout = QHBoxLayout()
        lable3 = QLabel("Baudrate")

        lable3.setFont(font2)

        BaudLayout.addWidget(lable3)

        # 串口的下拉选框
        BAUD = QComboBox(self)
        BAUD.addItem('2400', 2400)
        BAUD.addItem('4800', 4800)
        BAUD.addItem('9600', 9600)
        BAUD.addItem('19200', 19200)
        BAUD.addItem('38400', 38400)
        BAUD.addItem('57600', 57600)
        BAUD.addItem('115200', 115200)
        BAUD.addItem('128000', 128000)
        BAUD.addItem('230400', 230400)
        BAUD.addItem('256000', 256000)
        BAUD.setMinimumWidth(90)
        BAUD.setMaximumWidth(90)
        BaudLayout.addWidget(BAUD)
        # 将COM和BAUD作为类的成员变量
        self.BAUD = BAUD
        # BaudLayout
        ContSeriLayout.addLayout(BaudLayout)

        CommunicationLayout = QHBoxLayout()
        self.indicatior = QLabel()
        self.indicatior.setFixedSize(20, 20)
        self.indicatior.setStyleSheet("background-color: gray; border-radius: 10px;")
        CommunicationLayout.addWidget(self.indicatior)

        post_com_button = QPushButton("Open Serial")
        post_com_button.setFixedSize(80, 20)  # 设置按钮1的尺寸
        post_com_button.clicked.connect(self.post_com_function)
        CommunicationLayout.addWidget(post_com_button)

        ContSeriLayout.addLayout(CommunicationLayout)
        # program end

        ##program2 start 这里是创建电机控制面板模块的
        lable4 = QLabel("Serial Port Configuration")
        lable4.setFixedSize(200, 20)

        lable4.setFont(font1)
        # 将第一个文本框放在串口设置布局中
        ContMotCLayout.addWidget(lable4)

        ##program2 end

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

    def post_com_function(self):
        self.selected_port = self.COM.currentText()
        self.selected_baud = int(self.BAUD.currentText())
        if self.indicatior.styleSheet() == "background-color: gray; border-radius: 10px;":
            self.indicatior.setStyleSheet("background-color: green; border-radius: 10px;")
            self.COM.setDisabled(True)
            self.BAUD.setDisabled(True)
        else:
            self.indicatior.setStyleSheet("background-color: gray; border-radius: 10px;")
            self.COM.setEnabled(True)
            self.BAUD.setEnabled(True)
        print("Selected port:", self.selected_port)
        print("Selected baud rate:", self.selected_baud)


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









