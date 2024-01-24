import logging
import threading
from os.path import basename
import time
import concurrent.futures


logpath = basename(__file__) + '.txt'
lock = threading.Lock


def safe_logging(massage, logger):
    with lock:
        with open(open(logpath, "a")) as logfile:
            logfile.write(massage)


def main():
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
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:



if __name__ == "__main__":
    main()
