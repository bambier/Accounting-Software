from pathlib import Path

from PySide6.QtCore import QSize, Qt, Slot
from PySide6.QtGui import QIcon, QPixmap, QStandardItem, QStandardItemModel
from PySide6.QtWidgets import (QFileDialog, QHBoxLayout, QHeaderView,
                               QTabWidget, QToolButton, QWidget)

from src.core.database.models import Billing, db
from src.core.utils.logger import get_logger

from .ui.form_ui import Ui_Form

logger = get_logger()

# TODO: do not add item to db before saving using save btn


class SalesScreen(QTabWidget):

    def setup_ui(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        path = Path(__file__).parent / "styles" / "sales.qss"
        with open(path, "r", encoding="UTF-8") as style_file:
            self.setStyleSheet(style_file.read())

        self.ui.save_btn.clicked.connect(self.save)
        self.ui.select_logo_btn.clicked.connect(self.select_logo)
        self.ui.add_to_record_btn.clicked.connect(self.add_record)
        self.ui.select_costumer_btn.clicked.connect(self.select_costumer)


        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # type: ignore
        # self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)  # type: ignore
        self.ui.tableView.setColumnWidth(0, 5000)
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels([
            self.tr("Name"),
            self.tr("Price"),
            self.tr("Count"),
            self.tr("Total"),
            self.tr("Action"),
        ])
        self.ui.tableView.setModel(self.model)

        self.retranslateUi()

    def retranslateUi(self):
        self.setTabText(0, self.tr("Invoices"))
        self.setTabText(1, self.tr("Customers"))

    @Slot(name="Save to db")
    def save(self):
        print("Saved")

    @Slot(name="Select Loog")
    def select_logo(self):
        file_path, selected_filter = QFileDialog.getOpenFileName(
            caption=self.tr("Select an Image"),
            filter=(
                "PNG (*.png);;"
                "JPEG (*.jpg *.jpeg);;"
                "SVG (*.svg);;"
                "Web (*.webp);;"
                "BMP (*.bmp);;"
                "TIFF (*.tif *.tiff);;"
                "PPM (*.ppm);;"
                "PGM (*.pgm);;"
                "PBM (*.pbm);;"
                "Favicons (*.ico)"
            ),
        )

        if file_path:
            pixmap = QPixmap(Path(file_path).absolute())
            pixmap = pixmap.scaled(250, 250, Qt.AspectRatioMode.KeepAspectRatio)
            self.ui.image_lable.setPixmap(pixmap)

    @Slot(name="Add record to list")
    def add_record(self) -> None:
        name = self.ui.billing_name_input.text()
        price = self.ui.price_input.text() or 0
        count = self.ui.count_input.text() or 0
        if all([name, price, count]):
            try:
                price = int(price)
                count = int(count)

                self.model = self.ui.tableView.model()
                row_items = ([
                    QStandardItem(name),
                    QStandardItem(str(price)),
                    QStandardItem(str(count)),
                    QStandardItem(str(price * count)),
                    QStandardItem(),
                ])

                for i in range(len(row_items)):
                    row_items[i].setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                self.model.appendRow(row_items)  # type: ignore
                self.add_delete_button(self.model.rowCount() - 1)

                self.ui.billing_name_input.clear()
                self.ui.price_input.clear()
                self.ui.count_input.clear()

            except ValueError as value_error:
                logger.error(f"Price and Count must be integer number.\n{value_error}",)

            except Exception as error:
                logger.fatal(f"Unexpected error happend.\n{error}",)

    def add_delete_button(self, row: int) -> None:
        # Create a container widget for perfect centering
        container = QWidget()
        layout = QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create icon button
        btn = QToolButton()
        btn.setProperty("class", "table_delete_btn")
        icon = QIcon(":/icons/delete-2.svg")
        btn.setIcon(icon)
        btn.setToolTip(self.tr("Delete"))
        btn.clicked.connect(lambda checked, r=row: self.delete_row(r))
        layout.addWidget(btn)

        # Set container in table cell
        self.ui.tableView.setIndexWidget(
            self.model.index(row, 4),  # Assuming column 4 is action column
            container
        )

    def delete_row(self, row: int) -> None:
        try:
            # Remove from table
            self.model.removeRow(row)

            # Reindex remaining buttons
            for r in range(row, self.model.rowCount()):
                self.add_delete_button(r)

        except Exception as e:
            logger.error(f"Error deleting row:\n{e}")




    def select_costumer(self):
        print("Select costumer")