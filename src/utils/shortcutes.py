import sys
from pathlib import Path

from models import (create_tables, db_manager, init_database,
                    initialize_test_data)
# Local imports
from utils.logger import get_logger
from utils.settings import BASE_DIR

from .settings import APP_NAME

logger = get_logger()

# Database Path exists


def check_db_path_exist() -> Path:
    data_dir = BASE_DIR / 'data'
    data_dir.mkdir(exist_ok=True, parents=True)
    return data_dir


# Database Settings
def get_database_path() -> Path:
    """Get the path to the SQLite database file"""
    data_dir = check_db_path_exist()
    return data_dir / f'{APP_NAME}.db'


def initialize_database(path: Path | str) -> None:
    """Initialize database connection"""
    try:
        # Initialize database
        db = init_database(path)

        # Connect to database
        db_manager.connect()

        # Create tables
        create_tables()

        # Add test data if empty
        initialize_test_data()

        logger.info("Database initialized successfully!")

    except Exception as e:
        logger.critical(f"Failed to initialize database:\n{str(e)}")
        sys.exit(1)
