from shipday.utils.verifiers import verify_instance_of, verify_none_or_instance_of
from shipday.exeptions.shipday_exeption import ShipdayException
from shipday.httpclient.shipdayclient import ShipdayClient
from shipday.order.address import Address
from datetime import datetime


class OnDemandDeliveryService:
    PATH = 'on-demand/'
    SERVICES_PATH = PATH + 'services'
    ESTIMATE_PATH = PATH + 'estimate/{order_id}'
    AVAILABILITY_PATH = 'third-party/availability'
    ASSIGN_PATH = PATH + 'assign'
    DETAILS_PATH = PATH + 'details/{order_id}'
    CANCEL_PATH = PATH + 'cancel/{order_id}'

    def __init__(self, *args, api_key, **kwargs):
        self.httpclient = ShipdayClient(*args, api_key=api_key, **kwargs)

    def get_services(self) -> list:
        res = self.httpclient.get(self.SERVICES_PATH)
        return res

    def get_active_services(self) -> list:
        services = self.get_services()
        active_services = [tp['name'] for tp in services if tp[tp['name']] is True]
        return active_services

    def estimate(self, order_id: int) -> dict:
        verify_instance_of(int, order_id, 'Order id must be integer')
        res = self.httpclient.get(self.ESTIMATE_PATH.format_map({'order_id': order_id}))
        return res

    def check_availability(self, *args, pickup_address: Address, delivery_address: Address,
                           delivery_time: datetime = None) -> dict:
        verify_instance_of(Address, pickup_address, 'Pickup address must be of type {}'.format(Address))
        verify_instance_of(Address, delivery_address, 'Delivery address must be of type {}'.format(Address))
        verify_none_or_instance_of(datetime, delivery_time, 'Delivery Time must be of type {}'.format(datetime))

        data = {
            'pickupAddress': pickup_address.get_single_line(),
            'deliveryAddress': delivery_address.get_single_line()
        }
        if delivery_time is not None:
            data['deliveryTime'] = delivery_time.isoformat()

        res = self.httpclient.post(self.AVAILABILITY_PATH, data)
        return res

    def assign(self, *args, order_id:int, service_name: str, tip: float = 0, estimate_reference=None, **kwargs) -> dict:
        verify_instance_of(int, order_id, 'Order id must be integer')
        verify_instance_of([int, float], tip, 'Tip must be a number')
        verify_none_or_instance_of(str, estimate_reference, 'Invalid Reference')

        if service_name not in self.get_active_services():
            raise ShipdayException('Service not available')
        data = {
            'name': service_name,
            'orderId': order_id,
            'tip': tip
        }
        if estimate_reference is not None:
            data['estimateReference'] = estimate_reference

        res = self.httpclient.post(self.ASSIGN_PATH, data)
        return res

    def cancel(self, order_id: int) -> dict:
        verify_instance_of(int, order_id, 'Order id must be integer')
        res = self.httpclient.post(self.CANCEL_PATH.format_map({'order_id': order_id}), {})
        return res

    def get_details(self, order_id: int) -> dict:
        verify_instance_of(int, order_id, 'Order id must be integer')
        res = self.httpclient.get(self.DETAILS_PATH.format_map({'order_id': order_id}))
        return res
