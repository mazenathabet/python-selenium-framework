import logging


def test_logging_demo():
    # get object of the logging class
    logger = logging.getLogger(__name__)

    # to set a file to print the logs on
    file_handler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)")
    file_handler.setFormatter(formatter)
    # error level has a hierarchy
    # debug
    # info
    # warning
    # error
    # critical
    # if you set the error level warning it means it will get all the logs from warning to above ( error, critical)
    logger.addHandler(file_handler)  # filehander object
    logger.setLevel(logging.ERROR)  # set the logging level
    # is more like the print method but i will print it in file and not console
    logger.debug("a debug statement is executed")
    logger.info("information statement")
    # when you want alert in logs but you don't want fail the test
    logger.warning("something is in warning mode")
    # when assertion fail
    logger.error(" a major error has happened")
    # critical issue
    logger.critical("Critical issue")
