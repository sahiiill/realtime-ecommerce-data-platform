import logging

from logging.handlers import RotatingFileHandler


def setup_logger(log_file):

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            RotatingFileHandler(
                log_file,
                maxBytes=5_000_000,
                backupCount=3
            ),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger(__name__)