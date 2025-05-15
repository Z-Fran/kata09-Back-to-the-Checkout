import pytest
from src.rule import Rule
from src.strategy import (RegularPricing,
                          DiscountPricing,
                          NDiscountMPricing,
                          BuyNGetMFreePricing,
                          NForMPricing,
                          WeightPricing)   
from src.checkout import Checkout

def get_rules():
    rules = {
        "A": Rule(RegularPricing(1)),
        "B": Rule(DiscountPricing(2, 10)),
        "C": Rule(NDiscountMPricing(4, 3, 10)),
        "D": Rule(BuyNGetMFreePricing(3, 3, 2)),
        "E": Rule(NForMPricing(1, 3, 2)),
        "F": Rule(WeightPricing(10, 1)),
    }
    return rules

def scan_items(checkout, items):
    items = list(items)
    while items:
        item = items.pop(0)
        if item == '|':
            item = items.pop(0)
            quantity = float(''.join(items[0:items.index('|')]))
            items = items[items.index('|')+1:]
            checkout.scan(item, quantity)
        else:
            checkout.scan(item)

def test_ABC():
    checkout = Checkout(get_rules())
    items = "ABCBBCCC"
    scan_items(checkout, items)
    assert checkout.calculate_total_price() == 20.8

def test_DE():
    checkout = Checkout(get_rules())
    items = "DDEEDDEDDE"
    scan_items(checkout, items)
    assert checkout.calculate_total_price() == 15.0

def test_F():
    checkout = Checkout(get_rules())
    items = "AA|F2.5|AA"
    scan_items(checkout, items)
    assert checkout.calculate_total_price() == 29.0



