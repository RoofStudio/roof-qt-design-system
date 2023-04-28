from PySide6.QtWidgets import QVBoxLayout, QWidget


class ContentComponent(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.layout.addStretch(1)

        self.setLayout(self.layout)
