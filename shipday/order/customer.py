import json
from collections import defaultdict

from shipday.order.address import Address
from shipday.utils.verifiers import verify_instance_of, verify_none_or_instance_of


class Customer:
    def __init__(self, *arg,
                 name: str = None, address: Address = None, email: str = None, phone_number: str = None,
                 **kwargs):
        kwargs = defaultdict(lambda: None, **kwargs)
        self._name = name or kwargs['customerName']
        self._address = address
        self._email = email or kwargs['customerEmail']
        self._phone_number = phone_number or kwargs['customerPhoneNumber']
        self._address_line = kwargs['customerAddress']

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        verify_instance_of(str, value, "Name is not String")
        self._name = value

    @property
    def address(self) -> Address:
        return self._address

    @address.setter
    def address(self, value: Address):
        verify_instance_of(Address, value, "Address is not String")
        self._address = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        verify_instance_of(str, value, "Email is not String")
        self._email = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        verify_instance_of(str, value, "Phone number is not String")
        self._phone_number = value

    def __repr__(self):
        return json.dumps(self.get_body())

    def verify(self) -> None:
        verify_instance_of(str, self.name, "Customer must have a name")
        verify_instance_of(Address, self.address, "Customer must have a Address")
        verify_instance_of(str, self.phone_number, "Customer must have a phone number")
        verify_none_or_instance_of(str, self.email, "Customer email must be a String or None")

    def get_body(self) -> dict:
        return {
            'customerName': self.name,
            'customerAddress': self._address_line or (
                self.address.get_single_line() if self._address is not None else None),
            'dropoff': self.address.get_breakdown() if self._address is not None else None,
            'customerEmail': self.email,
            'customerPhoneNumber': self.phone_number
        }
