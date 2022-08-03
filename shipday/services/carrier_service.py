from shipday.carrier import CarrierRequest
from shipday.exeptions import ShipdayException
from shipday.httpclient.shipdayclient import ShipdayClient


class CarrierService:
    path = 'carriers/'

    def __init__(self, *args, api_key, **kwargs):
        self.httpclient = ShipdayClient(*args, api_key=api_key, **kwargs)

    def get_carriers(self):
        return self.httpclient.get(self.path)

    def add_carrier(self, request: CarrierRequest):
        request.verify()
        response = self.httpclient.post(self.path, request.get_body())
        if 'errorCode' in response:
            raise ShipdayException(response['errorMessage'])
        return response

    def delete_carrier(self, carrier_id: int):
        if type(carrier_id) is not int:
            raise ShipdayException('Provide a valid carrier id')
        response = self.httpclient.delete(self.path + str(carrier_id))

        return response
