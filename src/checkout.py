from typing import List
from src.rule import Rule

class Checkout:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.scanned_items = {}

    def scan(self, item: str, quantity: float = 1):
        if item not in self.scanned_items:
            self.scanned_items[item] = quantity
        else:
            self.scanned_items[item] += quantity

    def calculate_total_price(self) -> float:
        total_price = 0
        for item in self.scanned_items:
            item_rule = self.rules[item]
            item_quantity = self.scanned_items[item]
            total_price += item_rule.calculate_price(item_quantity)
        return total_price
