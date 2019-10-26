#!/usr/bin/env python3
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)

web = QWebEngineView()

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "html/app.html"))
local_url = QUrl.fromLocalFile(file_path)
web.load(local_url)
# web.setHtml(html, QUrl("qrc:/"))
# web.load(QUrl.fromLocalFile('app.html'))
# web.load(QUrl("url")) 'app.html'
web.show()

sys.exit(app.exec_())