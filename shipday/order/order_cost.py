from collections import defaultdict

from shipday.utils.verifiers import verify_not_negative


class OrderCost:
    def __init__(self, *args,
                 tips: float = 0.0, tax: float = 0.0, discount: float = 0.0, delivery_fee: float = 0.0,
                 total: float = 0.0,
                 **kwargs):
        kwargs = defaultdict(lambda: 0.0, **kwargs)
        self._tips = tips
        self._tax = tax
        self._discount = discount or kwargs['discountAmount']
        self._delivery_fee = delivery_fee or kwargs['deliveryFee']
        self._total = total or kwargs['totalOrderCost']

    @property
    def tips(self):
        return self._tips

    @tips.setter
    def tips(self, value):
        verify_not_negative(value, "Tips must be a positive number")
        self._tips = float(value)

    @property
    def tax(self):
        return self._tax

    @tax.setter
    def tax(self, value):
        verify_not_negative(value, "Tax must be a positive number")
        self._tax = value

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        verify_not_negative(value, "Discount must be a positive number")
        self._discount = value

    @property
    def delivery_fee(self):
        return self._delivery_fee

    @delivery_fee.setter
    def delivery_fee(self, value):
        verify_not_negative(value, "Delivery Fee must be a positive number")
        self._delivery_fee = float(value)

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        verify_not_negative(value, "Total must be a positive number")
        self._total = value

    def verify(self):
        verify_not_negative(self._tips, "Tips must be a positive number")
        verify_not_negative(self._tax, "Tax must be a positive number")
        verify_not_negative(self._discount, "Discount must be a positive number")
        verify_not_negative(self._delivery_fee, "Delivery Fee must be a positive number")
        verify_not_negative(self._total, "Total must be a positive number")

    def get_body(self):
        return {
            'tips': self.tips,
            'tax': self.tax,
            'discountAmount': self.discount,
            'deliveryFee': self.delivery_fee,
            'total': self.total
        }
