from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

from Browser import Browser


class App(QWidget):
    def __init__(self, screen_resolution) -> None:
        super().__init__()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.title = "PopupTranslator"
        self.width = screen_resolution.width() * 20 / 100
        self.height = screen_resolution.height() * 60 / 100
        self.left = screen_resolution.width() - self.width
        self.top = 0
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        beowser = Browser(self)
        beowser.load("https://translate.google.com/m/translate#auto/fa/")
        layout = QVBoxLayout(self)
        layout.addWidget(beowser)

        button = QPushButton("Hide")
        button.clicked.connect(self.hide)
        layout.addWidget(button)
        self.show()

    @pyqtSlot()
    def hide(self):
        self.setVisible(False)
