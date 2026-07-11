from pathlib import Path

from utils.logger import get_logger

logger = get_logger()

__all__ = [
    'BASE_DIR',
    'APP_NAME',
    'APP_VERSION',
    'ORGANIZATION_DOMAIN',
    'ORGANIZATION_NAME',
]

BASE_DIR = Path(__file__).parent.parent.parent

# UI Settings

# Application Metadata
APP_NAME = 'Ganzabara'
APP_VERSION = '1.0.0'
ORGANIZATION_DOMAIN = 'ac.soft'
ORGANIZATION_NAME = 'Free Tech'
