from shipday.exeptions import ShipdayException
from shipday.services import OrderService, CarrierService, OnDemandDeliveryService


class Shipday:
    def __init__(self, *args, api_key, **kwargs):
        self.__api_key__ = api_key
        self.__verify_api_key()
        self.OrderService = OrderService(api_key=api_key)
        self.CarrierService = CarrierService(api_key=api_key)
        self.OnDemandDeliveryService = OnDemandDeliveryService(api_key=api_key)

    def __verify_api_key(self):
        if self.__api_key__ is None or len(self.__api_key__) < 10:
            raise ShipdayException('Invalid API key')
