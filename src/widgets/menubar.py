from pathlib import Path

from PySide6.QtCore import QUrl, Slot
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QFileDialog, QMainWindow

from controllers.settings import Settings
from plugins.loader import register_plugin
from ui.main_window_ui import Ui_MainWindow
from utils.logger import get_logger
from widgets.plugins_list import PluginsListView

logger = get_logger()


class Menubar:
    """A custom menubar class that sets up the UI and handles menu actions."""

    def __init__(self, main_window: QMainWindow):
        self.ui: Ui_MainWindow = main_window.ui  # type: ignore
        self.parent = main_window

        self.actionContact = self.ui.actionContact
        self.actionInfo = self.ui.actionInfo
        self.actionHelp = self.ui.actionHelp

        self.actionRegister = self.ui.actionRegister
        self.actionList = self.ui.actionList
        self.actionImport = self.ui.actionImport
        self.actionExport = self.ui.actionExport

        self.actionPrefrences = self.ui.actionPrefrences
        self._add_style_properties()

    def _add_style_properties(self):
        """Add only the necessary properties for modern styling."""
        # Highlight important actions
        self.actionContact.setProperty("highlighted", "true")
        self.actionPrefrences.setProperty("type", "settings")

        # Add accessible names for styling
        self.actionRegister.setProperty("name", "register")
        self.actionList.setProperty("name", "plugin-list")
        self.actionImport.setProperty("name", "import")
        self.actionExport.setProperty("name", "export")

    def setup_ui(self):
        """Initialize and configure the actions for the menubar."""
        # Connect the actions to their handlers
        self.actionRegister.triggered.connect(self.register_plugin)
        self.actionContact.triggered.connect(self.open_contact)
        self.actionInfo.triggered.connect(self.open_info)
        self.actionList.triggered.connect(self.open_plugins_list)
        self.actionImport.triggered.connect(self.import_data)
        self.actionExport.triggered.connect(self.export_data)
        self.actionPrefrences.triggered.connect(self.open_settings)

    @Slot()
    def register_plugin(self):
        """Handle the 'Register' action by opening a file dialog to select a folder."""
        folder_path = Path(QFileDialog.getExistingDirectory()).absolute()

        if folder_path:
            main_window = self.parent
            register_plugin(path=folder_path, add_func=main_window.add_to_screen)  # type: ignore

    @Slot()
    def open_contact(self):
        """Open the contact URL in the web browser."""
        url = QUrl("https://github.com/Vahrka/Ganzabara/discussions")
        if not QDesktopServices.openUrl(url):
            logger.error(f"Failed to open URL: {url}")

    @Slot()
    def open_info(self):
        """Open the info URL in the web browser."""
        url = QUrl("https://github.com/Vahrka/Ganzabara")
        if not QDesktopServices.openUrl(url):
            logger.error(f"Failed to open URL: {url}")

    @Slot()
    def open_plugins_list(self):
        """Show the plugins list in a new window."""
        plugins_list = PluginsListView(self.parent)
        plugins_list.setup_ui()
        plugins_list.show()

    @Slot()
    def import_data(self):
        """Handle the import action."""
        # Add your import functionality here
        pass

    @Slot()
    def export_data(self):
        """Handle the export action."""
        # Add your export functionality here
        pass

    @Slot()
    def open_settings(self):
        settings_window = Settings(self.parent)
        settings_window.setup_ui()
        settings_window.show()
