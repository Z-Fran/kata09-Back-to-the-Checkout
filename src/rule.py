from src.strategy import PricingStrategy

class Rule:
    """A class representing a pricing rule that applies a specific pricing strategy.
    
    This class encapsulates a pricing strategy and provides a method to calculate
    the total price for a given quantity of items using that strategy.
    """
    
    def __init__(self,
                 strategy: PricingStrategy):
        """Initialize a new Rule instance.
        
        Args:
            strategy (PricingStrategy): The pricing strategy to be used for calculations.
        """
        self.strategy = strategy
        
    def calculate_price(self, item_quantity: int) -> float:
        """Calculate the total price for a given quantity of items.
        
        Args:
            item_quantity (int): The number of items to calculate the price for.
            
        Returns:
            float: The total price calculated using the strategy.
        """
        return self.strategy.calculate_price(item_quantity)
