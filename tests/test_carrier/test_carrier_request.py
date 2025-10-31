import pytest
from shipday.exceptions.shipday_exception import ShipdayException
from shipday.carrier.carrier_request import CarrierRequest


class TestCarrierRequest:
    """Carrier Insertion Request"""
    non_str_values = [None, 1, 1.0, [1, 2], {'a': 1}]

    @pytest.mark.parametrize('carrier_request', [
        CarrierRequest(email='ca@shipday.com', phone_number='+139024523')
    ])
    def test_name_missing(self, carrier_request: CarrierRequest):
        """Throws exception if name is not set ::"""
        with pytest.raises(ShipdayException):
            carrier_request.verify()

    @pytest.mark.parametrize('carrier_request', [
        CarrierRequest(name='My Carrier', phone_number='+139024523')
    ])
    def test_email_missing(self, carrier_request: CarrierRequest):
        """Throws exception if email is not set ::"""
        with pytest.raises(ShipdayException):
            carrier_request.verify()

    @pytest.mark.parametrize('carrier_request', [
        CarrierRequest(name='My Carrier', email='ca@shipday.com')
    ])
    def test_phone_number_missing(self, carrier_request: CarrierRequest):
        """Throws exception if phone number is not set ::"""
        with pytest.raises(ShipdayException):
            carrier_request.verify()

    @pytest.mark.parametrize('carrier_request', [
        CarrierRequest(email='ca@shipday.com', phone_number='+139024523'),
        CarrierRequest(name='My Carrier', email='ca@shipday.com', phone_number='+139024523')
    ])
    @pytest.mark.parametrize('value', non_str_values)
    def test_invalid_name_set(self, carrier_request: CarrierRequest, value):
        """Throws exception if name is not a String ::"""
        with pytest.raises(ShipdayException):
            carrier_request.name = value
            carrier_request.verify()

    @pytest.mark.parametrize('carrier_request', [
        CarrierRequest(name='My Carrier', phone_number='+139024523'),
        CarrierRequest(name='My Carrier', email='ca@shipday.com', phone_number='+139024523')
    ])
    @pytest.mark.parametrize('value', non_str_values)
    def test_invalid_email_set(self, carrier_request: CarrierRequest, value):
        """Throws exception if email is not a String ::"""
        with pytest.raises(ShipdayException):
            carrier_request.email = value
            carrier_request.verify()

    @pytest.mark.parametrize('carrier_request', [
        CarrierRequest(name='My Carrier', phone_number='+139024523'),
        CarrierRequest(name='My Carrier', email='ca@shipday.com', phone_number='+139024523')
    ])
    @pytest.mark.parametrize('value', non_str_values)
    def test_invalid_phone_number_set(self, carrier_request: CarrierRequest, value):
        """Throws exception if phone_number is not a String ::"""
        with pytest.raises(ShipdayException):
            carrier_request.phone_number = value
            carrier_request.verify()
