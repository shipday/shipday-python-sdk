from shipday.exeptions import ShipdayException
from shipday.httpclient.shipdayclient import ShipdayClient
from shipday.order import Order, OrderQuery
from shipday.utils.verifiers import verify_instance_of


class OrderService:
    PATH = 'orders/'
    EDIT_PATH = 'order/edit/{order_id}'
    ASSIGN_PATH = PATH + 'assign/{order_id}/{carrier_id}'
    QUERY_PATH = PATH + 'query/'

    def __init__(self, *args, api_key, **kwargs):
        self.httpclient = ShipdayClient(*args, api_key=api_key, **kwargs)

    def get_orders(self) -> list:
        return self.httpclient.get(self.PATH)

    def get_order(self, order_number: str) -> list:
        if order_number is None:
            raise ShipdayException('Order number can not be None')
        response = self.httpclient.get(self.PATH + str(order_number))
        return response

    def insert_order(self, request: Order):
        request.verify()
        response = self.httpclient.post(self.PATH, request.get_body())
        if 'errorCode' in response:
            raise ShipdayException(response['errorMessage'])
        return response

    def edit_order(self, order_id: int, request: Order):
        request.verify()
        payload = request.get_body()
        payload['orderId'] = order_id
        response = self.httpclient.put(
            self.EDIT_PATH.format_map(
                {'order_id': order_id}
            ),
            payload
        )
        if 'errorCode' in response:
            raise ShipdayException(response['errorMessage'])
        return response

    def delete_order(self, order_id: int):
        verify_instance_of(int, order_id, 'Order id must be integer')

        response = self.httpclient.delete(self.PATH + str(order_id))
        return response

    def assign_order(self, order_id: int, carrier_id: int):
        verify_instance_of(int, order_id, 'Order id must be integer')
        verify_instance_of(int, carrier_id, 'Carrier id must be integer')

        response = self.httpclient.put(self.ASSIGN_PATH.format_map({'order_id': order_id, 'carrier_id': carrier_id}),
                                       {})
        return response

    def query(self, query: OrderQuery):
        if type(query) is not OrderQuery:
            raise ShipdayException("Query is not of type " + str(OrderQuery))
        response = self.httpclient.post(self.QUERY_PATH, query.get_body())
        return response
