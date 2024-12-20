from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QTableWidget


def create_unit_page(unit_type, calculate_callback):
    page = QWidget()
    layout = QGridLayout(page)

    labels = ["Width:", "Height:", "Depth:", "Void:", "Leg Height:", "Inset:", "Shelf Total:"]
    default_values = [600, 720, 570, 50, 150, 2, 1]
    line_edits = {label.strip(':'): QLineEdit(str(default_values[i])) for i, label in enumerate(labels)}

    for i, label in enumerate(labels):
        layout.addWidget(QLabel(label), i, 0)
        layout.addWidget(line_edits[label.strip(':')], i, 1)

    calculate_button = QPushButton("Calculate")
    calculate_button.clicked.connect(lambda: calculate_callback(line_edits, unit_type, page))
    layout.addWidget(calculate_button, len(labels), 0, 1, 2)

    table = QTableWidget(0, 5)
    table.setHorizontalHeaderLabels(["QTY", "Part", "Width", "Length", "Depth"])
    layout.addWidget(table, len(labels) + 1, 0, 1, 2)

    return page, table
