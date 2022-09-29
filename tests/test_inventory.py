import pytest

from product_inventory.inventory import Inventory
from .fixtures import (
    product,
    product_two,
    empty_inventory,
    single_item_inventory,
    two_item_inventory
)


class TestInventoryCreation:
    def test_inventory_can_be_instantiated(self):
        inventory = Inventory(
            name="test"
        )
        assert isinstance(inventory, Inventory)

    def test_inventory_can_be_instantiated_and_have_no_products(self):
        inventory = Inventory(
            name="test"
        )
        assert inventory.products == []


class TestInventoryName:
    def test_inventory_name_getter(self, empty_inventory):
        assert "test_inventory" == empty_inventory.name

    def test_inventory_name_setter(self, empty_inventory):
        empty_inventory.name = "test"
        assert "test" == empty_inventory.name

    def test_inventory_name_set_fails_with_int(self, empty_inventory):
        with pytest.raises(ValueError):
            empty_inventory.name = 1


class TestInventoryProducts:
    def test_inventory_products_getter(self, single_item_inventory, product):
        assert single_item_inventory.products == [product]

    def test_inventory_product_setter(self, empty_inventory, product):
        empty_inventory.products = [product]
        assert empty_inventory.products == [product]

    def test_inventory_products_must_be_list_of_products(self, empty_inventory):
        with pytest.raises(ValueError):
            empty_inventory.products = ["12", 14]

    def test_single_product_can_be_added_to_inventory(self , single_item_inventory, product, product_two):
        single_item_inventory.add_product(product_two)
        assert single_item_inventory.products == [product, product_two]

    def test_product_can_not_be_added_of_incorrect_type(self, single_item_inventory):
        with pytest.raises(ValueError):
            single_item_inventory.add_product(2)

    def test_products_can_be_added_to_inventory(self, empty_inventory, product, product_two):
        empty_inventory.add_products([product, product_two])
        assert empty_inventory.products == [product, product_two]

    def test_products_of_incorrect_type_can_not_be_added_to_inventory(self, empty_inventory):
        with pytest.raises(ValueError):
            empty_inventory.add_products([12, 12])

    def test_remove_product_removes_product(self, single_item_inventory, product):
        single_item_inventory.remove_product(product)
        assert single_item_inventory.products == []

    def test_remove_products_removes_products(self, two_item_inventory, product, product_two):
        two_item_inventory.remove_products([product, product_two])
        assert two_item_inventory.products == []


class TestInventoryItems:
    def test_inventory_total_items(self, single_item_inventory):
        assert single_item_inventory.total_items == 1


class TestInventorySum:
    def test_inventory_sum(self, single_item_inventory):
        assert single_item_inventory.inventory_sum == 100.0
