import os
from pathlib import Path

# Codes Here

__all__ = [
    'BASE_DIR',
    'APP_NAME',
    'APP_VERSION',
    'ORGANIZATION_DOMAIN',
    'ORGANIZATION_NAME',
]

BASE_DIR = Path(__file__).parent.parent

# UI Settings

# Application Metadata
APP_NAME = 'Ganzabara'
APP_VERSION = '1.0.0'
ORGANIZATION_DOMAIN = 'Ganzabara.Vahrka'
ORGANIZATION_NAME = 'Vahrka'

# DEBUG = bool(os.environ.get(f"{APP_NAME}-DEBUG-MODE", False))
DEBUG = False
LOG_LEVEL = 10
# if DEBUG:
#     LOG_LEVEL = os.environ.get(f"{APP_NAME}-LOG-LEVEL", 10) # DEBUG=10
# else:
#     LOG_LEVEL = os.environ.get(f"{APP_NAME}-LOG-LEVEL", 50) # CRITICAL=50
