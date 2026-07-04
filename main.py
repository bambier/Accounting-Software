#! /usr/bin/env python3
import sys

from PySide6.QtCore import QFile, QLibraryInfo, QLocale, QSettings, QTranslator
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QApplication

# Reources
import source_rc
# Local imports
from src.core.database.models import initialize_database
from src.core.plugins.loader import load_internal_plugins
from src.core.utils.logger import get_logger
from src.core.utils.settings import (APP_NAME, APP_VERSION,
                                     ORGANIZATION_DOMAIN, ORGANIZATION_NAME)
from src.core.utils.shortcutes import get_database_path, load_fonts
from src.gui.main_window import MainWindow

# Codes Here
logger = get_logger(APP_NAME)


def setup_application():
    """Configure the QApplication instance."""
    # Set up application settings
    QSettings.setDefaultFormat(QSettings.IniFormat)  # type: ignore

    # Create application instance
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setOrganizationName(ORGANIZATION_NAME)
    app.setOrganizationDomain(ORGANIZATION_DOMAIN)
    app.setApplicationDisplayName(APP_NAME)
    app.setApplicationVersion(APP_VERSION)
    app.setFont(QFont(":/fonts/Vazirmatn-RD-UI-FD-Regular", 10))
    app.setWindowIcon(QIcon(":/img-icon/icon-ico"))

    path = QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)
    translator = QTranslator(app)
    if translator.load(QLocale.system(), 'qtbase', '_', path):
        app.installTranslator(translator)
    translator = QTranslator(app)
    path = ':/translations'
    if translator.load(QLocale.system(), 'example', '_', path):
        app.installTranslator(translator)

    # Load stylesheet in main.py
    style_file = QFile(":/styles/default-style")
    if style_file.open(QFile.ReadOnly | QFile.Text):  # pyright: ignore[reportAttributeAccessIssue]
        app.setStyleSheet(str(style_file.readAll(), encoding="utf-8"))  # type: ignore
    else:
        logger.error("Faild to load style sheet.")

    return app


def main():
    try:
        # Initialize database
        db_path = get_database_path()
        initialize_database(db_path)

        # Set up application
        app = setup_application()
        load_fonts()

        # Create and show main window
        main_window = MainWindow()
        # main_window.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        # main_window.setWindowState(Qt.WindowState.WindowMaximized)
        main_window.setMinimumWidth(1024)
        main_window.setMinimumHeight(720)
        # Load installed plugins
        load_internal_plugins(main_window.add_to_screen)

        main_window.show()

        # Start event loop
        exit_code = app.exec()

        # Remove registerd plugins so next time we can register them again
        QSettings().remove('registerd_plugins')

        sys.exit(exit_code)

    except Exception as e:
        logger.critical(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
