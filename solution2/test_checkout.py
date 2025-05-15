from .checkout import Checkout

def get_rules():
    return {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "AAA": 2,
        "AAAAA": 3.4,
        "CC": 5,
        "CD": 5,
    }

def test_6A():
    checkout = Checkout(get_rules())
    items = list('AAAAAA')
    result = checkout.calculate_price(items)
    assert result == 4

def test_10A():
    checkout = Checkout(get_rules())
    items = list('AAAAAAAAAA')
    result = checkout.calculate_price(items)
    assert result == 6.8
