class Product:
    """
    Class to represent a product and its quantity held
    """

    def __init__(self, product_id: int, name: str, price: float, quantity: int = 0):
        self._product_id: int = product_id
        self._name: str = name
        self._price: float = price
        self._quantity: quantity = quantity

    def get_product_id(self) -> int:
        return self._product_id

    def set_product_id(self, new_id: int) -> None:
        self._product_id = new_id
        return None

    def get_name(self) -> str:
        return self._name

    def set_name(self, new_name: str) -> None:
        self._name = new_name
        return None

    def get_price(self) -> float:
        return self._price

    def set_price(self, new_price: float) -> None:
        self._price = new_price
        return None

    def get_quantity(self) -> int:
        return self._quantity

    def set_quantity(self, new_quantity: int) -> None:
        self._quantity = new_quantity

    def increase_quantity(self, increase_value: int) -> None:
        self._quantity += increase_value

    def decrease_quantity(self, decrease_value: int) -> None:
        self._quantity -= decrease_value

    def increase_price(self, increase_value: int) -> None:
        self._price += increase_value

    def decrease_price(self, decrease_value: int) -> None:
        self._price -= decrease_value
