import logging

def mylog(logfilename):
    logging.basicConfig(level=logging.INFO, filename=logfilename, filemode='w',format='%(asctime)s - %(levelname)s - %(message)s')


def message(Loglevel, msg):
    """
    Loggt eine Nachricht mit dem angegebenen Log-Level.
    """
    loglevel = Loglevel.lower()
    if loglevel == "info":
        logging.info(msg)
    elif loglevel == "error":
        logging.error(msg)
    elif loglevel == "warning":
        logging.warning(msg)
    elif loglevel == "debug":
        logging.debug(msg)
    else:
        logging.info("Unbekanntes Loglevel: " + msg)