import inspect
import logging


class Base:
    def get_Logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        file_handler = logging.FileHandler("greenkart.log")

        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        return logger
