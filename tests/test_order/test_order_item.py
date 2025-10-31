import pytest

from shipday.exceptions import ShipdayException
from shipday.order import OrderItem


class TestOrderItem:
    """Order Item Test"""

    non_str_values = [None, 1, 1.0, [1, 2], {'a': 1}]
    not_positive_numbers = [None, -1, 'abc', [1], {'a': 1}]
    not_positive_integers = not_positive_numbers + [3.5]

    @pytest.mark.parametrize('order_item', [
        OrderItem(unitPrice=1, quantity=4),
        OrderItem(unitPrice=3.5, quantity=2),
        OrderItem(unitPrice=1, quantity=5, add_ons='Extra cheese'),
        OrderItem(unitPrice=2, quantity=7, add_ons='Extra cheese', detail='Signature Item'),
    ])
    def test_name_missing(self, order_item: OrderItem):
        """Throws exception if name is not set ::"""
        with pytest.raises(ShipdayException):
            order_item.verify()


    @pytest.mark.parametrize('order_item', [
        OrderItem(name='Pizza', unitPrice=1),
        OrderItem(name='Pizza', unitPrice=3.5),
        OrderItem(name='Pizza', unitPrice=1, add_ons='Extra cheese'),
        OrderItem(name='Pizza', unitPrice=2, add_ons='Extra cheese', detail='Signature Item'),
    ])
    def test_quantity_missing(self, order_item: OrderItem):
        """Throws exception if quantity is not set ::"""
        with pytest.raises(ShipdayException):
            order_item.verify()

    @pytest.mark.parametrize('order_item', [
        OrderItem(unitPrice=2, quantity=7),
        OrderItem(name='Pizza', unitPrice=2, quantity=7),
        OrderItem(name='Pizza', unitPrice=2, quantity=7, add_ons='Extra cheese'),
        OrderItem(name='Pizza', unitPrice=2, quantity=7, add_ons='Extra cheese', detail='Signature Item')
    ])
    @pytest.mark.parametrize('value', non_str_values)
    def test_invalid_name_set(self, order_item: OrderItem, value):
        """Throws exception if name is not a String ::"""
        with pytest.raises(ShipdayException):
            order_item.name = value

    @pytest.mark.parametrize('order_item', [
        OrderItem(name='Pizza', quantity=7),
        OrderItem(name='Pizza', unitPrice=2, quantity=7),
        OrderItem(name='Pizza', unitPrice=2, quantity=7, add_ons='Extra cheese'),
        OrderItem(name='Pizza', unitPrice=2, quantity=7, add_ons='Extra cheese', detail='Signature Item')
    ])
    @pytest.mark.parametrize('value', not_positive_numbers)
    def test_invalid_price_set(self, order_item: OrderItem, value):
        """Throws exception if price is not a positive number or zero ::"""
        with pytest.raises(ShipdayException):
            order_item.unit_price = value

    @pytest.mark.parametrize('order_item', [
        OrderItem(name='Pizza', unitPrice=2),
        OrderItem(name='Pizza', unitPrice=2, quantity=7),
        OrderItem(name='Pizza', unitPrice=2, quantity=7, add_ons='Extra cheese'),
        OrderItem(name='Pizza', unitPrice=2, quantity=7, add_ons='Extra cheese', detail='Signature Item')
    ])
    @pytest.mark.parametrize('value', not_positive_integers + [0, 0.0])
    def test_invalid_quantity_set(self, order_item: OrderItem, value):
        """Throws exception if quantity is not a non-zero positive integer::"""
        with pytest.raises(ShipdayException):
            order_item.quantity = value

    @pytest.mark.parametrize('order_item', [
        OrderItem(name='Pizza', unitPrice=2, quantity=7),
        OrderItem(name='Pizza', unitPrice=2, quantity=7, add_ons='Extra cheese'),
        OrderItem(name='Pizza', unitPrice=2, quantity=7, add_ons='Extra cheese', detail='Signature Item')
    ])
    @pytest.mark.parametrize('value', non_str_values)
    def test_invalid_addons_set(self, order_item: OrderItem, value):
        """Throws exception if addons is not a string ::"""
        with pytest.raises(ShipdayException):
            order_item.add_ons = value

    @pytest.mark.parametrize('order_item', [
        OrderItem(name='Pizza', unitPrice=2, quantity=7),
        OrderItem(name='Pizza', unitPrice=2, quantity=7, add_ons='Extra cheese'),
        OrderItem(name='Pizza', unitPrice=2, quantity=7, add_ons='Extra cheese', detail='Signature Item')
    ])
    @pytest.mark.parametrize('value', non_str_values)
    def test_invalid_detail_set(self, order_item: OrderItem, value):
        """Throws exception if detail is not a string ::"""
        with pytest.raises(ShipdayException):
            order_item.detail = value
