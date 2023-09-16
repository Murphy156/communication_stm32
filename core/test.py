import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QFrame, QLabel

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个实线框
        frame = QFrame(self)
        frame.setFrameShape(QFrame.Shape.Box)
        frame.setLineWidth(2)

        # 创建一个 QWidget 作为实线框的子控件
        widget_inside_frame = QWidget(frame)

        # 创建一个垂直布局，并设置给这个 QWidget
        vbox = QVBoxLayout(widget_inside_frame)
        vbox.addWidget(QLabel("Label 1"))
        vbox.addWidget(QLabel("Label 2"))

        # 将这个 QWidget 添加到实线框中
        frame_layout = QVBoxLayout()
        frame_layout.addWidget(widget_inside_frame)
        frame.setLayout(frame_layout)

        # 创建一个垂直布局，将实线框放置在主窗口中
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(frame)

        self.setWindowTitle('Frame Example')
        self.setGeometry(100, 100, 300, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
