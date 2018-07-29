from PyQt5.QtCore import QUrl
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtWebKitWidgets import QWebPage, QWebView
from PyQt5.QtWidgets import QApplication


class Browser(QWebView):
    def __init__(self, windows):
        self.view = QWebView.__init__(self)
        self._window = windows
        QApplication.clipboard().dataChanged.connect(self.clipboard_changed)

    def clipboard_changed(self):
        url = "https://translate.google.com/m/translate#auto/fa/{}".format(QApplication.clipboard().text())
        self.load(QUrl(url))

    def load(self, url):
        self.setUrl(QUrl(url))
        self._window.setVisible(True)

    @staticmethod
    def disable_js():
        settings = QWebSettings.globalSettings()
        settings.setAttribute(QWebSettings.JavascriptEnabled, False)
