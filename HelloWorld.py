import sys
from PySide6.QtWidgets import QApplication
from Dialog import Dialog

if(__name__ == "__main__"):
    app = QApplication()
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec())