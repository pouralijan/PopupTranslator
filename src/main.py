#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication

from Gui import App

if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen_resolution = app.desktop().screenGeometry()
    exce = App(screen_resolution)
    exce.show()
    sys.exit(app.exec_())
