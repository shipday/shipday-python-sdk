import json
from collections import defaultdict

from shipday.order.address import Address
from shipday.utils.verifiers import verify_instance_of


class Restaurant:
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
        verify_instance_of(str, value, "Restaurant name is not a string")
        self._name = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        verify_instance_of(Address, value, "Restaurant is not of Restaurant type")
        self._address = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        verify_instance_of(str, value, "Phone number is not a string")
        self._phone_number = value

    def __repr__(self):
        return json.dumps(self.get_body())

    def verify(self):
        verify_instance_of(str, self.name, "Restaurant must have a name")
        verify_instance_of(Address, self.address, "Restaurant must be of type Address")

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
