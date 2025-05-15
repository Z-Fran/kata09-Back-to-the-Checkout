def check_price(price: float) -> float:
    if type(price) not in [int, float]:
        raise TypeError("Price must be a number")
    if price < 0:
        raise ValueError("Price cannot be negative")

def check_quantity(quantity: int) -> int:
    if type(quantity) != int:
        raise TypeError("Quantity must be a int")
    if quantity < 0:
        raise ValueError("Quantity cannot be negative")
    return quantity

def check_discount(discount: int) -> int:
    if type(discount) != int:
        raise TypeError("Discount must be a int")
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100")
    return discount  

def check_weight(weight: float) -> float:
    if type(weight) not in [int, float]:
        raise TypeError("Weight must be a float")
    if weight < 0:
        raise ValueError("Weight cannot be negative")
    return weight
