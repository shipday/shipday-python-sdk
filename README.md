# Shipday Python SDK

The Shipday Python sdk provides easier access to Shipday API's
Python applications and scripts.

## Documentation

See the [shipday api](https://docs.shipday.com) docs for Python.

## Requirements

Python 3.6 or higher

## Installation

```markdown
pip install shipday
```

## Usage

Import Shipday from shipday package.

```python
from shipday import Shipday
```

You need to provide the shipday api-key in order to use the library. Example usages looks like following:-

```python
API_KEY = '##########.#######################'
my_shipday = Shipday(api_key=API_KEY)
```

This my_shipday object contains two services (CarrierService and OrderService) which you can use to get your job
done. Here are few examples,

### Carrier Service

To get all your carriers, use get_carriers() function of the CarrierService. Following example
prints the number of carriers you have -

```python
my_carriers = my_shipday.CarrierService.get_carriers()
print('I have {} carriers'.format(len(my_carriers)))
```

To add a carrier, you need to create a CarrierRequest and send it using add_carrier() function of
CarrierService.
See the example below -

```python
from shipday.carrier import CarrierRequest

carrier_req = CarrierRequest(name='Library carrier',
                             email='library_carrier3@shahriar.shipday',
                             phone_number='+123456789')
my_shipday.CarrierService.add_carrier(carrier_req)
```

To delete a carrier, use delete_carrier() function of the CarrierService. For example-

```python
my_shipday.CarrierService.delete_carrier(carrier_id=1234)
```

### Order Service

To get all the orders, use get_orders() function of the OrderService.

```python
my_orders = my_shipday.OrderService.get_orders()
```

To add an order, you need to create an Order object and send it using insert_order() function of
OrderService. For example -

```python
from shipday.order import Address, Customer, Pickup, OrderItem, Order

new_order = Order(orderNumber='100')

# Add customer details
new_order.customer = Customer(
    name='Shahriar', email='shahriar@shahriar.shipday', phone_number='+88012367124',
    address=Address(street='556 Crestlake Dr', city='San Francisco', state='California', country='USA')
)
# Don't worry if you forget to send a parameter, you can also set it later like following line
new_order.customer.address.zip = 'CA 94132'

# Add pickup details
new_order.pickup = Pickup(
    name='My pickup point', phone_number='+8832462374'
)
new_order.pickup.address = Address(street='890 Geneva Av', city='San Fransisco', state='California', zip='CA 94132',
                                   country='USA')

# Add order items
new_order.order_items = [OrderItem(name='Pizza', unit_price=10.0, quantity=1)]
new_order.order_items.append(
    OrderItem(name='Popcorn Shrimp', quantity=1, unit_price=5)
)

my_shipday.OrderService.insert_order(new_order)
```

To get retrive orders by order number, use get_order function. This will return a list of orders matching the given
order_number.

```python
orders = my_shipday.OrderService.get_order(order_number='#1')
```

To assign an order to a carrier, use assign_order() function. For example,

```python
my_shipday.OrderService.assign_order(order_id=7995257, carrier_id=242324)
```

To delete an order, use delete_order() function. For example,

```python
my_shipday.OrderService.delete_order(order_id=7995246)
```

You can also query orders using query() function. For that you need to create a OrderQuery object. Following
code retrieves all orders from last 24 hours -

```python
from shipday.order import OrderQuery

query = OrderQuery()

from datetime import datetime, timedelta

query.start_time = datetime.now() - timedelta(days=1)

my_shipday.OrderService.query(query=query)
```



