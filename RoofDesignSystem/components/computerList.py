from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView


class ComputerList(QTableWidget):
    def __init__(
        self, computers, parent=None, header=["Computer Name", "Status", "User"]
    ):
        super(ComputerList, self).__init__(parent)

        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(header)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for computer in computers:
            self.add_computer(computer)

    def add_computer(self, computer):
        row = self.rowCount()

        if type(computer) != str:
            self.insertRow(row)
            self.setItem(row, 0, QTableWidgetItem(computer["name"]))
            self.setItem(row, 1, QTableWidgetItem(computer["status"]))
            self.setItem(row, 2, QTableWidgetItem(computer.get("username", "")))

    def get_item_by_column_text(self, column, text):
        for row in range(self.rowCount()):
            item = self.item(row, column)
            if item and item.text() == text:
                return item
        return None

    def update_computer_list(self, computer_list):
        self.setRowCount(0)
        for computer in computer_list:
            if type(computer) != bool:
                self.add_computer(computer)
