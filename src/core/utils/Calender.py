"""
Calendar utilities: convert and format dates in both Jalali (Shamsi)
and Gregorian calendars.

Storage stays Gregorian (ISO format) everywhere in the database — only
display/input is calendar-aware. This keeps sorting, DB queries, and
date arithmetic simple regardless of which calendar the user prefers.
"""

from datetime import date as gdate
from datetime import datetime as gdatetime
from enum import Enum

import jdatetime


class CalendarType(str, Enum):
    GREGORIAN = "gregorian"
    JALALI = "jalali"


def to_jalali(value: gdate) -> jdatetime.date:
    """Convert a Gregorian date to Jalali."""
    return jdatetime.date.fromgregorian(date=value)


def to_gregorian(value: jdatetime.date) -> gdate:
    """Convert a Jalali date back to Gregorian."""
    return value.togregorian()


def format_date(value: gdate, calendar: CalendarType = CalendarType.GREGORIAN,
                fmt: str = "%Y-%m-%d") -> str:
    """Format a stored (Gregorian) date for display in the chosen calendar."""
    if calendar == CalendarType.JALALI:
        return to_jalali(value).strftime(fmt)
    return value.strftime(fmt)


def format_both(value: gdate, fmt: str = "%Y-%m-%d") -> str:
    """Convenience: show both calendars together, e.g. for reports."""
    return f"{value.strftime(fmt)}  ({to_jalali(value).strftime(fmt)})"


def parse_date(text: str, calendar: CalendarType = CalendarType.GREGORIAN,
               fmt: str = "%Y-%m-%d") -> gdate:
    """Parse user input in the chosen calendar and return a Gregorian date
    for storage."""
    if calendar == CalendarType.JALALI:
        return to_gregorian(jdatetime.datetime.strptime(text, fmt).date())
    return gdatetime.strptime(text, fmt).date()
