from src.rule import Rule
from src.strategy import RegularPricing

def test_rule():
    rule = Rule(strategy=RegularPricing(price=10))
    assert rule.calculate_price(10) == 100.0
