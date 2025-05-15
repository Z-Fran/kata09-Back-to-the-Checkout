from typing import List
from src.rule import Rule

class Checkout:
    """A checkout system that calculates total price based on pricing rules.
    
    This class manages a collection of items scanned at checkout and calculates
    their total price according to the provided pricing rules.
    
    Attributes:
        rules (List[Rule]): A list of pricing rules for different items.
        scanned_items (dict): A dictionary tracking scanned items and their quantities.
    """
    
    def __init__(self, rules: List[Rule]):
        """Initialize the checkout system with pricing rules.
        
        Args:
            rules (List[Rule]): A list of pricing rules for different items.
        """
        self.rules = rules
        self.scanned_items = {}

    def scan(self, item: str, quantity: float = 1):
        """Scan an item and add it to the checkout.
        
        Args:
            item (str): The identifier of the item being scanned.
            quantity (float, optional): The quantity of the item. Defaults to 1.
        """
        if item not in self.scanned_items:
            self.scanned_items[item] = quantity
        else:
            self.scanned_items[item] += quantity

    def calculate_total_price(self) -> float:
        """Calculate the total price of all scanned items.
        
        Returns:
            float: The total price calculated based on the pricing rules.
        """
        total_price = 0
        for item in self.scanned_items:
            item_rule = self.rules[item]
            item_quantity = self.scanned_items[item]
            total_price += item_rule.calculate_price(item_quantity)
        return total_price
