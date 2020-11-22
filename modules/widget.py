from PyQt5 import QtCore, QtGui, QtWidgets
from modules.mylable import MyLabel


class Widget (QtWidgets, QtWidgets):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
