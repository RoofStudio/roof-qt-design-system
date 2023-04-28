from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from app.components.header import Header


class Page(QWidget):
    def __init__(self, parent=None, title="Page Name"):
        super().__init__(parent)

        header = Header(title)
        self.layout = QVBoxLayout()
        self.layout.addWidget(header)

        # set margin to default
        # the child components it will control the margins and paddings
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
