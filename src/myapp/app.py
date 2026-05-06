import sys

from loguru import logger

_LEVEL_ABBR = {
    "TRACE": "TRC",
    "DEBUG": "DBG",
    "INFO": "INF",
    "SUCCESS": "SUC",
    "WARNING": "WRN",
    "ERROR": "ERR",
    "CRITICAL": "CRT",
}


def _log_format(record: dict) -> str:
    record["extra"]["lvl"] = _LEVEL_ABBR.get(record["level"].name, record["level"].name[:3])
    return (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{extra[lvl]}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
        "<level>{message}</level>\n{exception}"
    )


def configure_logging():
    """Configure loguru for console and file logging.

    Removes the default handler and sets up:
    - stderr handler at LOG_LEVEL (default: INFO, configurable via env var)
    - File handler at DEBUG level writing to LOG_FILE (default: app.log)

    Log format: ``YYYY-MM-DD HH:mm:ss | LVL | module:func:line | message``
    where LVL is a 3-char abbreviation (INF, DBG, WRN, ERR, …).
    """
    import os

    log_level = os.environ.get("LOG_LEVEL", "INFO")
    log_file = os.environ.get("LOG_FILE", "app.log")
    logger.remove()
    logger.add(sys.stderr, level=log_level, format=_log_format)
    logger.add(log_file, level="DEBUG", rotation="50 KB", retention=1, format=_log_format)


@logger.catch
def main():
    """Run the application.

    Configures logging and prints a greeting to verify the setup works.
    """
    configure_logging()
    logger.info("Hello from myapp!")
