# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form1RfKnkR.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(300, 200)
        self.pushButton1 = QPushButton(Dialog)
        self.pushButton1.setObjectName(u"pushButton1")
        self.pushButton1.setGeometry(QRect(100, 70, 80, 25))
        self.pushButton2 = QPushButton(Dialog)
        self.pushButton2.setObjectName(u"pushButton2")
        self.pushButton2.setGeometry(QRect(100, 100, 80, 25))

        self.retranslateUi(Dialog)
        self.pushButton1.clicked.connect(Dialog.pushButton1Click)
        self.pushButton2.clicked.connect(Dialog.pushButton2Click)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton1.setText(QCoreApplication.translate("Dialog", u"Say Hello", None))
        self.pushButton2.setText(QCoreApplication.translate("Dialog", u"Quit", None))
    # retranslateUi

