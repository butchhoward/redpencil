#!/usr/bin/env python
import unittest
from mock import patch, MagicMock, Mock

from datetime import date


class SaleItem(object):
	def __init__(self, price=None):
		self.Price = price
		self.RedPencilDiscount = False

	def change_price_to(self, price):
		reduction = 1- (price / self.Price)
		if reduction >= 0.05 and reduction <= 0.30:
			self.RedPencilDiscount = True
		self.Price = price


	def is_red_pencil_discount(self):
		return self.RedPencilDiscount
		

class TestRedPencil(unittest.TestCase):
	def setUp(self):
		self.item100 = SaleItem(100.00)

	def test_can_create_saleitem_with_given_price(self):
		self.assertEqual(self.item100.Price, 100.00)

	def test_sale_item_price_defaults_to_none(self):
		item = SaleItem()
		self.assertEqual(item.Price, None)

	def test_can_change_price_to_given_value(self):
		self.item100.change_price_to(75.00)
		self.assertEqual(self.item100.Price, 75.00)

	def test_redpencil_discount_is_true_when_price_reduced_5_percent(self):
		self.item100.change_price_to(95.00)
		self.assertTrue(self.item100.is_red_pencil_discount())

	def test_redpencil_discount_is_false_when_price_reduced_4_percent(self):
		self.item100.change_price_to(96.00)
		self.assertFalse(self.item100.is_red_pencil_discount())

	def test_redpencil_discount_is_false_when_priced_reduced_31_percent(self):
		self.item100.change_price_to(69.00)
		self.assertFalse(self.item100.is_red_pencil_discount())

	#this is failing because the mock is not quite right
	@patch("datetime.date.today")
	def test_price_change_date_defaults_at_today(self, mocktoday):
		currentday = datetime.date(2014,04,22)
		mocktoday.return_value = currentday
		self.assertEqual(self.item100.PriceChangeDate, currentday )




if __name__ == '__main__':
    unittest.main()