import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QWidget, QVBoxLayout, QGridLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.calculation_bar = QLineEdit()

        # Button labels arranged like a calculator
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"]
        ]

        # Main layout
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.calculation_bar)

        # Grid layout for buttons
        grid = QGridLayout()

        for row, row_values in enumerate(buttons):
            for col, text in enumerate(row_values):
                btn = QPushButton(text)
                btn.setFixedSize(50, 50)  # make it look neat
                grid.addWidget(btn, row, col)

                if text == "=":
                    btn.clicked.connect(self.on_click_equal)
                else:
                    btn.clicked.connect(lambda _, t=text: self._append(t))

        self.main_layout.addLayout(grid)

        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

    def _append(self, text):
        """Append character to the display"""
        current = self.calculation_bar.text()
        self.calculation_bar.setText(current + text)

    def on_click_equal(self):
        """Evaluate the expression"""
        try:
            result = str(eval(self.calculation_bar.text()))
            self.calculation_bar.setText(result)
        except Exception:
            self.calculation_bar.setText("Error")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(300, 300)
    window.show()
    sys.exit(app.exec_())
