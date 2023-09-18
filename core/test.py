import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, Qt
from PyQt6.QtGui import QColor

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.button = QPushButton('Click me', self)
        self.button.setStyleSheet('background-color: green')
        self.button.clicked.connect(self.onButtonClick)

        layout.addWidget(self.button)
        self.setLayout(layout)

    def onButtonClick(self):
        # Get the original button color
        original_color = self.button.palette().button().color()

        # Create a property animation for background color
        animation = QPropertyAnimation(self.button, b'backgroundColor')
        animation.setDuration(500)  # Animation duration in milliseconds
        animation.setStartValue(original_color)
        animation.setEndValue(QColor('red'))
        animation.setEasingCurve(QEasingCurve.Type.OutQuad)

        # Connect the finished signal to restore the original color
        animation.finished.connect(lambda: self.button.setStyleSheet(f'background-color: {original_color.name()}'))

        # Start the animation
        animation.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
