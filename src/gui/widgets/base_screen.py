from typing import override

from PySide6.QtWidgets import QWidget

from src.core.utils.logger import setup_logger

# Codes Here

logger = setup_logger()


class BaseScreen(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super(BaseScreen, self).__init__(*args, **kwargs)
        self.logger = logger

    @override
    def setup_ui(self):
        pass
