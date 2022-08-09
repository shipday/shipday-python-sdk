import json
from datetime import datetime

from shipday.exeptions import ShipdayException
from shipday.order.order_status import OrderStatus
from shipday.utils.verifiers import verify_none_or_instance_of
from shipday.order.customer import Customer
from shipday.order.pickup import Pickup
from shipday.order.order_item import OrderItem
from shipday.order.order_cost import OrderCost
from shipday.order.address import Address


class OrderQuery:

    customer_address = Address(street='Jefferson St', city='California', state='CA', country='USA')
    customer = Customer(name='customer', address=customer_address, email='customer@shipday.com',
                        phone_number='+1343523423')

    pickup_address = Address(street='Hacker way', city='California', state='CA', country='USA')
    pickup = Pickup(name='customer', address=pickup_address, phone_number='+134343534')

    item_1 = OrderItem(name='Pizza', unitPrice=2, quantity=7, add_ons='Extra cheese', detail='Signature Item')
    cost = OrderCost(tips=1.0, deliveryFee=5, total=20)
    def __init__(self, *args,
                 start_time: datetime = None, end_time: datetime = None, order_status: str = None,
                 start_cursor=None, end_cursor=None,
                 **kwargs):
        self._start_time = start_time
        self._end_time = end_time
        self._order_status = order_status
        self._start_cursor = start_cursor
        self._end_cursor = end_cursor

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        verify_none_or_instance_of(datetime, value, "Start time is not of type " + str(datetime))
        self._start_time = value

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        verify_none_or_instance_of(datetime, value, "End time is not of type " + str(datetime))
        self._end_time = value

    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        verify_none_or_instance_of(str, value, "Invalid order status")
        if value not in OrderStatus._list_:
            raise ShipdayException("Invalid order status")
        self._order_status = value

    @property
    def start_cursor(self):
        return self._start_cursor

    @start_cursor.setter
    def start_cursor(self, value):
        verify_none_or_instance_of(int, value, "Start cursor is not integer")
        self._start_cursor = value

    @property
    def end_cursor(self):
        return self._end_cursor

    @end_cursor.setter
    def end_cursor(self, value):
        verify_none_or_instance_of(int, value, "End cursor is not integer")
        self._end_cursor = value

    def __repr__(self):
        return json.dumps(self.get_body())

    def verify(self):
        verify_none_or_instance_of(datetime, self._start_time, "Start time is not of type " + str(datetime))
        verify_none_or_instance_of(datetime, self._end_time, "End time is not of type " + str(datetime))
        verify_none_or_instance_of(str, self._order_status, "Invalid order status")
        if self._order_status not in OrderStatus.list_:
            raise ShipdayException("Invalid order status")
        verify_none_or_instance_of(int, self._start_cursor, "Start cursor is not integer")
        verify_none_or_instance_of(int, self._end_cursor, "End cursor is not integer")

    def get_body(self):
        obj = dict()
        if self.start_time is not None:
            obj['startTime'] = self.start_time.isoformat()
        if self.end_time is not None:
            obj['endTime'] = self.end_time.isoformat()
        if self.order_status is not None:
            obj['orderStatus'] = self.order_status
        if self.start_cursor is not None:
            obj['startCursor'] = self.start_cursor
        if self.end_cursor is not None:
            obj['endCursor'] = self.end_cursor

        return obj
