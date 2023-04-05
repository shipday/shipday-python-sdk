import json
from collections import defaultdict

from shipday.exeptions.shipday_exeption import ShipdayException
from shipday.utils.verifiers import verify_instance_of, verify_none_or_instance_of


class OrderItem:
    def __init__(self, name=None, unit_price=None, quantity=None, add_ons=None, detail=None,
                 **kwargs):
        kwargs = defaultdict(lambda: None, **kwargs)
        self._name = name
        self._unit_price = unit_price or kwargs['unitPrice'] or 0
        self._quantity = quantity
        self._add_ons = add_ons or kwargs['addOns']
        self._detail = detail

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        verify_instance_of(str, value, 'OrderItem is not a name')
        self._name = value

    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        if type(value) not in (float, int) or value < 0:
            raise ShipdayException("OrderItem must have a valid price")
        self._unit_price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        if type(value) is not int or value < 1:
            raise ShipdayException("Order quantity must be a positive integer")
        self._quantity = value

    @property
    def add_ons(self):
        return self._add_ons

    @add_ons.setter
    def add_ons(self, value):
        verify_instance_of(str, value, 'add ons is not string')
        self._add_ons = value

    @property
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, value):
        verify_instance_of(str, value, 'detail is not string')
        self._detail = value

    def __repr__(self):
        return json.dumps(self.get_body())

    def verify(self):
        verify_instance_of(str, self._name, 'OrderItem must have a name of type string')
        verify_instance_of([int, float], self._unit_price, 'OrderItem must have a valid price of type int or float')
        verify_instance_of(int, self._quantity, 'Order quantity must be a positive integer')
        verify_none_or_instance_of(str, self._add_ons, 'Add ons must be String or None')
        verify_none_or_instance_of(str, self._detail, 'Details must be String or None')

    def get_body(self) -> dict:
        obj = {
            'name': self.name,
            'unitPrice': self.unit_price,
            'quantity': self.quantity
        }

        if self.add_ons is not None:
            obj['addOns'] = self.add_ons

        if self.detail is not None:
            obj['detail'] = self.detail

        return obj
