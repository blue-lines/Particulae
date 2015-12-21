__author__ = 'Julien Heck'

"""
google_finance.py
GoogleFinance class
"""


import urllib.request
import datetime
import logging

class GoogleFinance:
    """
    Connect to google finance url and download stock data
    """

    def __init__(self, symbol=None, start_date=None):
        """
        Class constructor
        :param symbol: string of stock symbol
        :param start_date: struct_time object, start date of the stock data
        :return:
        """
        self.symbol = symbol.upper()
        self.start_date = start_date
        # Create URL based on parameters symbol and start_date
        self.base_url = "http://www.google.com/finance/historical?q="
        logging.info("GoogleFinance instance created for {0} stocks starting from {1}-{2}-{3}"
                     .format(self.symbol, self.start_date.tm_year, self.start_date.tm_mon, self.start_date.tm_mday))

    def getHistoricalData(self, file_name=None):
        """
        :param file_name: string of file name of output data
        :return: write data retrieved from base_url to filename
        """
        today_date = datetime.datetime.today().date()
        success = True

        # Create URL string based on symbol, start date and today's date
        try:
            start_date_str = "{0}-{1}-{2}".format(self.start_date.tm_year, self.start_date.tm_mon, self.start_date.tm_mday)
            url_str = (self.base_url + self.symbol + "&startdate="
                   + start_date_str
                   + "&enddate={}".format(today_date) + "&output=csv")
            logging.info("Accessing url: {0}".format(url_str))
        # Connect to URL and download data
            url_data = urllib.request.urlopen(url_str)
            csv = (url_data.read()).decode("utf-8-sig").encode("utf-8")
        except:
            message = "Failed to connect to URL"
            logging.error(message)
            success = False

        # Write output to file if file name is not None
        if file_name is not None:
            try:
                parse_file = open(file_name, "w")
                str_response = csv.decode('utf-8')
                print(str_response, file=parse_file)
                parse_file.close()
            except:
                message = "Failed to open/write to file: {0}".format(file_name)
                logging.error(message)
                success = False
        return success