import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logfile.log")

formatter=logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.setLevel(logging.INFO)
logger.info("My First Info Log")
