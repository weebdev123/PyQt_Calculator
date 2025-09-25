# calculator/main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QWidget, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from calculator import CalculatorLogic   # <--- cleaner import


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.logic = CalculatorLogic()
        self.setWindowTitle("PyQt Calculator")

        self.calculation_bar = QLineEdit()
        self.calculation_bar.setFixedHeight(60)
        self.calculation_bar.setFont(QFont("Arial", 20))
        self.calculation_bar.setFocus()

        buttons = [
            [".", "C", "⌫", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", "(", ")", "="]
        ]

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.calculation_bar)

        grid = QGridLayout()
        for row, row_values in enumerate(buttons):
            for col, text in enumerate(row_values):
                btn = QPushButton(text)
                btn.setFixedSize(70, 70)
                btn.setFont(QFont("Arial", 16))
                btn.setFocusPolicy(Qt.NoFocus)
                grid.addWidget(btn, row, col)
                btn.clicked.connect(lambda _, t=text: self.on_button_click(t))

        self.main_layout.addLayout(grid)

        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

    def on_button_click(self, text: str):
        current = self.calculation_bar.text()
        if text == "=":
            self.calculation_bar.setText(self.logic.evaluate_expression(current))
        elif text == "C":
            self.calculation_bar.setText(self.logic.clear())
        elif text == "⌫":
            self.calculation_bar.setText(self.logic.backspace(current))
        else:
            self.calculation_bar.setText(self.logic.append(current, text))

    def keyPressEvent(self, event):
        key = event.key()
        current = self.calculation_bar.text()
        if key in (Qt.Key_Return, Qt.Key_Enter):
            self.calculation_bar.setText(self.logic.evaluate_expression(current))
        elif key == Qt.Key_Backspace:
            self.calculation_bar.setText(self.logic.backspace(current))
        elif key == Qt.Key_Escape:
            self.calculation_bar.setText(self.logic.clear())
        else:
            text = event.text()
            if text in "0123456789+-*/().":
                self.calculation_bar.setText(self.logic.append(current, text))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(300, 300)
    window.show()
    sys.exit(app.exec_())
