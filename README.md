# Inventory Tracking System

## Overview

This solution provides a system for tracking customer orders and warehouse inventory. It processes input commands to register products, manage inventory, and record customer orders, then generates a report showing customer spending patterns.

## Features

- Product registration with pricing
- Inventory management (stock check-ins)
- Order processing with validation
- Customer spending tracking
- Comprehensive reporting with:
  - Per-product spending
  - Average order values
  - Proper handling of failed orders

## Installation

1. Ensure Python 3.10+ is installed
2. Install dependencies:

```bash
pip install pytest
```

## Usage

Process an input file:

```bash
python3 main.py input.txt
```

Run tests:

```bash
python3 -m pytest tests/
```

## Input Format

The system accepts three command types:

#### 1. Register products:

```bash
register <product_name> $<price>
```

#### 2. Check-in inventory:

```bash
checkin <product_name> <quantity>
```

#### 3. Place orders:

```bash
order <customer_name> <product_name> <quantity>
```

## Output Format

The report shows:

- Customers alphabetically
- Products alphabetically per customer
- Formatted currency values
- Average order value when applicable

Example:

```bash
Alice: hats - $102.50, socks - $34.50 | Average Order Value: $68.50
Bob: shirts - $47.97 | Average Order Value: $47.97
```

## Design Decisions

#### 1. Domain Modeling:

- Used classes for core entities (Product, Inventory, Customer)
- Warehouse as aggregate root coordinating operations

#### 2. Data Integrity:

- Decimal for monetary values
- Inventory validation before order processing
- Immutable operations where possible

#### 3. Error Handling:

- Silent skipping of malformed input
- Graceful handling of stock shortages

#### 4. Testing:

- Unit tests for all components
- Integration via end-to-end processing
- Edge case coverage

## Testing Approach

The test suite verifies:

- Model behavior (90% coverage)
- Command processing logic
- Report formatting accuracy
- Inventory management
- Error scenarios
