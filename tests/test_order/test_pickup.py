import pytest

from shipday.exceptions import ShipdayException
from shipday.order import Pickup, Address


class TestPickup:
    """Pickup Test"""
    non_str_values = [None, 1, 1.0, [1, 2], {'a': 1}]
    address = Address(street='Jefferson St', city='California', state='CA', country='USA')

    @pytest.mark.parametrize('pickup', [
        Pickup(address=address, phone_number='+1343523423'),
    ])
    def test_name_missing(self, pickup: Pickup):
        """Throws exception if name is not set ::"""
        with pytest.raises(ShipdayException):
            pickup.verify()

    @pytest.mark.parametrize('pickup', [
        Pickup(name='My Pickup Place', phone_number='+1343523423'),
    ])
    def test_address_missing(self, pickup: Pickup):
        """Throws exception if address is not set ::"""
        with pytest.raises(ShipdayException):
            pickup.verify()

    @pytest.mark.parametrize('pickup', [
        Pickup(address=address, phone_number='+1343523423'),
        Pickup(name='customer', address=address, phone_number='+1343523423')
    ])
    @pytest.mark.parametrize('value', non_str_values)
    def test_invalid_name_set(self, pickup: Pickup, value):
        """Throws exception if name is not String ::"""
        with pytest.raises(ShipdayException):
            pickup.name = value

    @pytest.mark.parametrize('pickup', [
        Pickup(name='customer', phone_number='+1343523423'),
        Pickup(name='customer', address=address, phone_number='+1343523423')
    ])
    @pytest.mark.parametrize('value', non_str_values + ['adfsas'])
    def test_invalid_address_set(self, pickup: Pickup, value):
        """Throws exception if Address is not Address type ::"""
        with pytest.raises(ShipdayException):
            pickup.address = value

    @pytest.mark.parametrize('pickup', [
        Pickup(name='customer', address=address),
        Pickup(name='customer', address=address, phone_number='+1343523423')
    ])
    @pytest.mark.parametrize('value', non_str_values)
    def test_invalid_phone_number_set(self, pickup: Pickup, value):
        """Throws exception if phone number is not String ::"""
        with pytest.raises(ShipdayException):
            pickup.phone_number = value

