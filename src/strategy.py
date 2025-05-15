from src.utils import (check_price,
                       check_quantity,
                       check_discount,
                       check_weight)

class PricingStrategy():
    """Base class for all pricing strategies.
    
    This abstract class defines the interface for all pricing strategies.
    Each concrete strategy must implement the calculate_price method.
    """
    def __init__(self, price: float):
        """Initialize the pricing strategy with a base price.
        
        Args:
            price (float): The base price of the item
        """
        check_price(price)
        self.price = round(price, 2)

    def calculate_price(self, item_quantity: int) -> float:
        """Calculate the total price for a given quantity of items.
        
        Args:
            item_quantity (int): The number of items to calculate price for
            
        Returns:
            float: The total price rounded to 2 decimal places
        """
        pass


class RegularPricing(PricingStrategy):
    """Regular pricing strategy that applies no special discounts.
    
    This strategy simply multiplies the base price by the quantity.
    """
    def __init__(self, price: float):
        """Initialize regular pricing with base price.
        
        Args:
            price (float): The base price of the item
        """
        super().__init__(price)
        
    def calculate_price(self, item_quantity: int) -> float:
        """Calculate total price by multiplying base price with quantity.
        
        Args:
            item_quantity (int): The number of items to calculate price for
            
        Returns:
            float: The total price rounded to 2 decimal places
        """
        total_price = self.price * item_quantity
        return round(total_price, 2)


class DiscountPricing(PricingStrategy):
    """Pricing strategy that applies a percentage discount to all items.
    
    This strategy applies the same discount percentage to every item purchased.
    """
    def __init__(self, price: float, discount: int):
        """Initialize discount pricing with base price and discount percentage.
        
        Args:
            price (float): The base price of the item
            discount (int): The discount percentage to apply (0-100)
        """
        check_discount(discount)
        self.discount = discount
        super().__init__(price)

    def calculate_price(self, item_quantity: int) -> float:
        """Calculate total price with discount applied to all items.
        
        Args:
            item_quantity (int): The number of items to calculate price for
            
        Returns:
            float: The total price rounded to 2 decimal places
        """
        discounted_price = round(self.price * (100 - self.discount)/100.0, 2)
        total_price = discounted_price * item_quantity
        return round(total_price, 2)


class NDiscountMPricing(PricingStrategy):
    """Pricing strategy that applies a discount when buying N or more items.
    
    This strategy applies a discount percentage only when the quantity purchased
    meets or exceeds the specified threshold.
    """
    def __init__(self, price: float, buy_quantity: int, discount: int):
        """Initialize N-for-discount pricing with base price, quantity threshold and discount.
        
        Args:
            price (float): The base price of the item
            buy_quantity (int): The minimum quantity needed to get the discount
            discount (int): The discount percentage to apply (0-100)
        """
        check_quantity(buy_quantity)
        check_discount(discount)
        self.buy_quantity = buy_quantity
        self.discount = discount
        super().__init__(price)

    def calculate_price(self, item_quantity: int) -> float:
        """Calculate total price with discount applied if quantity threshold is met.
        
        Args:
            item_quantity (int): The number of items to calculate price for
            
        Returns:
            float: The total price rounded to 2 decimal places
        """
        if item_quantity < self.buy_quantity:
            return self.price * item_quantity
        else:
            discounted_price = round(self.price * (100 - self.discount)/100.0, 2)
            total_price = discounted_price * item_quantity
            return round(total_price, 2)
        
        
class BuyNGetMFreePricing(PricingStrategy):
    """Pricing strategy that offers M free items when buying N items.
    
    This strategy implements a "Buy N, Get M Free" promotion where customers
    get M items free for every N items purchased.
    """
    def __init__(self, price: float, buy_quantity: int, free_quantity: int):
        """Initialize Buy-N-Get-M-Free pricing with base price and quantities.
        
        Args:
            price (float): The base price of the item
            buy_quantity (int): The number of items that must be purchased
            free_quantity (int): The number of items that will be free
        """
        check_quantity(buy_quantity)
        check_quantity(free_quantity)
        self.buy_quantity = buy_quantity
        self.free_quantity = free_quantity
        super().__init__(price)

    def calculate_price(self, item_quantity: int) -> float:
        """Calculate total price with free items applied.
        
        Args:
            item_quantity (int): The number of items to calculate price for
            
        Returns:
            float: The total price rounded to 2 decimal places
        """
        complete_sets = item_quantity // (self.buy_quantity + self.free_quantity)
        remaining_items = item_quantity % (self.buy_quantity + self.free_quantity)
        total_price = self.price * self.buy_quantity * complete_sets
        total_price += self.price * min(remaining_items, self.buy_quantity)
        return round(total_price, 2)


class NForMPricing(PricingStrategy):
    """Pricing strategy that offers N items for a special price M.
    
    This strategy implements a "N for M" promotion where customers can buy
    N items for a special price M, with remaining items at regular price.
    """
    def __init__(self, price: float, buy_quantity: int, m_price: int):
        """Initialize N-for-M pricing with base price, quantity and special price.
        
        Args:
            price (float): The base price of the item
            buy_quantity (int): The number of items in the special offer
            m_price (int): The special price for buying N items
        """
        check_quantity(buy_quantity)
        check_price(m_price)
        self.buy_quantity = buy_quantity
        self.m_price = m_price
        super().__init__(price)

    def calculate_price(self, item_quantity: int) -> float:
        """Calculate total price with special N-for-M pricing applied.
        
        Args:
            item_quantity (int): The number of items to calculate price for
            
        Returns:
            float: The total price rounded to 2 decimal places
        """
        complete_sets = item_quantity // self.buy_quantity
        remaining_items = item_quantity % self.buy_quantity
        total_price = self.m_price * complete_sets
        total_price += self.price * remaining_items
        return round(total_price, 2)


class WeightPricing(PricingStrategy):
    """Pricing strategy that calculates price based on weight.
    
    This strategy is used for items sold by weight, where the price
    is calculated based on the weight of the items.
    """
    def __init__(self, price: float, weight: float):
        """Initialize weight-based pricing with base price and weight.
        
        Args:
            price (float): The base price per unit of weight
            weight (float): The weight unit for pricing
        """
        check_weight(weight)
        self.weight = float(weight)
        super().__init__(price)
        
    def calculate_price(self, item_quantity: int) -> float:
        """Calculate total price based on weight.
        
        Args:
            item_quantity (int): The number of items to calculate price for
            
        Returns:
            float: The total price rounded to 2 decimal places
        """
        total_price = self.price * (item_quantity/self.weight)
        return round(total_price, 2)
