import logging
import platform
import subprocess

from .settings import APP_NAME, LOG_LEVEL

__all__ = ["get_logger"]


# ANSI color codes
COLORS = {
    # "DEBUG": "\033[92m",  # Green
    "INFO": "\033[96m",   # Cyan
    "WARNING": "\033[93m",  # Yellow
    "ERROR": "\033[91m",   # Red
    "CRITICAL": "\033[91m\033[1m",  # Bright Red
    "RESET": "\033[0m",  # Reset to default
}


class ColoredFormatter(logging.Formatter):
    """Custom formatter to add colors to log messages."""

    def format(self, record):
        # Get the color for the log level (default is RESET/none)
        color = COLORS.get(record.levelname, COLORS["RESET"])
        reset = COLORS["RESET"]

        # Apply color to the log message
        record.levelname = f"{color}{record.levelname}{reset}"
        record.msg = f"{color}{record.msg}{reset}"
        return super().format(record)


def get_logger(name: str = APP_NAME, level=LOG_LEVEL) -> logging.Logger:
    """Set up and return a customized logger."""
    # Create or get the logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Check if the logger already has handlers to avoid duplication
    if not logger.handlers:
        # Create a console handler
        if LOG_LEVEL == 50:
            logger_handler = logging.FileHandler(f"{APP_NAME}.log")
        else:
            logger_handler = logging.StreamHandler()
        logger_handler.setLevel(level)

        # Create a formatter and add it to the handler
        formatter = ColoredFormatter(
            fmt="%(levelname)s - %(filename)s:%(lineno)d - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        logger_handler.setFormatter(formatter)

        # Add the handler to the logger
        logger.addHandler(logger_handler)

    return logger


# Example usage
if __name__ == "__main__":
    logger = get_logger()

    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")


if platform.system() == "Windows":
    subprocess.run("cls", shell=True)
elif platform.system() in ["Linux", "Darwin"]:  # Darwin is macOS
    subprocess.run("clear", shell=True)
