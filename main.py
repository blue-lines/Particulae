__author__ = 'Julien Heck'


import configparser
import logging
import sys

if __name__ == "__main__":

    logfile_name = "particulae.log"

    try:
        logging.basicConfig(filename=logfile_name,
                            level=logging.DEBUG,
                            format='%(asctime)s, %(levelname)s, %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
    except:
        print("Failed to open log file {0}".format(logfile_name))
        sys.exit(-1)

    logging.info("Starting execution")

    try:
        config = configparser.ConfigParser()
        config.read("setup.cfg")
    except:
        logging.error("Failed to read config file")
        sys.exit(-1)

    logging.info("Parser setup")





    logging.info("Terminating execution")
