import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSpacerItem, QSizePolicy

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

        # 创建按钮1
        button1 = QPushButton("按钮1")

        # 创建一个垂直的伸展因子，将按钮1推到顶部
        spacer1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        # 创建按钮2
        button2 = QPushButton("按钮2")

        # 创建水平的伸展因子，将按钮2推到底部
        spacer2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        # 将控件和伸展因子添加到布局中
        main_layout.addItem(spacer1)
        main_layout.addWidget(button1)
        main_layout.addItem(spacer2)
        main_layout.addWidget(button2)

        # 设置主窗口容器的布局
        main_widget.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
