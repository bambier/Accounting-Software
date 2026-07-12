#! /usr/bin/env python3
import platform
import sys

# Reources
import source_rc
# Local imports
from app import Application
from main_window import MainWindow
from utils.logger import get_logger
from utils.settings import APP_NAME
from utils.shortcutes import get_database_path, initialize_database




# Codes Here
logger = get_logger(APP_NAME)

# --------------------------------------------------------------------------- #
# License-enforced platform guard
# --------------------------------------------------------------------------- #
# NCHL-1.1 §3.e: "Compile or build any kind of software for MacOS or IOS" is
# a prohibited action without a commercial agreement. We refuse to proceed
# rather than silently produce an unsupported/unlicensed build artifact.
if sys.platform == "darwin" or platform.system() == "Darwin":
    message = (
        "\n"
        f"Building {APP_NAME} for macOS/iOS is not permitted.\n"
        "See LICENSE (NCHL-1.1, Section 3.e). Supported build targets are\n"
        "Windows and Linux only. Contact Vahrka for commercial licensing\n"
        "options if macOS/iOS support is required.\n"
    )
    logger.critical(message)
    sys.exit(message)


def main():
    try:
        # Initialize database
        db_path = get_database_path()
        initialize_database(db_path)

    except Exception as e:
        logger.error("Couldn't initialize database.")
        logger.critical(e)
        sys.exit(1)

    try:
        # Set up application
        app = Application().run()

    except Exception as e:
        logger.error("Couldn't set up application.")
        logger.critical(e)
        sys.exit(1)

    try:
        # Create and show main window
        main_window = MainWindow()
        # main_window.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        # main_window.setWindowState(Qt.WindowState.WindowMaximized)
        main_window.setMinimumWidth(1024)
        main_window.setMinimumHeight(768)

        main_window.show()

        # Start event loop
        exit_code = app.exec()

        sys.exit(exit_code)

    except Exception as e:
        logger.error("Couldn't create and show main window.")
        logger.critical(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
