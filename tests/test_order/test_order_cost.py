import pytest
from itertools import combinations

from shipday.exceptions import ShipdayException
from shipday.order import OrderCost


def get_test_order_costs() -> list:
    params = {
        'tips': 2.5,
        'tax': 3.0,
        'discount': 1,
        'deliveryFee': 3,
        'total': 20
    }
    return [OrderCost(**{key: params[key] for key in combination})
            for r in range(len(params) + 1)
            for combination in combinations(params, r)]


class TestOrderCost:
    """Order Cost"""

    not_positive_numbers = [None, -1, 'abc', [1], {'a': 1}]

    oc = OrderCost(tips=1, tax=5, discount=3, deliveryFee=10, total=20)

    @pytest.mark.parametrize('order_cost', get_test_order_costs())
    @pytest.mark.parametrize('value', not_positive_numbers)
    def test_invalid_tips_set(self, order_cost: OrderCost, value):
        """Throws exception if tips is not a positive number or zero ::"""
        with pytest.raises(ShipdayException):
            order_cost.tips = value

    @pytest.mark.parametrize('order_cost', get_test_order_costs())
    @pytest.mark.parametrize('value', not_positive_numbers)
    def test_invalid_tax_set(self, order_cost: OrderCost, value):
        """Throws exception if tax is not a positive number or zero ::"""
        with pytest.raises(ShipdayException):
            order_cost.tax = value

    @pytest.mark.parametrize('order_cost', get_test_order_costs())
    @pytest.mark.parametrize('value', not_positive_numbers)
    def test_invalid_discount_set(self, order_cost: OrderCost, value):
        """Throws exception if discount is not a positive number or zero ::"""
        with pytest.raises(ShipdayException):
            order_cost.discount = value

    @pytest.mark.parametrize('order_cost', get_test_order_costs())
    @pytest.mark.parametrize('value', not_positive_numbers)
    def test_invalid_delivery_set(self, order_cost: OrderCost, value):
        """Throws exception if delivery fee is not a positive number or zero ::"""
        with pytest.raises(ShipdayException):
            order_cost.delivery_fee = value

    @pytest.mark.parametrize('order_cost', get_test_order_costs())
    @pytest.mark.parametrize('value', not_positive_numbers)
    def test_invalid_total_set(self, order_cost: OrderCost, value):
        """Throws exception if total is not a positive number or zero ::"""
        with pytest.raises(ShipdayException):
            order_cost.total = value
