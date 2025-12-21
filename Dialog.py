
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QWidget, QMessageBox)
from ui_Dialog import Ui_Dialog

class Dialog(QDialog):

    def __init__(self):
        super(Dialog,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
    
    def pushButton1Click(self):
        QMessageBox.information(self, "Hello", "Hello, World!!!")

    def pushButton2Click(self):
        QApplication.quit()
        