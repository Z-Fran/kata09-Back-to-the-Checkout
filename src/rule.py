from .strategy import PricingStrategy

class Rule:
    def __init__(self,
                 strategy: PricingStrategy):
        self.strategy = strategy
        
    def calculate_price(self, item_quantity: int) -> float:
        return self.strategy.calculate_price(item_quantity)
