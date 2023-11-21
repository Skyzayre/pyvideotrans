# set baidu appid and secrot
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog

from videotrans.ui.baidu import Ui_baiduform
from videotrans.ui.chatgpt import Ui_chatgptform
from videotrans.ui.deepl import Ui_deeplform
from videotrans.ui.deeplx import Ui_deeplxform
from videotrans.ui.tencent import Ui_tencentform


class BaiduForm(QDialog, Ui_baiduform):  # <===
    def __init__(self, parent=None):
        super(BaiduForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon("./icon.ico"))

class TencentForm(QDialog, Ui_tencentform):  # <===
    def __init__(self, parent=None):
        super(TencentForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon("./icon.ico"))


class DeepLForm(QDialog, Ui_deeplform):  # <===
    def __init__(self, parent=None):
        super(DeepLForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon("./icon.ico"))


class DeepLXForm(QDialog, Ui_deeplxform):  # <===
    def __init__(self, parent=None):
        super(DeepLXForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon("./icon.ico"))


# set chatgpt api and key
class ChatgptForm(QDialog, Ui_chatgptform):  # <===
    def __init__(self, parent=None):
        super(ChatgptForm, self).__init__(parent)
        self.setupUi(self)
        self.chatgpt_model.addItems(["gpt-3.5-turbo", "gpt-4-turbo", "gpt-4"])
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon("./icon.ico"))
