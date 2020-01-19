#!/usr/bin/env python3
import sys
from PySide2.QtWidgets import QApplication

from PopupTranslator import PopupTranslatorWidget

def main():
    app = QApplication(sys.argv)
    screen_resolution = app.desktop().screenGeometry()
    exce = PopupTranslatorWidget(screen_resolution)
    exce.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    print("Main")
    #main()
