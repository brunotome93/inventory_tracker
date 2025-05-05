from decimal import Decimal
from models import Warehouse, Customer
from reporter import generate_report, format_currency

def test_format_currency():
    assert format_currency(Decimal("20.5")) == "$20.50"
    assert format_currency(Decimal("3.456")) == "$3.46"

def test_generate_report():
    warehouse = Warehouse()
    
    # Customer with no orders
    warehouse.customers["dan"] = Customer("dan")
    
    # Customer with orders
    kate = Customer("kate")
    kate.add_order("hats", 20, Decimal("20.50"))
    kate.add_order("socks", 10, Decimal("3.45"))
    warehouse.customers["kate"] = kate
    
    report = generate_report(warehouse)
    lines = report.split("\n")
    
    assert "dan: n/a" in lines
    assert "kate: hats - $410.00, socks - $34.50 | Average Order Value: $222.25" in lines