## Critical, Error, Debug, Info, Execution
import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logging.debug("Debug Log: ")
logging.critical("Critical Log: ")
logging.error("Error Log: ")
logging.warning("Warning Log: ")
logging.info("Info. Log: ")