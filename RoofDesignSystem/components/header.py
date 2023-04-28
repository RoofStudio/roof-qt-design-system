from PySide6.QtWidgets import QGroupBox, QHBoxLayout, QLabel


class Header(QGroupBox):
    def __init__(self, title, *args, **kwargs):
        super().__init__(*args, **kwargs)

        label = QLabel(title)
        self.layout = QHBoxLayout()

        # add title widget and centralizing header
        self.layout.addStretch(1)
        self.layout.addWidget(label)
        self.layout.addStretch(1)

        self.setLayout(self.layout)
