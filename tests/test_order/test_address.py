import pytest

from shipday.exceptions import ShipdayException
from shipday.order import Address


class TestAddress:
    @pytest.mark.parametrize('address, is_valid', [
        (Address(street='Jefferson St', city='California', state='CA', country='USA'), True),
        (Address(street='Jefferson St', city='California', state='CA', country='USA', latitude=1.0, longitude=1.0), True),
        (Address(street='Jefferson St', city='California', state='CA', country='USA', latitude=1.0), False),
        (Address(street='Jefferson St', city='California', state='CA', country='USA', longitude=1.0), False),
        (Address(street='Jefferson St', city='California', state='CA', country='USA', latitude=300, longitude=45.0), False),
        (Address(street='Jefferson St', city='California', state='CA', country='USA', latitude=1.0, longitude=300), False)
    ])
    def test_coordinates(self, address: Address, is_valid: bool):
        if is_valid:
            address.verify()
        else:
            with pytest.raises(ShipdayException):
                address.verify()

