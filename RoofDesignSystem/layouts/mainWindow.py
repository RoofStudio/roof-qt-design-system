from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QStackedWidget, QMainWindow, QWidget

from RoofDesignSystem.styles import get_stylesheet


class MainWindow(QMainWindow):
    def __init__(
        self, parent=None, width=300, height=300, title="Main Window", icon_path=None
    ):
        super().__init__(parent)

        if icon_path:
            self.setWindowIcon(QIcon(icon_path))

        self.setWindowTitle(title)

        self.setMinimumWidth(width)
        self.setMinimumHeight(height)
        self.setWindowFlags(self.windowFlags() ^ Qt.WindowMinimizeButtonHint)
        self.setWindowFlags(self.windowFlags() ^ Qt.WindowMaximizeButtonHint)

        self.setProperty("saveWindowPref", True)
        self.stacked_widget = QStackedWidget()

        self.setup_routes()
        self.setCentralWidget(self.stacked_widget)
        self.setStyleSheet(get_stylesheet())

    def setup_routes(self, new_routes=None):
        list_of_routes = new_routes

        if not list_of_routes:
            raise Exception("Routes not found")

        for route in list_of_routes:
            route.component.next_page = self.set_page
            self.stacked_widget.addWidget(route.component)

    def set_page(self, index=0):
        self.stacked_widget.setCurrentIndex(index)

    def get_page(self, name):
        return self.stacked_widget.findChild(QWidget, name)
