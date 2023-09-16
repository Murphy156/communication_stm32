import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox

class CheckBoxExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Checkbox Example')
        self.setGeometry(300, 300, 300, 200)

        vbox = QVBoxLayout()

        # Create checkboxes
        checkbox1 = QCheckBox('Option 1', self)
        checkbox2 = QCheckBox('Option 2', self)
        checkbox3 = QCheckBox('Option 3', self)

        # Connect the stateChanged signal to a slot
        checkbox1.stateChanged.connect(self.checkbox_state_changed)
        checkbox2.stateChanged.connect(self.checkbox_state_changed)
        checkbox3.stateChanged.connect(self.checkbox_state_changed)

        # Add checkboxes to the vertical layout
        vbox.addWidget(checkbox1)
        vbox.addWidget(checkbox2)
        vbox.addWidget(checkbox3)

        self.setLayout(vbox)
        self.show()

    def checkbox_state_changed(self, state):
        sender = self.sender()  # Get the checkbox that triggered the signal

        if state == 2:  # 2 means checked, 0 means unchecked
            print(f'Checkbox {sender.text()} is checked')
        else:
            print(f'Checkbox {sender.text()} is unchecked')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CheckBoxExample()
    sys.exit(app.exec())
