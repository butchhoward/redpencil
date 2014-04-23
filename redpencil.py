#!/usr/bin/env python
import unittest
from mock import patch, MagicMock, Mock

class Item(object):
	def __init__(self):
		self.price = 10.00
		self.reduced_price = 0.0
		self.red_pencil = False

	def get_price(self):
		return self.price

	def reduce_price(self, percent):
		self.reduced_price = self.price * (1.0 - (percent/100.0))
		if percent in range(5,31):
			self.red_pencil = True

	def get_reduced_price(self):
		return self.reduced_price

 	def get_red_penciled(self):
		return self.red_pencil



class TestPriceChange(unittest.TestCase):

	def setUp(self):
		self.item = Item()

	def test_get_price(self):
		self.assertEqual(self.item.get_price(), 10.00)

	def test_price_reduced_5percent(self):
		self.item.reduce_price(5)
		self.assertEqual( self.item.get_reduced_price(), 10.00 * 0.95)

	def test_is_redpencil_when_reduced_price_between_5_and_30_percent(self):
		self.item.reduce_price(30)
		self.assertTrue(self.item.get_red_penciled())

	def test_is_redpencil_when_price_is_reduced_by_5_percent(self):
		self.item.reduce_price(5)
		self.assertTrue(self.item.get_red_penciled())

	def test_is_not_redpencel_when_priced_is_reduced_by_4_percent(self):
		self.item.reduce_price(4)
		self.assertFalse(self.item.get_red_penciled())

	def test_is_not_redpencil_when_price_is_reduced_by_35_percent(self):
		self.item.reduce_price(35)
		self.assertFalse(self.item.get_red_penciled())



if __name__ == '__main__':
    unittest.main()