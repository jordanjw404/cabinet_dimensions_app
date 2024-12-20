from PySide6.QtWidgets import QMainWindow, QStackedWidget, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QMessageBox, QTableWidgetItem

from unit_pages import create_unit_page
from calculator import determine_parts

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cabinet Design System")
        self.setGeometry(100, 100, 800, 600)

        self.main_widget = QWidget()
        self.main_layout = QHBoxLayout(self.main_widget)

        self.menu_layout = QVBoxLayout()
        unit_types = [
            "Base Unit", "Wall Unit", "Tall Unit",
            "Oven Housing Unit", "Antaro Drawer Base Unit", "Legra Drawer Base Unit"
        ]
        self.pages = QStackedWidget()
        self.tables = {}

        for index, unit_type in enumerate(unit_types):
            page, table = create_unit_page(unit_type, self.calculate_and_update_table)
            self.pages.addWidget(page)
            self.tables[unit_type] = table

            button = QPushButton(unit_type)
            button.clicked.connect(lambda checked, idx=index: self.pages.setCurrentIndex(idx))
            self.menu_layout.addWidget(button)

        self.menu_layout.addStretch(1)
        self.main_layout.addLayout(self.menu_layout, 1)
        self.main_layout.addWidget(self.pages, 4)
        self.setCentralWidget(self.main_widget)

    def calculate_and_update_table(self, line_edits, unit_type, page):
        try:
            values = {key: float(edit.text()) for key, edit in line_edits.items()}
            values['Shelf Total'] = int(values['Shelf Total'])
        except ValueError:
            QMessageBox.critical(self, "Input Error", "Please enter valid numeric values.")
            return

        table = self.tables[unit_type]
        parts = determine_parts(values, unit_type)
        table.setRowCount(len(parts))
        for row, (qty, part, part_width, part_length, part_depth) in enumerate(parts):
            table.setItem(row, 0, QTableWidgetItem(qty))
            table.setItem(row, 1, QTableWidgetItem(part))
            table.setItem(row, 2, QTableWidgetItem(str(part_width)))
            table.setItem(row, 3, QTableWidgetItem(str(part_length)))
            table.setItem(row, 4, QTableWidgetItem(str(part_depth)))
