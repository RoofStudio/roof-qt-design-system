from PySide6.QtWidgets import (
    QHBoxLayout,
    QLineEdit,
    QLabel,
    QVBoxLayout,
    QGroupBox,
)


class LineEdit(QGroupBox):
    def __init__(
        self, label_text="", value="", horizontal_label=False, *args, **kwargs
    ):
        super().__init__()
        self.label = QLabel(label_text)
        self.line_edit = QLineEdit(value, *args, **kwargs)
        self.content_widget = QGroupBox()

        self.content_layout = QHBoxLayout()
        self.layout = QHBoxLayout() if horizontal_label else QVBoxLayout()

        self.content_layout.addWidget(self.line_edit)
        self.content_widget.setLayout(self.content_layout)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.content_widget)

        # remove margins for all layout
        # the margins it will be managed by parent widget
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.layout)
        self.setObjectName("LineEdit")

    def text(self):
        return self.line_edit.text()

    def connect(self, action=None):
        if action:
            # connect signals in external events
            self.line_edit.returnPressed.connect(
                lambda: action(text=self.line_edit.text())
            )
