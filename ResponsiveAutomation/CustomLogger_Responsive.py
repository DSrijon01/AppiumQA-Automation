import inspect
import logging

def customLogger():
    # Get the name of the calling function
    caller_function = inspect.stack()[1][3]

    # Replace invalid characters in the function name to create a valid log filename
    log_filename = f"{caller_function.replace('<', '_').replace('>', '_')}.log"

    # Create the logging object with the caller_function as the logger name
    logger = logging.getLogger(caller_function)

    # Set the log level
    logger.setLevel(logging.DEBUG)

    # Create the fileHandler to save the logs in the file
    fileHandler = logging.FileHandler(log_filename, mode='w')

    # Set the log level for fileHandler
    fileHandler.setLevel(logging.DEBUG)

    # Create the formatter for log messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%d/%m/%y %I:%M:%S %p %A')

    # Set the formatter for fileHandler
    fileHandler.setFormatter(formatter)

    # Add the fileHandler to the logger
    logger.addHandler(fileHandler)

    # Finally, return the logger object
    return logger
