import unittest
from client import getDataPoint, getRatio


class ClientTest(unittest.TestCase):

    # Test for prices as average of bid and ask
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Assertions ------------ """
        for quote in quotes:
            price = round(
                ((quote['top_ask']['price'] + quote['top_bid']['price']) / 2), 3)
            self.assertEqual(getDataPoint(quote),
                             (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], price))

    # Test
    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Assertions ------------ """
        # Can not find a need for this test.

    #  Test getRatio function
    def test_getRatio(self):
        self.assertEqual(getRatio(34, 42), 0.81)
        self.assertEqual(getRatio(119.21, 121.68), 0.98)

    # Test getRatio function with B as zero (0)
    def test_getRatio_B_zero(self):
        self.assertEqual(getRatio(3, 0), None)


if __name__ == '__main__':
    unittest.main()
