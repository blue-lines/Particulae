__author__ = 'Julien Heck'


import configparser
import logging
import sys
import time
import google_finance
import mongodb

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

    db = mongodb.mongoDatabase()

    ######
    date_string = "2015-12-15"
    stock_date = time.strptime(date_string, "%Y-%m-%d")


    stock_name = "AAPL"
    filename = "{0}.csv".format(stock_name)
    stock = google_finance.GoogleFinance(stock_name, stock_date)
    stock.getHistoricalData(filename)


    col_names = []
    stock_data = []
    stock_dict = {}
    with open(filename) as fp:
        iterfp = iter(fp.readline, '\n')
        current = next(iterfp)
        col_names = current.rstrip('\n').split(",")

        for line in iterfp:
            line_data = line.rstrip('\n').split(",")
            stock_data.append(line.rstrip('\n').split(","))
            stock_dict = dict(zip(col_names, line_data))
            print(stock_dict)
            db.insertStockData(stock_name, stock_dict)



#with open('coors.csv', mode='r') as infile:
#    reader = csv.reader(infile)
#    mydict = {rows[0]:rows[1] for rows in reader}

    ######





    logging.info("Terminating execution")
