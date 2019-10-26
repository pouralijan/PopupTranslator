#!/usr/bin/env python3

import os

from PySide2 import QtCore
from PySide2.QtGui import qApp, QIcon
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton, QMenu, QAction
from PySide2.QtWidgets import QSystemTrayIcon

import PopupTranslator


class SystemTrayIconActions(object):
    def __init__(self, widget):
        self._actions_list = []
        self.Quit = QAction("&Quit", widget, triggered=qApp.quit)

        self._actions_list.append(self.Quit)

    def get_actions(self):
        return self._actions_list


class SystemTrayIconMenu(object):
    def __init__(self, actions: SystemTrayIconActions, widget):
        self.tray_icon_menu = QMenu(widget)

        for action in actions:
            self.tray_icon_menu.addAction(action)

        self.tray_icon = QSystemTrayIcon(widget)

        self.tray_icon.setContextMenu(self.tray_icon_menu)


class PopupTranslatorWidget(QWidget):
    DATA_LOCATION = "/usr/share/PopupTranslator/"
    def __init__(self, screen_resolution) -> None:
        super().__init__()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.title = "PopupTranslator"
        self.width = screen_resolution.width() * 20 / 100
        self.height = screen_resolution.height() * 60 / 100
        self.left = screen_resolution.width() - self.width
        self.top = 0

        self._source_language = ""
        self._des_language = "fa"

        self.icon = QIcon(os.path.join(self.DATA_LOCATION, "./icon.png"))

        system_tray_icon_action = SystemTrayIconActions(self)
        system_tray_icon_menu = SystemTrayIconMenu(
                system_tray_icon_action.get_actions(), self)
        system_tray_icon_menu.tray_icon.setIcon(self.icon)
        system_tray_icon_menu.tray_icon.show()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(self.icon)
        self.setGeometry(self.left, self.top, self.width, self.height)
        popup_browser = PopupTranslator.PopupBrowser(self)
        popup_browser.load(
                "https://translate.google.com/m/translate#auto/{}/".format(
                    self.get_des_language()))
        layout = QVBoxLayout(self)
        layout.addWidget(popup_browser)
        button = QPushButton("Hide")
        button.clicked.connect(self.hide)
        layout.addWidget(button)
        self.show()

    def get_des_language(self):
        return self._des_language

    def set_des_language(self, language):
        self._des_language = language

    @Slot()
    def hide(self):
        self.setVisible(False)
