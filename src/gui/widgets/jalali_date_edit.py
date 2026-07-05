"""
JalaliDateEdit: a QDateEdit-like widget that displays and lets the user
pick dates in the Jalali calendar, while exposing/accepting standard
Python datetime.date (Gregorian) for storage in the database.
"""

from datetime import date as gdate
from typing import Optional

import jdatetime
from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QHBoxLayout, QLineEdit, QToolButton, QWidget

from src.gui.widgets.jalali_calendar_popup import JalaliCalendarPopup


class JalaliDateEdit(QWidget):
    """Usage:
        edit = JalaliDateEdit()
        edit.setDate(transaction.date)   # pass a Gregorian date.date()
        ...
        transaction.date = edit.date()   # get back a Gregorian date.date()
        edit.dateChanged.connect(...)    # emits Gregorian date.date()
    """

    dateChanged = Signal(object)  # emits datetime.date (Gregorian)

    DISPLAY_FORMAT = "%Y-%m-%d"

    def __init__(self, parent=None):
        super().__init__(parent)
        self._jalali_date: jdatetime.date = jdatetime.date.today()

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)

        self.line_edit = QLineEdit()
        self.line_edit.setReadOnly(True)

        self.calendar_btn = QToolButton()
        self.calendar_btn.setText("📅")
        self.calendar_btn.clicked.connect(self._open_popup)

        layout.addWidget(self.line_edit)
        layout.addWidget(self.calendar_btn)

        self._refresh_text()

    def _open_popup(self):
        popup = JalaliCalendarPopup(initial=self._jalali_date, parent=self)
        popup.dateSelected.connect(self._on_picked)
        # Position popup just under the widget
        pos = self.mapToGlobal(self.rect().bottomLeft())
        popup.move(pos)
        popup.show()

    def _on_picked(self, picked: jdatetime.date):
        self._jalali_date = picked
        self._refresh_text()
        self.dateChanged.emit(self.date())

    def _refresh_text(self):
        self.line_edit.setText(self._jalali_date.strftime(self.DISPLAY_FORMAT))

    # --- Public API, mirrors QDateEdit but in/out are Gregorian dates ---

    def date(self) -> gdate:
        """Return the currently selected date as a Gregorian date."""
        return self._jalali_date.togregorian()

    def setDate(self, value: gdate) -> None:
        """Set the widget's date from a Gregorian date."""
        self._jalali_date = jdatetime.date.fromgregorian(date=value)
        self._refresh_text()

    def jalaliDate(self) -> jdatetime.date:
        """Return the currently selected date as a Jalali date, if needed
        directly."""
        return self._jalali_date
