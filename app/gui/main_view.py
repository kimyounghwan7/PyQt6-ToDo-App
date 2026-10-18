from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
	QApplication, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout,
	QTableWidget, QTableWidgetItem, QTreeWidget, QTreeWidgetItem
)
from PySide6.QtGui import QColor, QGuiApplication
from PySide6.QtQuick import QQuickView

import sys
from loguru import logger

class Form(QDialog):
	def __init__(self, parent=None):
		super(Form, self).__init__(parent)
		self.colors: list = [
			("Red", "#FF0000"),
			("Green", "#00FF00"),
			("Blue", "#0000FF"),
			("Black", "#000000"),
			("White", "#FFFFFF"),
			("Electric Green", "#41CD52"),
			("Dark Blue", "#222840"),
			("Yellow", "#F9E56d")
		]
  
		self.tree_data: dict[str, str] = {
			"Project A": ["file_a.py", "file_b.py", "file_c.py"],
			"Project B": ["file_a.csv", "photo_a.png"],
			"Project C": ["temp.txt"],
		}
  
		self.setWindowTitle("My Form")
		self.edit = QLineEdit("write my name here")
		self.button = QPushButton("Show Greeting")
		self.button.clicked.connect(self.greetings)

		self.table: QTableWidget = self._init_table()
		self.qt_tree: QTreeWidget = self._init_tree()

		layout = QVBoxLayout(self)
		layout.addWidget(self.edit)
		layout.addWidget(self.button)
		layout.addWidget(self.table)
		layout.addWidget(self.qt_tree)

	def greetings(self):
		logger.info(f"Hello, {self.edit.text()}!")

	def _init_table(self) -> QTableWidget:
		table = QTableWidget()
		table.setRowCount(len(self.colors))
		table.setColumnCount(len(self.colors[0]) + 1)
		table.setHorizontalHeaderLabels(["Name", "Hex Code", "Color"])

		for i, (name, code) in enumerate(self.colors):
			item_name = QTableWidgetItem(name)
			item_code = QTableWidgetItem(code)
			item_color = QTableWidgetItem()
			item_color.setBackground(self.get_rgb_from_hex(code))
			table.setItem(i, 0, item_name)
			table.setItem(i, 1, item_code)
			table.setItem(i, 2, item_color)
		return table

	def _init_tree(self) -> QTreeWidget:
		tree = QTreeWidget()
		tree.setColumnCount(2)
		tree.setHeaderLabels(["Name", "Type"])
		items = []
		for key, values in self.tree_data.items():
			item = QTreeWidgetItem([key])
			for value in values:
				ext = value.split(".")[-1].upper()
				child = QTreeWidgetItem([value, ext])
				item.addChild(child)
			items.append(item)
		tree.insertTopLevelItems(0, items)
		return tree

	def get_rgb_from_hex(self, code: str) -> QColor:
		code_hex = code.replace("#", "")
		logger.info(code_hex)
		rgb = tuple(int(code_hex[i:i+2], 16) for i in (0, 2, 4))
		logger.info(rgb)
		return QColor.fromRgb(rgb[0], rgb[1], rgb[2])

def main_view():
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	sys.exit(app.exec())