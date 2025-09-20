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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
