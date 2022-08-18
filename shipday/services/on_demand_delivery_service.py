from shipday.utils.verifiers import verify_instance_of, verify_none_or_instance_of
from shipday.exeptions.shipday_exeption import ShipdayException
from shipday.httpclient.shipdayclient import ShipdayClient


class OnDemandDeliveryService:
    PATH = 'on-demand/'
    SERVICES_PATH = PATH + 'services'
    ESTIMATE_PATH = PATH + 'estimate/{order_id}'
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

    def estimate(self, order_id) -> dict:
        verify_instance_of(int, order_id, 'Order id must be integer')
        res = self.httpclient.get(self.ESTIMATE_PATH.format_map({'order_id': order_id}))
        return res

    def assign(self, *args, order_id, service_name, tip=0, estimate_reference=None, **kwargs) -> dict:
        verify_instance_of(int, order_id, 'Order id must be integer')
        verify_instance_of([int, float], tip, 'Order id must be integer')
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

    def cancel(self, order_id) -> dict:
        verify_instance_of(int, order_id, 'Order id must be integer')
        res = self.httpclient.post(self.CANCEL_PATH.format_map({'order_id': order_id}), {})
        return res

    def get_details(self, order_id) -> dict:
        verify_instance_of(int, order_id, 'Order id must be integer')
        res = self.httpclient.get(self.DETAILS_PATH.format_map({'order_id': order_id}))
        return res
