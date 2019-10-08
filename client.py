################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import urllib2
import time
import json
import random
import math

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    """ Produce all of the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    # price as average of bid and ask prices
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, round(price, 3)


def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    if (price_b == 0):
        return
    # Return the ratio in 3 decimal places
    return round((float(price_a) / price_b), 3)


# Main
if __name__ == "__main__":
    price_abc = 0
    price_def = 0

    # Query the price once every N seconds.
    for _ in xrange(N):
        quotes = json.loads(urllib2.urlopen(
            QUERY.format(random.random())).read())

        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            print "Quoted %s at (bid:%s, ask:%s, price:%s)" % (
                stock, bid_price, ask_price, price)
            if stock == "ABC":
                price_abc = price
            else:
                price_def = price
        print "Ratio %s" % getRatio(price_abc, price_def)
