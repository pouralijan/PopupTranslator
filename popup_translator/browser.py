#!/usr/bin/env python3

from PySide2.QtCore import QUrl
from PySide2.QtWidgets import QApplication
from PySide2.QtWebEngineWidgets import QWebEngineView


class PopupBrowser(QWebEngineView):
    def __init__(self, windows, url, des_language, name):
        self.view = QWebEngineView.__init__(self)
        self._window = windows
        self.url = url
        self.name = name
        self.des_language = des_language
        QApplication.clipboard().dataChanged.connect(self.clipboard_changed)

    def clipboard_changed(self):
        url = self.url.format(self.des_language, QApplication.clipboard().text())
        self.load(QUrl(url))

    def load(self, url):
        self.setUrl(QUrl(url))
        self._window.setVisible(True)
