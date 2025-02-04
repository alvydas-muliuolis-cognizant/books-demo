import logging

LOG_FILE_ERROR = "error.log"
LOG_FORMAT_ERROR = "%(asctime)s - %(name)s - %(message)s"


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    file_handler_error = logging.FileHandler(LOG_FILE_ERROR, mode="a")
    file_handler_error.setFormatter(logging.Formatter(LOG_FORMAT_ERROR))
    file_handler_error.setLevel(logging.ERROR)
    logger.addHandler(file_handler_error)

    return logger
