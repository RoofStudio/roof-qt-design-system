import os

from PySide6.QtWidgets import QApplication
import sys
from RoofDesignSystem.layouts.mainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(
        width=500,
        height=500,
        title="Roof Environment Installer",
    )

    window.show()
    sys.exit(app.exec())
