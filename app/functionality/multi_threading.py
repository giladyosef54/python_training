import logging
import threading
from os.path import basename, splitext
import concurrent.futures


logpath = splitext(basename(__file__))[0] + '.txt'
lock = threading.Lock()


def safe_logging(name):
    with lock:
        logging.info(name)


def create_and_log_threads(threads_num):
    # create a logger
    logger = logging.getLogger()
    # set logger level
    logger.setLevel(logging.INFO)

    # create file handler
    file_hdlr = logging.FileHandler(logpath, mode='a')
    # set level
    file_hdlr.setLevel(logging.INFO)

    # add handler to logger
    logger.addHandler(file_hdlr)


    fmt = "%(asctime)s: %(message)s"

    logging.basicConfig(format=fmt, filename=logpath, level=logging.INFO, datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads_num) as executor:
        executor.map(safe_logging, range(threads_num))

