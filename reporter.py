from decimal import Decimal
from models import Warehouse

def format_currency(amount: Decimal) -> str:
    return f"${amount:.2f}"

def generate_report(warehouse: Warehouse) -> str:
    lines = []
    customer_names = sorted(warehouse.customers.keys())
    
    for name in customer_names:
        customer = warehouse.customers[name]
        spending = customer.get_spending_by_product()
        avg_order = customer.get_average_order_value()
        
        if not spending:
            lines.append(f"{name}: n/a")
            continue
        
        product_details = []
        for product_name in sorted(spending.keys()):
            total = spending[product_name]
            product_details.append(f"{product_name} - {format_currency(total)}")
        
        products_str = ", ".join(product_details)
        
        if avg_order is not None:
            avg_str = format_currency(avg_order)
            lines.append(f"{name}: {products_str} | Average Order Value: {avg_str}")
        else:
            lines.append(f"{name}: {products_str}")
    
    return "\n".join(lines)