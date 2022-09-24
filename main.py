#!/usr/bin/env python3

from product_inventory.product import Product
from product_inventory.inventory import Inventory

if __name__ == '__main__':
    # Create our inventory with no products
    inventory_1 = Inventory("Warehouse 1")

    # Create our first product
    product_1 = Product(
        product_id=1,
        name="Pepsi Cola",
        price=1.20,
        quantity=100
    )

    # Display all product attributes
    print(f"""
Product Name:
{product_1.name}
Product ID:
{product_1.product_id}
Product Quantity:
{product_1.quantity}
Product price:
{product_1.price}
    """)

    # Set all product attributes again
    product_1.name = "Pepsi"
    product_1.product_id = 2
    product_1.quantity = 200
    product_1.price = 1.40

    print(f"""
Product New Name:
{product_1.name}
Product New ID:
{product_1.product_id}
Product New Quantity:
{product_1.quantity}
Product New Price:
{product_1.price}
    """)

    # Create a second product
    product_2 = Product(
        product_id=2,
        name="Fanta 2L",
        price=2.40,
        quantity=100
    )

    # Show inventory properties
    print(f"""
Inventory Name:
{inventory_1.name}
Inventory Products:
{inventory_1.products}
    """)

    # Set out inventory products to now be the two products we have created
    inventory_1.products = [product_1, product_2]
    print(f"""
Inventory New Products:
{[product.name for product in inventory_1.products]}
    """)

    # Remove product from our inventory
    inventory_1.remove_product(product_1)
    print(f"""
New Inventory After Product has been removed:
{[product.name for product in inventory_1.products]}
    """)
