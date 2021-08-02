import logging
import logging.handlers

def getLogger(logfile='myLog.log'):
    """Get the logger object from logging modules

    Args:
        logfile (str, optional): [The path of the log file]. Defaults to 'myLog.log'.

    Returns:
        [logging_obj]: [the logger object for logging things]. 
    """
    logger = logging.getLogger(logfile)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter('[%(filename)s:%(lineno)d] %(asctime)s %(levelname)s: %(message)s')

    # Rotating File Handler
    rotatingFilehandler = logging.handlers.RotatingFileHandler(
        logfile, maxBytes=(1048576*5), backupCount=10
    )
    rotatingFilehandler.setFormatter(formatter)
    logger.addHandler(rotatingFilehandler)

    # file Handler
    # fileHandler = logging.FileHandler(logfile, mode='a')
    # fileHandler.setFormatter(logFormatter)
    # logger.addHandler(fileHandler)

    # consoleHandler
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(formatter)
    logger.addHandler(consoleHandler)

    return logger


if __name__ == "__main__":
    logger = getLogger()
    logger.warning('ABC')



