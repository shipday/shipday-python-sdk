import pytest

from shipday.exceptions import ShipdayException
from shipday.order import Customer, Address


class TestCustomer:
    """Customer Object"""
    non_str_values = [None, 1, 1.0, [1, 2], {'a': 1}]
    address = Address(street='Jefferson St', city='California', state='CA', country='USA')

    @pytest.mark.parametrize('customer', [
        Customer(address=address, email='customer@shipday.com', phone_number='+1343523423'),
    ])
    def test_name_missing(self, customer: Customer):
        """Throws exception if name is not set ::"""
        with pytest.raises(ShipdayException):
            customer.verify()

    @pytest.mark.parametrize('customer', [
        Customer(name='customer', email='customer@shipday.com', phone_number='+1343523423'),
    ])
    def test_address_missing(self, customer: Customer):
        """Throws exception if address is not set ::"""
        with pytest.raises(ShipdayException):
            customer.verify()

    @pytest.mark.parametrize('customer', [
        Customer(name='customer', email='customer@shipday.com', phone_number='+1343523423'),
    ])
    def test_phone_number_missing(self, customer: Customer):
        """Throws exception if phone number is not set ::"""
        with pytest.raises(ShipdayException):
            customer.verify()

    @pytest.mark.parametrize('customer', [
        Customer(address=address, email='customer@shipday.com', phone_number='+1343523423'),
        Customer(name='customer', address=address, email='customer@shipday.com', phone_number='+1343523423')
    ])
    @pytest.mark.parametrize('value', non_str_values)
    def test_invalid_name_set(self, customer: Customer, value):
        """Throws exception if name is not String ::"""
        with pytest.raises(ShipdayException):
            customer.name = value

    @pytest.mark.parametrize('customer', [
        Customer(name='customer', email='customer@shipday.com', phone_number='+1343523423'),
        Customer(name='customer', address=address, email='customer@shipday.com', phone_number='+1343523423')
    ])
    @pytest.mark.parametrize('value', non_str_values + ['adfsas'])
    def test_invalid_address_set(self, customer: Customer, value):
        """Throws exception if Address is not Address type ::"""
        with pytest.raises(ShipdayException):
            customer.address = value

    @pytest.mark.parametrize('customer', [
        Customer(name='customer', email='customer@shipday.com', phone_number='+1343523423'),
        Customer(name='customer', address=address, email='customer@shipday.com', phone_number='+1343523423')
    ])
    @pytest.mark.parametrize('value', [
        address,
        Address(street='Jefferson St', city='California', state='CA', country='USA', latitude=1.0, longitude=1.0),
    ])
    def test_valid_address_set(self, customer: Customer, value):
        """Valid Address set ::"""
        customer.address = value
        assert customer.address == value

    @pytest.mark.parametrize('customer', [
        Customer(name='customer', address=address, phone_number='+1343523423'),
        Customer(name='customer', address=address, email='customer@shipday.com', phone_number='+1343523423')
    ])
    @pytest.mark.parametrize('value', [1, 1.0])
    def test_invalid_email_set(self, customer: Customer, value):
        """Throws exception if email is not String or None ::"""
        with pytest.raises(ShipdayException):
            customer.email = value

    @pytest.mark.parametrize('customer', [
        Customer(name='customer', address=address, email='customer@shipday.com'),
        Customer(name='customer', address=address, email='customer@shipday.com', phone_number='+1343523423')
    ])
    @pytest.mark.parametrize('value', non_str_values)
    def test_invalid_phone_number_set(self, customer: Customer, value):
        """Throws exception if phone number is not String ::"""
        with pytest.raises(ShipdayException):
            customer.phone_number = value
