from decimal import Decimal
from typing import Dict, List, Optional

class Product:
    def __init__(self, name: str, price: Decimal):
        self.name = name
        self.price = price

class Inventory:
    def __init__(self):
        self.stock: Dict[str, int] = {}
    
    def add_stock(self, product_name: str, quantity: int) -> None:
        self.stock[product_name] = self.stock.get(product_name, 0) + quantity
    
    def has_stock(self, product_name: str, quantity: int) -> bool:
        return self.stock.get(product_name, 0) >= quantity
    
    def deduct_stock(self, product_name: str, quantity: int) -> None:
        if self.has_stock(product_name, quantity):
            self.stock[product_name] -= quantity

class Customer:
    def __init__(self, name: str):
        self.name = name
        self.orders: List[Dict[str, Decimal]] = []
    
    def add_order(self, product_name: str, quantity: int, price: Decimal) -> None:
        total = price * quantity
        self.orders.append({
            'product': product_name,
            'quantity': quantity,
            'total': total
        })
    
    def get_total_spent(self) -> Decimal:
        return sum(order['total'] for order in self.orders)
    
    def get_spending_by_product(self) -> Dict[str, Decimal]:
        spending = {}
        for order in self.orders:
            spending[order['product']] = spending.get(order['product'], Decimal(0)) + order['total']
        return spending
    
    def get_average_order_value(self) -> Optional[Decimal]:
        if not self.orders:
            return None
        return self.get_total_spent() / len(self.orders)

class Warehouse:
    def __init__(self):
        self.products: Dict[str, Product] = {}
        self.inventory = Inventory()
        self.customers: Dict[str, Customer] = {}
    
    def register_product(self, name: str, price: Decimal) -> None:
        self.products[name] = Product(name, price)
    
    def checkin_product(self, name: str, quantity: int) -> None:
        if name in self.products:
            self.inventory.add_stock(name, quantity)
    
    def process_order(self, customer_name: str, product_name: str, quantity: int) -> bool:
        if (product_name not in self.products or 
            not self.inventory.has_stock(product_name, quantity)):
            return False
        
        if customer_name not in self.customers:
            self.customers[customer_name] = Customer(customer_name)
        
        price = self.products[product_name].price
        self.customers[customer_name].add_order(product_name, quantity, price)
        self.inventory.deduct_stock(product_name, quantity)
        return True