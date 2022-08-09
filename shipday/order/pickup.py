import json
from collections import defaultdict

from shipday.order.address import Address
from shipday.utils.verifiers import verify_instance_of, verify_none_or_instance_of


class Pickup:
    def __init__(self, *args,
                 name: str = None, address: Address = None, phone_number: str = None,
                 **kwargs):
        kwargs = defaultdict(lambda: None, **kwargs)
        self._name = name or kwargs['restaurantName']
        self._address = address
        self._phone_number = phone_number or kwargs['restaurantPhoneNumber']
        self.__address_line = kwargs['restaurantAddress']

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        verify_instance_of(str, value, 'Pickup name is not a string')
        self._name = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        verify_instance_of(Address, value, 'Pickup address is not of Address type')
        self._address = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        verify_instance_of(str, value, 'Pickup Phone number is not a string')
        self._phone_number = value

    def __repr__(self):
        return json.dumps(self.get_body())

    def verify(self):
        verify_instance_of(str, self._name, 'Pickup must have a name')
        verify_instance_of(Address, self._address, 'Pickup must be of type Address')
        verify_none_or_instance_of(str, self._phone_number, 'Pickup phone number must be String or None')

    def get_body(self) -> dict:
        obj = {
            'restaurantName': self.name,
            'restaurantAddress': self.__address_line or (
                self.address.get_single_line() if self._address is not None else None),
            'pickup': self.address.get_breakdown() if self._address is not None else None,
        }
        if self.phone_number is not None:
            obj['restaurantPhoneNumber'] = self.phone_number
        return obj
