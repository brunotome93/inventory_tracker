from decimal import Decimal
from models import Warehouse
from typing import TextIO

def process_line(warehouse: Warehouse, line: str) -> None:
    parts = line.strip().split()
    if not parts:
        return
    
    command = parts[0].lower()
    
    try:
        if command == 'register' and len(parts) == 3:
            name = parts[1]
            price = Decimal(parts[2].lstrip('$'))
            warehouse.register_product(name, price)
        
        elif command == 'checkin' and len(parts) == 3:
            name = parts[1]
            quantity = int(parts[2])
            warehouse.checkin_product(name, quantity)
        
        elif command == 'order' and len(parts) == 4:
            customer_name = parts[1]
            product_name = parts[2]
            quantity = int(parts[3])
            warehouse.process_order(customer_name, product_name, quantity)
    
    except (ValueError, IndexError):
        # Skip malformed lines
        pass

def process_file(file_path: str) -> Warehouse:
    warehouse = Warehouse()
    with open(file_path, 'r') as file:
        for line in file:
            process_line(warehouse, line)
    return warehouse