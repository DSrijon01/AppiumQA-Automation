import logging

logging.basicConfig(format='%(asctime)s, %(levelname)s, %(message)s', datefmt='%d/%m/%y %I:%M:%S %p', level=logging.DEBUG, filename="format.log", filemode="w")
logging.debug("Debug Log: ")
logging.critical("Critical Log: ")
logging.error("Error Log: ")
logging.warning("Warning Log: ")
logging.info("Info. Log: ")
