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
New inventory after Product has been removed:
{[product.name for product in inventory_1.products]}
    """)

    # Remove multiple products from our inventory
    product_3 = Product(
        product_id=3,
        name="DR pepper",
        price=1.35,
        quantity=50
    )

    inventory_1.add_product(product_3)

    inventory_1.remove_products([product_3, product_2])

    print(f"""
New inventory after multiple products have been been removed:
{[product.name for product in inventory_1.products]}
    """)

    # Add multiple products to our already instantiated inventory
    inventory_1.add_products([product_1, product_2, product_3])
    print(f"""
New inventory after multiple products have been been added:
{[product.name for product in inventory_1.products]}
        """)

    # Show the total size of our inventory
    print(f"Total inventory size: {inventory_1.total_items}")

    # Show the total amount all products in our inventory would cost
    print(f"Total inventory cost: ${inventory_1.inventory_sum}")

