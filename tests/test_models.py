from decimal import Decimal
from models import Product, Inventory, Customer, Warehouse

def test_product_creation():
    product = Product("hats", Decimal("20.50"))
    assert product.name == "hats"
    assert product.price == Decimal("20.50")

def test_inventory_management():
    inventory = Inventory()
    inventory.add_stock("hats", 100)
    assert inventory.has_stock("hats", 50)
    assert not inventory.has_stock("hats", 101)
    assert not inventory.has_stock("socks", 1)
    
    inventory.deduct_stock("hats", 20)
    assert inventory.has_stock("hats", 80)
    assert not inventory.has_stock("hats", 81)

def test_customer_orders():
    customer = Customer("kate")
    customer.add_order("hats", 2, Decimal("10.00"))
    customer.add_order("socks", 3, Decimal("5.00"))
    
    assert customer.get_total_spent() == Decimal("35.00")
    assert customer.get_spending_by_product() == {
        "hats": Decimal("20.00"),
        "socks": Decimal("15.00")
    }
    assert customer.get_average_order_value() == Decimal("17.50")

def test_warehouse_operations():
    warehouse = Warehouse()
    warehouse.register_product("hats", Decimal("20.50"))
    warehouse.checkin_product("hats", 100)
    
    assert warehouse.process_order("kate", "hats", 20)
    assert warehouse.inventory.has_stock("hats", 80)
    assert not warehouse.inventory.has_stock("hats", 81)
    
    assert not warehouse.process_order("dan", "socks", 10)
    assert "dan" not in warehouse.customers