import pytest

from product_inventory.product import Product
from product_inventory.inventory import Inventory


@pytest.fixture
def product() -> Product:
    product = Product(
        product_id=1,
        name="test_product",
        price=1.00,
        quantity=100
    )

    return product


@pytest.fixture
def product_two() -> Product:
    product = Product(
        product_id=2,
        name="test_product_two",
        price=2.00,
        quantity=200
    )

    return product


@pytest.fixture
def empty_inventory() -> Inventory:
    inventory = Inventory(
        name="test_inventory"
    )

    return inventory


@pytest.fixture()
def single_item_inventory(product) -> Inventory:

    inventory = Inventory(
        name="test_inventory",
        products=[product]
    )

    return inventory


@pytest.fixture()
def two_item_inventory(product, product_two) -> Inventory:

    inventory = Inventory(
        name="test_inventory",
        products=[product, product_two]
    )

    return inventory

