from PySide2.QtCore import QUrl
from PySide2.QtWidgets import QApplication
from PySide2.QtWebEngineWidgets import QWebEngineView

class Browser(QWebEngineView):
    def __init__(self, windows):
        self.view = QWebEngineView.__init__(self)
        self._window = windows
        QApplication.clipboard().dataChanged.connect(self.clipboard_changed)

    def clipboard_changed(self):
        url = "https://translate.google.com/m/translate#auto/fa/{}".format(QApplication.clipboard().text())
        self.load(QUrl(url))

    def load(self, url):
        self.setUrl(QUrl(url))
        self._window.setVisible(True)
