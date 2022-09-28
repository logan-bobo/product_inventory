from .product import Product


class Inventory:
    """
    A class to represent our inventory for a store
    """

    def __init__(self, name: str, products=None):
        if not products:
            products = []
        self._name: str = name
        self._products: list[Product] = products

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str):
        if type(new_name) != str:
            raise ValueError("New name must be a str")
        self._name = new_name

    @property
    def products(self) -> list[Product]:
        return self._products

    @products.setter
    def products(self, new_products: list[Product]):
        self._products = new_products

    @property
    def total_items(self) -> int:
        return len(self._products)

    @property
    def inventory_sum(self) -> float:
        return sum([(p.price * p.quantity) for p in self._products])

    def add_product(self, new_product: Product):
        self._products.append(new_product)

    def add_products(self, new_products: list[Product]):
        for new_product in new_products:
            self._products.append(new_product)

    def remove_product(self, product_to_remove: Product):
        try:
            self._products.remove(product_to_remove)
        except ValueError as e:
            raise ValueError(f"Product {product_to_remove} not in inventory. Error: {e}")

    def remove_products(self, products_to_remove: list[Product]):
        for product_to_remove in products_to_remove:
            try:
                self._products.remove(product_to_remove)
            except ValueError as e:
                raise ValueError(f"Product {product_to_remove} not in inventory. Error: {e}")
