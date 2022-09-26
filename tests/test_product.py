import pytest

from product_inventory.product import Product


@pytest.fixture
def product():
    test_product = Product(
        product_id=1,
        name="test_product",
        price=1.00,
        quantity=100
    )

    return test_product


class TestProductId:
    def test_product_id_property_is_integer(self, product):
        assert isinstance(product.product_id, int)

    def test_product_id_propert:
        pass

class TestProductName:
    pass

class TestProductPrice:
    pass

class TestProductQuantity:
    pass