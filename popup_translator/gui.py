#!/usr/bin/env python3

import os

try:
    from PySide2 import QtCore
    from PySide2.QtGui import QGuiApplication, QIcon
    from PySide2.QtCore import Slot
    from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton, QMenu, QAction, QTabWidget
    from PySide2.QtWidgets import QSystemTrayIcon, QGridLayout
except ImportError as error:
    raise SystemExit(error)

from .browser import PopupBrowser


class SystemTrayIconActions(object):
    def __init__(self, widget):
        self._actions_list = []
        self.Quit = QAction("&Quit", widget, triggered=QGuiApplication.quit)

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

        google_url = "https://translate.google.com/m/translate#auto/{}/{}"
        popup_browser_google = PopupBrowser(self, google_url, "en", "Google")

        cambridge_url = "https://dictionary.cambridge.org/dictionary/{}/{}"
        popup_browser_cambridge = PopupBrowser(self, cambridge_url, "english", "Cambridge")

        collins_url = "https://www.collinsdictionary.com/dictionary/{}/{}"
        popup_browser_collins = PopupBrowser(self, collins_url, "english", "Collins")

        oxford_url = "https://www.oxfordlearnersdictionaries.com/definition/{}/{}"
        popup_browser_oxford = PopupBrowser(self, oxford_url, "english", "Oxford")

        dictionaries = []
        dictionaries.append(popup_browser_google)
        dictionaries.append(popup_browser_cambridge)
        dictionaries.append(popup_browser_collins)
        dictionaries.append(popup_browser_oxford)

        layout = QGridLayout()
        self.setLayout(layout)
        tabwidget = QTabWidget()

        
        for dictionary in dictionaries:
            tabwidget.addTab(dictionary, dictionary.name)

        layout.addWidget(tabwidget, 0, 0)
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
