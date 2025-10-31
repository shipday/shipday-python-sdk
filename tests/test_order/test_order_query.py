from datetime import datetime

import pytest

from itertools import combinations

from shipday.exceptions import ShipdayException
from shipday.order import OrderQuery, Customer, Pickup, OrderItem, OrderCost, Address, OrderStatus


def get_test_order_queries() -> list:
    params = {
        'start_time': datetime.fromisoformat('2022-06-10T13:22'),
        'end_time': datetime.fromisoformat('2022-07-10T20:22'),
        'order_status': OrderStatus.ACTIVE,
        'start_cursor': 1,
        'end_cursor': 20
    }
    return [OrderQuery(**{key: params[key] for key in combination})
            for r in range(len(params) + 1)
            for combination in combinations(params, r)]


class TestOrderQuery():
    """Order Query"""

    non_str_values = [None, 1, 1.0, [1, 2], {'a': 1}]

    customer_address = Address(street='Jefferson St', city='California', state='CA', country='USA')
    customer = Customer(name='customer', address=customer_address, email='customer@shipday.com',
                        phone_number='+1343523423')

    pickup_address = Address(street='Hacker way', city='California', state='CA', country='USA')
    pickup = Pickup(name='customer', address=pickup_address, phone_number='+134343534')

    item_1 = OrderItem(name='Pizza', unitPrice=2, quantity=7, add_ons='Extra cheese', detail='Signature Item')
    cost = OrderCost(tips=1.0, deliveryFee=5, total=20)

    @pytest.mark.parametrize('query', get_test_order_queries())
    @pytest.mark.parametrize('value', [
        1, 1.0, [1, 2], {'a': 1}, '2022-08-10T13:22',
        customer, customer_address, pickup_address, item_1
    ])
    def test_invalid_start_time_set(self, query: OrderQuery, value):
        """Throws exception if start_time is neither datetime.datetime nor None::"""
        with pytest.raises(ShipdayException):
            query.start_time = value

    @pytest.mark.parametrize('query', get_test_order_queries())
    @pytest.mark.parametrize('value', [
        1, 1.0, [1, 2], {'a': 1}, '2022-08-10T13:22',
        customer, customer_address, pickup_address, item_1
    ])
    def test_invalid_end_time_set(self, query: OrderQuery, value):
        """Throws exception if end_time is neither datetime.datetime nor None::"""
        with pytest.raises(ShipdayException):
            query.end_time = value

    @pytest.mark.parametrize('query', get_test_order_queries())
    @pytest.mark.parametrize('value', [
        -4, 1, 1.0, [1, 2], {'a': 1}, '2022-08-10T13:22',
        customer, customer_address, pickup_address, item_1
    ])
    def test_invalid_order_status_set(self, query: OrderQuery, value):
        """Throws exception if order_status is neither datetime.datetime nor None::"""
        with pytest.raises(ShipdayException):
            query.order_status = value

    @pytest.mark.parametrize('query', get_test_order_queries())
    @pytest.mark.parametrize('value', [
        -4, 1, 1.0, [1, 2], {'a': 1}, '2022-08-10T13:22',
        customer, customer_address, pickup_address, item_1
    ])
    def test_invalid_order_status_set(self, query: OrderQuery, value):
        """Throws exception if end_time is neither datetime.datetime nor None::"""
        with pytest.raises(ShipdayException):
            query.order_status = value

    @pytest.mark.parametrize('query', get_test_order_queries())
    @pytest.mark.parametrize('value', [
        1.0, [1, 2], {'a': 1}, '2022-08-10T13:22',
        customer, customer_address, pickup_address, item_1
    ])
    def test_invalid_start_cursor_set(self, query: OrderQuery, value):
        """Throws exception if start_cursor is neither a positive integer or zero nor None::"""
        with pytest.raises(ShipdayException):
            query.start_cursor = value

    @pytest.mark.parametrize('query', get_test_order_queries())
    @pytest.mark.parametrize('value', [
        1.0, [1, 2], {'a': 1}, '2022-08-10T13:22',
        customer, customer_address, pickup_address, item_1
    ])
    def test_invalid_end_cursor_set(self, query: OrderQuery, value):
        """Throws exception if end_cursor is neither a positive integer or zero nor None::"""
        with pytest.raises(ShipdayException):
            query.end_cursor = value
