"""
A month-grid popup calendar rendered in Jalali (Shamsi), used by
JalaliDateEdit. Qt's own QCalendarWidget has no Jalali backend, so this
draws the grid manually with jdatetime.
"""

from typing import Optional

import jdatetime
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout, QLabel, QPushButton,
                               QToolButton, QVBoxLayout, QWidget)


class JalaliCalendarPopup(QWidget):
    """Borderless popup grid for picking a Jalali date."""

    dateSelected = Signal(object)  # emits jdatetime.date

    def __init__(self, initial: Optional[jdatetime.date] = None, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.WindowType.Popup)
        self.current = initial or jdatetime.date.today()
        self._build_ui()
        self._render_month()

    def month_name(self, month: int) -> str:
        """Translatable Jalali month name. month is 1-12."""
        names = [
            self.tr("Farvardin"), self.tr("Ordibehesht"), self.tr("Khordad"),
            self.tr("Tir"), self.tr("Mordad"), self.tr("Shahrivar"),
            self.tr("Mehr"), self.tr("Aban"), self.tr("Azar"),
            self.tr("Dey"), self.tr("Bahman"), self.tr("Esfand"),
        ]
        return names[month - 1]

    def weekday_headers(self) -> list:
        """Translatable single/short letter weekday headers, Sat -> Fri."""
        return [
            self.tr("Sa"), self.tr("Su"), self.tr("Mo"), self.tr("Tu"),
            self.tr("We"), self.tr("Th"), self.tr("Fr"),
        ]

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)

        nav = QHBoxLayout()
        self.prev_btn = QToolButton()
        self.prev_btn.setText("<")
        self.prev_btn.clicked.connect(self._go_prev_month)

        self.title_label = QLabel()
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.next_btn = QToolButton()
        self.next_btn.setText(">")
        self.next_btn.clicked.connect(self._go_next_month)

        nav.addWidget(self.prev_btn)
        nav.addWidget(self.title_label, stretch=1)
        nav.addWidget(self.next_btn)
        layout.addLayout(nav)

        self.grid = QGridLayout()
        self.grid.setSpacing(2)
        layout.addLayout(self.grid)

        self.header_labels = []
        for col, name in enumerate(self.weekday_headers()):
            header = QLabel(name)
            header.setAlignment(Qt.AlignmentFlag.AlignCenter)
            header.setProperty("class", "calendar_weekday")
            self.grid.addWidget(header, 0, col)
            self.header_labels.append(header)

    def retranslateUi(self):
        """Call this from your app's language-change handler to refresh text."""
        for header, name in zip(self.header_labels, self.weekday_headers()):
            header.setText(name)
        self._render_month()

    def _go_prev_month(self):
        year, month = self.current.year, self.current.month
        month -= 1
        if month == 0:
            month, year = 12, year - 1
        self.current = jdatetime.date(year, month, 1)
        self._render_month()

    def _go_next_month(self):
        year, month = self.current.year, self.current.month
        month += 1
        if month == 13:
            month, year = 1, year + 1
        self.current = jdatetime.date(year, month, 1)
        self._render_month()

    def _render_month(self):
        # Remove all day buttons from previous render (keep row 0 headers)
        for row in range(1, self.grid.rowCount()):
            for col in range(7):
                item = self.grid.itemAtPosition(row, col)
                if item and item.widget():
                    item.widget().deleteLater()

        year, month = self.current.year, self.current.month
        self.title_label.setText(f"{self.month_name(month)} {year}")

        first_of_month = jdatetime.date(year, month, 1)
        start_col = first_of_month.weekday()  # Sat=0 ... Fri=6
        days_in_month = self._days_in_jalali_month(year, month)

        row, col = 1, start_col
        today = jdatetime.date.today()
        for day in range(1, days_in_month + 1):
            btn = QPushButton(str(day))
            btn.setFixedSize(32, 28)
            btn.setFlat(True)
            if (year, month, day) == (today.year, today.month, today.day):
                btn.setProperty("class", "calendar_today")
            if (year, month, day) == (self.current.year, self.current.month, self.current.day):
                btn.setProperty("class", "calendar_selected")
            btn.clicked.connect(lambda checked, d=day: self._pick(d))
            self.grid.addWidget(btn, row, col)
            col += 1
            if col == 7:
                col = 0
                row += 1

    @staticmethod
    def _days_in_jalali_month(year: int, month: int) -> int:
        if month <= 6:
            return 31
        if month <= 11:
            return 30
        return 30 if jdatetime.date.isleap(year) else 29

    def _pick(self, day: int):
        picked = jdatetime.date(self.current.year, self.current.month, day)
        self.dateSelected.emit(picked)
        self.close()
