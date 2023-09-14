import sys
from PyQt6.QtWidgets import *

class SubWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("子窗口")
        self.setGeometry(200, 200, 400, 200)

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

        self.setWindowTitle("主窗口")
        self.setGeometry(100, 100, 400, 200)

        # 创建一个主界面容器
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # 创建垂直布局
        main_layout = QVBoxLayout()

        # 创建按钮布局
        button_layout = QVBoxLayout()

        # 创建四个按钮
        button1 = QPushButton("窗口1")
        button1.clicked.connect(self.show_sub_window)

        button2 = QPushButton("窗口2")
        button3 = QPushButton("窗口3")
        button4 = QPushButton("窗口4")

        # 将按钮添加到按钮布局中
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        button_layout.addWidget(button3)
        button_layout.addWidget(button4)

        # 添加按钮布局到主布局
        main_layout.addLayout(button_layout)

        # 设置主窗口容器的布局
        main_widget.setLayout(main_layout)

        # 创建一个堆叠窗口，用于显示子窗口
        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)

    def show_sub_window(self):
        sub_window = SubWindow()
        self.stacked_widget.addWidget(sub_window)
        self.stacked_widget.setCurrentWidget(sub_window)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())