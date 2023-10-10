import sys
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QFrame, QLabel, QPushButton, QLineEdit

class SubWindow2(QDialog):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-color: white;")

        Controlseparator = QFrame(self)
        Controlseparator.setStyleSheet("background-color: green;")
        Controlseparator.setFrameShape(QFrame.Shape.Box)
        Controlseparator.setFrameShadow(QFrame.Shadow.Sunken)
        Controlseparator.setFixedSize(200, 700)

        # 创建第一个垂直布局框架
        frame1 = QFrame(Controlseparator)
        frame1_layout = QVBoxLayout(frame1)
        frame1_label = QLabel('Frame 1:', frame1)
        frame1_button = QPushButton('Button 1', frame1)
        frame1_layout.addWidget(frame1_label)
        frame1_layout.addWidget(frame1_button)

        # 创建第二个垂直布局框架
        frame2 = QFrame(Controlseparator)
        frame2_layout = QVBoxLayout(frame2)
        frame2_label = QLabel('Frame 2:', frame2)
        frame2_button = QPushButton('Button 2', frame2)
        frame2_layout.addWidget(frame2_label)
        frame2_layout.addWidget(frame2_button)

        # 创建垂直布局并将两个框架添加到布局中
        ControlLayout = QVBoxLayout(Controlseparator)
        ControlLayout.addWidget(frame1)
        ControlLayout.addWidget(frame2)

        Showseparator = QFrame(self)
        Showseparator.setStyleSheet("background-color: blue;")
        Showseparator.setFrameShape(QFrame.Shape.Box)
        Showseparator.setFrameShadow(QFrame.Shadow.Sunken)
        Showseparator.setFixedSize(900, 700)

        # 创建一些控件放入Showseparator
        show_label = QLabel('Display:', Showseparator)
        show_button = QPushButton('Display Button', Showseparator)
        show_input = QLineEdit(Showseparator)

        ShowLayout = QVBoxLayout(Showseparator)
        ShowLayout.addWidget(show_label)
        ShowLayout.addWidget(show_button)
        ShowLayout.addWidget(show_input)

        Sub2Mainlayout = QHBoxLayout()
        Sub2Mainlayout.addWidget(Showseparator)
        Sub2Mainlayout.addWidget(Controlseparator)

        self.setLayout(Sub2Mainlayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sub_window = SubWindow2()
    sub_window.show()
    sys.exit(app.exec())
