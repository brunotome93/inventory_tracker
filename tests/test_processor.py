from decimal import Decimal
from models import Warehouse
from processor import process_line

def test_process_line_register():
    warehouse = Warehouse()
    process_line(warehouse, "register hats $20.50")
    assert "hats" in warehouse.products
    assert warehouse.products["hats"].price == Decimal("20.50")

def test_process_line_checkin():
    warehouse = Warehouse()
    warehouse.register_product("hats", Decimal("20.50"))
    process_line(warehouse, "checkin hats 100")
    assert warehouse.inventory.has_stock("hats", 100)

def test_process_line_order():
    warehouse = Warehouse()
    warehouse.register_product("hats", Decimal("20.50"))
    warehouse.checkin_product("hats", 100)
    process_line(warehouse, "order kate hats 20")
    assert warehouse.inventory.has_stock("hats", 80)
    assert "kate" in warehouse.customers
    assert len(warehouse.customers["kate"].orders) == 1

def test_process_line_invalid():
    warehouse = Warehouse()
    # Invalid command
    process_line(warehouse, "invalid command")
    # Malformed register
    process_line(warehouse, "register hats")
    # Malformed checkin
    process_line(warehouse, "checkin hats")
    # Malformed order
    process_line(warehouse, "order kate hats")
    assert len(warehouse.products) == 0
    assert len(warehouse.customers) == 0