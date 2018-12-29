#!/usr/bin/env python3
import sys
from PySide2.QtWidgets import QApplication

from Gui import PopupTranslator

if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen_resolution = app.desktop().screenGeometry()
    exce = PopupTranslator(screen_resolution)
    exce.show()
    sys.exit(app.exec_())
