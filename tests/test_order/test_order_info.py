import pytest

from datetime import datetime

from shipday.exeptions import ShipdayException
from shipday.order import Order, Customer, Pickup, OrderItem, OrderCost, Address


class TestOrderInfo:
    """Order"""

    non_str_values = [None, 1, 1.0, [1, 2], {'a': 1}]

    customer_address = Address(street='Jefferson St', city='California', state='CA', country='USA')
    customer = Customer(name='customer', address=customer_address, email='customer@shipday.com',
                        phone_number='+1343523423')

    pickup_address = Address(street='Hacker way', city='California', state='CA', country='USA')
    pickup = Pickup(name='customer', address=pickup_address, phone_number='+134343534')

    item_1 = OrderItem(name='Pizza', unitPrice=2, quantity=7, add_ons='Extra cheese', detail='Signature Item')
    cost = OrderCost(tips=1.0, deliveryFee=5, total=20)

    @pytest.mark.parametrize('order', [
        Order(customer=customer, pickup=pickup),
        Order(customer=customer, pickup=pickup, order_items=[item_1])
    ])
    def test_order_number_missing(self, order: Order):
        """Throws exception if order number is not set::"""
        with pytest.raises(ShipdayException):
            order.verify()

    @pytest.mark.parametrize('order', [
        Order(customer=customer, pickup=pickup),
        Order(orderNumber='1234', customer=customer, pickup=pickup),
        Order(customer=customer, pickup=pickup, order_items=[item_1]),
        Order(orderNumber='1234', customer=customer, pickup=pickup, order_items=[item_1])
    ])
    @pytest.mark.parametrize('value', non_str_values)
    def test_invalid_order_number_set(self, order: Order, value):
        """Throws exception if order number is not string ::"""
        with pytest.raises(ShipdayException):
            order.order_number = value

    @pytest.mark.parametrize('order', [
        Order(orderNumber='1234', pickup=pickup),
        Order(orderNumber='1234', customer=customer, pickup=pickup),
        Order(orderNumber='1234', pickup=pickup, order_items=[item_1]),
        Order(orderNumber='1234', customer=customer, pickup=pickup, order_items=[item_1])
    ])
    @pytest.mark.parametrize('value', [
        None, 1, 1.0, [1, 2], {'a': 1}, 'abc',
        pickup, item_1, customer_address, pickup_address
    ])
    def test_invalid_customer_set(self, order: Order, value):
        """Throws exception if customer is not Customer type::"""
        with pytest.raises(ShipdayException):
            order.customer = value

    @pytest.mark.parametrize('order', [
        Order(orderNumber='1234', customer=customer),
        Order(orderNumber='1234', customer=customer, pickup=pickup),
        Order(orderNumber='1234', customer=customer, order_items=[item_1]),
        Order(orderNumber='1234', customer=customer, pickup=pickup, order_items=[item_1])
    ])
    @pytest.mark.parametrize('value', [
        None, 1, 1.0, [1, 2], {'a': 1}, 'abc',
        customer, item_1, customer_address, pickup_address
    ])
    def test_invalid_pickup_set(self, order: Order, value):
        """Throws exception if pickup is not Pickup type::"""
        with pytest.raises(ShipdayException):
            order.pickup = value

    @pytest.mark.parametrize('order', [
        Order(orderNumber='1234', customer=customer, pickup=pickup),
        Order(orderNumber='1234', customer=customer, pickup=pickup, order_items=[item_1])
    ])
    @pytest.mark.parametrize('value', [
        1, 1.0, [1, 2], {'a': 1}, 'abc',
        customer, item_1, customer_address, pickup_address
    ])
    def test_invalid_order_items_set(self, order: Order, value):
        """Throws exception if order items is neither a list of OrderItem nor None::"""
        with pytest.raises(ShipdayException):
            order.order_items = value

    @pytest.mark.parametrize('order', [
        Order(orderNumber='1234', customer=customer, pickup=pickup),
        Order(orderNumber='1234', customer=customer, pickup=pickup, order_items=[item_1])
    ])
    @pytest.mark.parametrize('value', [
        None, 1, 1.0, [1, 2], {'a': 1}, 'abc',
        customer, customer_address, pickup_address
    ])
    def test_invalid_order_items_add(self, order: Order, value):
        """Throws exception if order items is not a list of OrderItem ::"""
        with pytest.raises(ShipdayException):
            order.order_items.append(value)
            order.verify()

    @pytest.mark.parametrize('order', [
        Order(orderNumber='1234', customer=customer, pickup=pickup),
        Order(orderNumber='1234', customer=customer, pickup=pickup, expected_delivery_time=datetime.fromisoformat('2022-08-10T13:22')),
        Order(orderNumber='1234', customer=customer, pickup=pickup, order_items=[item_1]),
        Order(orderNumber='1234', customer=customer, pickup=pickup, order_items=[item_1], expected_delivery_time=datetime.fromisoformat('2022-08-10T13:22'))
    ])
    @pytest.mark.parametrize('value', [
        1, 1.0, [1, 2], {'a': 1}, '2022-08-10T13:22',
        customer, customer_address, pickup_address, item_1
    ])
    def test_invalid_expected_delivery_time_set(self, order, value):
        """Throws exception if expected_delivery_time is neither datetime.datetime nor None ::"""
        with pytest.raises(ShipdayException):
            order.expected_delivery_time = value

    @pytest.mark.parametrize('order', [
        Order(orderNumber='1234', customer=customer, pickup=pickup),
        Order(orderNumber='1234', customer=customer, pickup=pickup, expected_pickup_time=datetime.fromisoformat('2022-08-10T13:22')),
        Order(orderNumber='1234', customer=customer, pickup=pickup, order_items=[item_1]),
        Order(orderNumber='1234', customer=customer, pickup=pickup, order_items=[item_1], expected_pickup_time=datetime.fromisoformat('2022-08-10T13:22'))
    ])
    @pytest.mark.parametrize('value', [
        1, 1.0, [1, 2], {'a': 1}, '2022-08-10T13:22',
        customer, customer_address, pickup_address, item_1
    ])
    def test_invalid_expected_pickup_time_set(self, order, value):
        """Throws exception if expected_pickup_time is neither datetime.datetime nor None ::"""
        with pytest.raises(ShipdayException):
            order.expected_pickup_time = value

    @pytest.mark.parametrize('order', [
        Order(orderNumber='1234', customer=customer, pickup=pickup),
        Order(orderNumber='1234', customer=customer, pickup=pickup, expected_pickup_time=datetime.fromisoformat('2022-08-10T13:22')),
        Order(orderNumber='1234', customer=customer, pickup=pickup, order_items=[item_1]),
        Order(orderNumber='1234', customer=customer, pickup=pickup, order_items=[item_1], expected_pickup_time=datetime.fromisoformat('2022-08-10T13:22'))
    ])
    @pytest.mark.parametrize('value', [
        1, 1.0, [1, 2], {'a': 1},
        customer, customer_address, pickup_address, item_1
    ])
    def test_invalid_instruction_set(self, order, value) :
        """Throws exception if delivery_instruction is neither string nor None ::"""
        with pytest.raises(ShipdayException):
            order.delivery_instruction = value

    @pytest.mark.parametrize('order', [
        Order(orderNumber='1234', customer=customer, pickup=pickup),
        Order(orderNumber='1234', customer=customer, pickup=pickup, expected_pickup_time=datetime.fromisoformat('2022-08-10T13:22')),
        Order(orderNumber='1234', customer=customer, pickup=pickup, order_items=[item_1]),
        Order(orderNumber='1234', customer=customer, pickup=pickup, order_items=[item_1], expected_pickup_time=datetime.fromisoformat('2022-08-10T13:22')),

    ])
    @pytest.mark.parametrize('value', [
        'get there fast', 'Apt 6', '', None, 'Put in front of the door', '.....', '+01234567'
    ])
    def test_valid_instruction_set(self, order, value) :
        """Successful if delivery instruction is string or None ::"""
        order.delivery_instruction = value
        assert order.delivery_instruction == value
