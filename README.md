# Shipday Python SDK

The Shipday Python sdk provides easier access to Shipday API's
from Python applications and scripts.

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

You need to provide the shipday api-key in order to use the library. To get your API key
login to your [Shipday Dispatch Dashboard](https://dispatch.shipday.com) and Find the 
API key from integrations tab.

Example usages looks like following:-

```python
API_KEY = '##########.#######################'
my_shipday = Shipday(api_key=API_KEY)
```

This my_shipday object contains three services (CarrierService, OrderService and OnDemandDeliveryService) which you can use to get your job
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

carrier_req = CarrierRequest(name='John Doe',
                             email='john.doe@shipday.com',
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
    name='John Doe', email='john.doe', phone_number='+12367124',
    address=Address(street='556 Crestlake Dr', city='San Francisco', state='California', country='USA')
)
# Don't worry if you forget to send a parameter, you can also set it later like following line
new_order.customer.address.zip = 'CA 94132'

# Add pickup details
new_order.pickup = Pickup(
    name='My pickup point', phone_number='+132462374'
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

To retrieve orders by order number, use get_order function. This will return a list of orders matching the given
order_number.

```python
orders = my_shipday.OrderService.get_order(order_number='100')
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

### OnDemandDeliveryService
To get informations on On-Demand Delivery Services use get_services() function like following code -
```python
my_shipday.OnDemandDeliveryService.get_services()
```

You can use get_active_services() function to retrieve the service names of those available to your account.
```python
my_shipday.OnDemandDeliveryService.get_active_services()
```

To estimate the cost and required delivery time from available delivery services, use estimate() function -
```python
my_shipday.OnDemandDeliveryService.estimate(order_id=123424)
```

You can assign an order to a delivery service provider by calling assign() method. For example,
```python
my_shipday.OnDemandDeliveryService.assign(order_id=1234, service_name='Uber')
```

After assigning an order to a service, you can get the details using get_details() method.
```python
my_shipday.OnDemandDeliveryService.get_details(order_id=1234)
```

If something goes wrong, you can cancel an assigned order using cancel() function. But this is not guaranteed to work-.
```python
my_shipday.OnDemandDeliveryService.cancel(order_id=1234)
```

