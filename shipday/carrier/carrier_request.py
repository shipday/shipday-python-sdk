from collections import defaultdict

from shipday.exeptions.shipday_exeption import ShipdayException
from shipday.utils.verifiers import verify_instance_of


class CarrierRequest:
    def __init__(self,
                 name:str = None, email:str = None, phone_number:str = None
                 , **kwargs):
        kwargs = defaultdict(lambda: None, **kwargs)
        self._name = name
        self._email = email
        self._phone_number = phone_number

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        verify_instance_of(str, value, "Carrier name is not a string")
        self._name = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        verify_instance_of(str, value, "Carrier email is not a string")
        self._email = value

    @property
    def phone_number(self) -> str:
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value: str) -> None:
        verify_instance_of(str, value, "Carrier phone number is not a string")
        self._phone_number = value

    def verify(self) -> None:
        if self.name is None:
            raise ShipdayException('Carrier must have a name')
        if self.email is None:
            raise ShipdayException('Carrier must have an email')
        if self.phone_number is None:
            raise ShipdayException('Carrier must have a phone number')

    def get_body(self) -> dict:
        self.verify()
        return {
            'name': self.name,
            'phoneNumber': self.phone_number,
            'email': self.email
        }
