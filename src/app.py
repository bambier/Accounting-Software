"""
Application initialization and configuration module.

This module provides the Application class which handles the setup and 
configuration of the Qt application instance, including fonts, icons,
translations, and stylesheets.
"""

import sys

from PySide6.QtCore import QFile, QLibraryInfo, QLocale, QSettings, QTranslator
from PySide6.QtGui import QFont, QFontDatabase, QIcon
from PySide6.QtWidgets import QApplication

from utils.logger import get_logger
from utils.settings import (APP_NAME, APP_VERSION, ORGANIZATION_DOMAIN,
                            ORGANIZATION_NAME)

logger = get_logger()


class Application:
    """
    Application class responsible for initializing and configuring the Qt application.

    This class handles the setup of the main application instance, including
    font loading, icon configuration, translation support, and stylesheet
    application. It follows the singleton pattern through the Qt framework.

    Attributes:
        app (QApplication): The main Qt application instance.
    """

    def __init__(self):
        """
        Initialize the Application instance and configure all application settings.

        This constructor sets up the application's core configurations including:
        - Application metadata (name, version, organization)
        - Font system
        - Application icon
        - Translation support
        - Stylesheet
        """
        # Set up application settings to use INI format for configuration storage
        QSettings.setDefaultFormat(QSettings.IniFormat)  # type: ignore

        # Create application instance with command line arguments
        self.app = QApplication(sys.argv)

        # Set application metadata for system identification
        self.app.setApplicationName(APP_NAME)
        self.app.setApplicationVersion(APP_VERSION)
        self.app.setOrganizationDomain(ORGANIZATION_DOMAIN)
        self.app.setOrganizationName(ORGANIZATION_NAME)

        # Configure application components

        try:
            self.__setup_fonts()
        except Exception as e:
            logger.error(f"Couldn't setup fonts.\n{e}")

        try:
            self.__setup_icon()
        except Exception as e:
            logger.error(f"Couldn't setup icon.\n{e}")

        try:
            self.__setup_translator()
        except Exception as e:
            logger.error(f"Couldn't setup translator.\n{e}")
        try:
            self.__setup_stylesheet()
        except Exception as e:
            logger.error(f"Couldn't setup stylesheet.\n{e}")

    def run(self) -> QApplication:
        """
        Return the configured QApplication instance.

        Returns:
            QApplication: The initialized Qt application instance.
        """
        return self.app

    def __setup_fonts(self):
        """
        Load and configure custom fonts for the application.

        This method loads Vazirmatn font family from resources and sets
        the Regular variant as the default application font. If the Regular
        variant is not found, it falls back to the first available font
        or the system default.

        The method logs success or failure for each font file loaded.
        """
        # Initialize font database for font management
        font_db = QFontDatabase()

        # List of font files to load from application resources
        font_files = [
            ":/fonts/Vazirmatn-RD-UI-FD-Black",
            ":/fonts/Vazirmatn-RD-UI-FD-Bold",
            ":/fonts/Vazirmatn-RD-UI-FD-ExtraBold",
            ":/fonts/Vazirmatn-RD-UI-FD-ExtraLight",
            ":/fonts/Vazirmatn-RD-UI-FD-Light",
            ":/fonts/Vazirmatn-RD-UI-FD-Medium",
            ":/fonts/Vazirmatn-RD-UI-FD-Regular",
            ":/fonts/Vazirmatn-RD-UI-FD-SemiBold",
            ":/fonts/Vazirmatn-RD-UI-FD-Thin",
        ]

        # Clear any previously loaded application fonts to avoid duplicates
        QFontDatabase.removeAllApplicationFonts()

        # Load each font file into the application
        for font_file in font_files:
            font_id = font_db.addApplicationFont(font_file)
            if font_id == -1:
                logger.error(f"Failed to load font: {font_file}")
        else:
            font_dic = QSettings(self.app).value("font-family", defaultValue={"Vazirmatn RD UI FD": 250})
            font = list(font_dic.keys())  # pyright: ignore[reportAttributeAccessIssue]
            self.app.setFont(QFont(font[0], 10))

    def __setup_icon(self):
        """
        Set the application window icon.

        Loads the icon from resources and sets it as the application's
        main window icon.
        """
        self.app.setWindowIcon(QIcon(":/img-icon/icon-ico"))

    def __setup_translator(self):
        """
        Configure internationalization support for the application.
        Supports both Qt built-in translations and custom application translations.
        """
        self.translators = []
        self.qt_translator = None
        self.app_translator = None

        # Load saved language preference
        settings = QSettings()
        saved_language = str(settings.value("language", "en"))

        # Language mapping for Qt translations
        qt_lang_map = {
            "en": "en",
            "fa": "fa",
            "de": "de",
            "az": "az",
            "tu": "tr",
            "az-ir": "fa",  # Qt has no az-ir translations.
            "ru": "ru"
        }

        # 1. Load Qt built-in translations
        qt_lang = qt_lang_map.get(saved_language, "en")
        qt_path = QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)

        if qt_lang != "en":
            # Load Qt main translations
            self.qt_translator = QTranslator(self.app)
            if self.qt_translator.load(f"qt_{qt_lang}.qm", qt_path):
                self.app.installTranslator(self.qt_translator)
                self.translators.append(self.qt_translator)
                logger.info(f"Loaded Qt translations: qt_{qt_lang}.qm")

            # Load Qt base translations
            qt_base = QTranslator(self.app)
            if qt_base.load(f"qtbase_{qt_lang}.qm", qt_path):
                self.app.installTranslator(qt_base)
                self.translators.append(qt_base)

        # 2. Load application translations
        app_lang_map = {
            "en": "en", "fa": "fa", "de": "de",
            "az": "az", "tu": "tu", "az-ir": "az-ir", "ru": "ru"
        }

        app_lang = app_lang_map.get(saved_language, "en")

        if app_lang != "en":
            self.app_translator = QTranslator(self.app)

            # Try loading from resources
            if self.app_translator.load(app_lang, APP_NAME, "_", ":/locales"):
                self.app.installTranslator(self.app_translator)
                self.translators.append(self.app_translator)
                logger.info(f"Loaded app translations: {APP_NAME}{app_lang}.qm")
            elif self.app_translator.load(f":/locales/{app_lang}"):
                self.app.installTranslator(self.app_translator)
                self.translators.append(self.app_translator)
                logger.info(f"Loaded app translations: {app_lang}")

    def __setup_stylesheet(self):
        """
        Apply the application-wide stylesheet.

        Loads the default stylesheet from resources and applies it
        to the entire application. The stylesheet defines the visual
        appearance of all widgets in the application.

        Logs an error message if the stylesheet file cannot be loaded.
        """
        # Load stylesheet application wide
        style_file = QFile(":/styles/default-style")
        if style_file.open(QFile.ReadOnly | QFile.Text):  # pyright: ignore[reportAttributeAccessIssue]
            self.app.setStyleSheet(
                str(style_file.readAll(), encoding="utf-8"))  # type: ignore
        else:
            logger.error("Failed to load style sheet.")
