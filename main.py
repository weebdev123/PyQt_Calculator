import sys
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QWidget, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.calculation_bar = QLineEdit()
        self.calculation_bar.setFixedHeight(60)  # make the bar taller
        self.calculation_bar.setFont(QFont("Arial", 20))  # larger font size
        # Button labels arranged like a calculator
        buttons = [
            [".", "C", "⌫", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", "(", ")", "="]
        ]

        # Main layout
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.calculation_bar)

        # Grid layout for buttons
        grid = QGridLayout()

        for row, row_values in enumerate(buttons):
            for col, text in enumerate(row_values):
                btn = QPushButton(text)
                btn.setFixedSize(70, 70)
                btn.setFont(QFont("Arial", 16))
                grid.addWidget(btn, row, col)

                # Connect signals
                if text == "=":
                    btn.clicked.connect(self.on_click_equal)
                elif text == "C":
                    btn.clicked.connect(self.on_clear)
                elif text == "⌫":
                    btn.clicked.connect(self.on_backspace)
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
        """Evaluate the expression safely"""
        expr = self.calculation_bar.text()

        # Allow only numbers, operators, parentheses, and dot
        if not re.fullmatch(r"[0-9+\-*/(). ]*", expr):
            self.calculation_bar.setText("Error")
            return

        try:
            result = str(eval(expr, {"__builtins__": None}, {}))
            self.calculation_bar.setText(result)
        except Exception:
            self.calculation_bar.setText("Error")

    def on_clear(self):
        """Clear the entire display"""
        self.calculation_bar.clear()

    def on_backspace(self):
        """Delete the last character"""
        current = self.calculation_bar.text()
        self.calculation_bar.setText(current[:-1])

    def keyPressEvent(self, event):
        """Handle keyboard input"""
        key = event.key()

        if key == Qt.Key_Return or key == Qt.Key_Enter:
            self.on_click_equal()
        elif key == Qt.Key_Backspace:
            self.on_backspace()
        elif key == Qt.Key_Escape:
            self.on_clear()
        else:
            text = event.text()
            if text in "0123456789+-*/().":
                self._append(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(300, 300)
    window.show()
    sys.exit(app.exec_())
