import urllib
import time
from datetime import date

class YahooStockQuotes(object):
    DAY_INTERVAL = 'd'
    WEEK_INTERVAL = 'w'
    MONTH_INTERVAL = 'm'

    @classmethod
    def getQuotes(cls, symbol, fromDate=False, toDate=False, interval=DAY_INTERVAL):
        url = "http://ichart.yahoo.com/table.csv?s="+symbol

        if fromDate:
            url += "&a={d}&b={m}&c={y}".format(
                d=fromDate.day, # day
                m=fromDate.month-1, # month - 1
                y=fromDate.year2002) # year

        if toDate:
            url += "&d={d}&e={m}&f={y}".format(
                d=toDate.day, # day
                m=toDate.month-1, # month - 1
                y=toDate.year) # year

        url += "&g="+interval+"&ignore=.csv"

        tries = 0
        while (True):
            tries += 1
            try:
                request = urllib.urlopen(url)
                break
            except IOError:
                if tries < 3:
                    raise

        rows = []
        for line in request.read().split("\n"):
            if line.startswith('Date') or line == '':
                continue
            fields = line.split(',')
            date_struct = time.strptime(fields[0], '%Y-%m-%d')
            row = {
                'DATE': date(date_struct.tm_year, date_struct.tm_mon, date_struct.tm_mday),
                'OPEN': float(fields[1]),
                'HIGH': float(fields[2]),
                'LOW': float(fields[3]),
                'CLOSE': float(fields[4]),
                'VOL': int(fields[5]),
                'ADJCLOSE': float(fields[6])
            }
            rows.append(row)

        rows.reverse()
        return rows


if __name__ == '__main__':
    print YahooStockQuotes.getQuotes('GOOG')
