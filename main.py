import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QMessageBox, QVBoxLayout, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.calculation_bar = QLineEdit()
        self.btn_7 = QPushButton("7")
        self.btn_8 = QPushButton("8")
        self.btn_9 = QPushButton("9")
        self.btn_div = QPushButton("/")

        self.btn_4 = QPushButton("4")
        self.btn_5 = QPushButton("5")
        self.btn_6 = QPushButton("6")
        self.btn_mul = QPushButton("*")

        self.btn_1 = QPushButton("1")
        self.btn_2 = QPushButton("2")
        self.btn_3 = QPushButton("3")
        self.btn_sub = QPushButton("-")

        self.btn_equal = QPushButton("=")
        self.btn_0 = QPushButton("0")
        self.btn_dot = QPushButton(".")
        self.btn_add = QPushButton("+")

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.calculation_bar)

        self.btn_layout1 = QHBoxLayout()
        self.btn_layout1.addWidget(self.btn_7)
        self.btn_layout1.addWidget(self.btn_8)
        self.btn_layout1.addWidget(self.btn_9)
        self.btn_layout1.addWidget(self.btn_div)

        self.btn_layout2 = QHBoxLayout()
        self.btn_layout2.addWidget(self.btn_4)
        self.btn_layout2.addWidget(self.btn_5)
        self.btn_layout2.addWidget(self.btn_6)
        self.btn_layout2.addWidget(self.btn_mul)

        self.btn_layout3 = QHBoxLayout()
        self.btn_layout3.addWidget(self.btn_1)
        self.btn_layout3.addWidget(self.btn_2)
        self.btn_layout3.addWidget(self.btn_3)
        self.btn_layout3.addWidget(self.btn_sub)

        self.btn_layout4 = QHBoxLayout()
        self.btn_layout4.addWidget(self.btn_equal)
        self.btn_layout4.addWidget(self.btn_0)
        self.btn_layout4.addWidget(self.btn_dot)
        self.btn_layout4.addWidget(self.btn_add)

        self.main_layout.addLayout(self.btn_layout1)
        self.main_layout.addLayout(self.btn_layout2)
        self.main_layout.addLayout(self.btn_layout3)
        self.main_layout.addLayout(self.btn_layout4)

        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

        # Digits
        self.btn_7.clicked.connect(self.on_click_7)
        self.btn_8.clicked.connect(self.on_click_8)
        self.btn_9.clicked.connect(self.on_click_9)
        self.btn_4.clicked.connect(self.on_click_4)
        self.btn_5.clicked.connect(self.on_click_5)
        self.btn_6.clicked.connect(self.on_click_6)
        self.btn_1.clicked.connect(self.on_click_1)
        self.btn_2.clicked.connect(self.on_click_2)
        self.btn_3.clicked.connect(self.on_click_3)
        self.btn_0.clicked.connect(self.on_click_0)

        # Operators
        self.btn_div.clicked.connect(self.on_click_div)
        self.btn_mul.clicked.connect(self.on_click_mul)
        self.btn_sub.clicked.connect(self.on_click_sub)
        self.btn_add.clicked.connect(self.on_click_add)
        self.btn_dot.clicked.connect(self.on_click_dot)

        # Equal
        self.btn_equal.clicked.connect(self.on_click_equal)

    def on_click_7(self):
        current = self.calculation_bar.text()
        self.calculation_bar.setText(current + "7")

    def on_click_8(self):
        current = self.calculation_bar.text()
        self.calculation_bar.setText(current + "8")

    def on_click_9(self):
        current = self.calculation_bar.text()
        self.calculation_bar.setText(current + "9")

    def on_click_div(self):
        current = self.calculation_bar.text()
        self.calculation_bar.setText(current + "/")

    def on_click_4(self):
        current = self.calculation_bar.text()
        self.calculation_bar.setText(current + "4")

    def on_click_5(self):
        current = self.calculation_bar.text()
        self.calculation_bar.setText(current + "5")

    def on_click_6(self):
        current = self.calculation_bar.text()
        self.calculation_bar.setText(current + "6")

    def on_click_mul(self):
        current = self.calculation_bar.text()
        self.calculation_bar.setText(current + "*")

    def on_click_1(self):
        current = self.calculation_bar.text()
        self.calculation_bar.setText(current + "1")

    def on_click_2(self):
        current = self.calculation_bar.text()
        self.calculation_bar.setText(current + "2")

    def on_click_3(self):
        current = self.calculation_bar.text()
        self.calculation_bar.setText(current + "3")

    def on_click_sub(self):
        current = self.calculation_bar.text()
        self.calculation_bar.setText(current + "-")

    def on_click_equal(self):
        try:
            expression = self.calculation_bar.text()
            result = str(eval(expression))  # careful with eval for user input!
            self.calculation_bar.setText(result)
        except Exception:
            self.calculation_bar.setText("Error")

    def on_click_0(self):
        current = self.calculation_bar.text()
        self.calculation_bar.setText(current + "0")

    def on_click_dot(self):
        current = self.calculation_bar.text()
        self.calculation_bar.setText(current + ".")

    def on_click_add(self):
        current = self.calculation_bar.text()
        self.calculation_bar.setText(current + "+")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
