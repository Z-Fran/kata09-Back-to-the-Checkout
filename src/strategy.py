from src.utils import check_price, check_quantity, check_discount, check_weight

class PricingStrategy():
    def __init__(self, price: float):
        check_price(price)
        self.price = round(price, 2)

    def calculate_price(self, item_quantity: int) -> float:
        pass


class RegularPricing(PricingStrategy):
    def __init__(self, price: float):
        super().__init__(price)
    def calculate_price(self, item_quantity: int) -> float:
        total_price = self.price * item_quantity
        return round(total_price, 2)


class DiscountPricing(PricingStrategy):
    def __init__(self, price: float, discount: int):
        check_discount(discount)
        self.discount = discount
        super().__init__(price)

    def calculate_price(self, item_quantity: int) -> float:
        discounted_price = round(self.price * (100 - self.discount)/100.0, 2)
        total_price = discounted_price * item_quantity
        return round(total_price, 2)


class NDiscountMPricing(PricingStrategy):
    def __init__(self, price: float, buy_quantity: int, discount: int):
        check_quantity(buy_quantity)
        check_discount(discount)
        self.buy_quantity = buy_quantity
        self.discount = discount
        super().__init__(price)

    def calculate_price(self, item_quantity: int) -> float:
        if item_quantity < self.buy_quantity:
            return self.price * item_quantity
        else:
            discounted_price = round(self.price * (100 - self.discount)/100.0, 2)
            total_price = discounted_price * item_quantity
            return round(total_price, 2)
        
        
class BuyNGetMFreePricing(PricingStrategy):
    def __init__(self, price: float, buy_quantity: int, free_quantity: int):
        check_quantity(buy_quantity)
        check_quantity(free_quantity)
        self.buy_quantity = buy_quantity
        self.free_quantity = free_quantity
        super().__init__(price)

    def calculate_price(self, item_quantity: int) -> float:
        complete_sets = item_quantity // (self.buy_quantity + self.free_quantity)
        remaining_items = item_quantity % (self.buy_quantity + self.free_quantity)
        total_price = self.price * self.buy_quantity * complete_sets
        total_price += self.price * min(remaining_items, self.buy_quantity)
        return round(total_price, 2)


class NForMPricing(PricingStrategy):
    def __init__(self, price: float, buy_quantity: int, m_price: int):
        check_quantity(buy_quantity)
        check_price(m_price)
        self.buy_quantity = buy_quantity
        self.m_price = m_price
        super().__init__(price)

    def calculate_price(self, item_quantity: int) -> float:
        complete_sets = item_quantity // self.buy_quantity
        remaining_items = item_quantity % self.buy_quantity
        total_price = self.m_price * complete_sets
        total_price += self.price * remaining_items
        return round(total_price, 2)

class WeightPricing(PricingStrategy):
    def __init__(self, price: float, weight: float):
        check_weight(weight)
        self.weight = float(weight)
        super().__init__(price)
    def calculate_price(self, item_quantity: int) -> float:
        total_price = self.price * (item_quantity/self.weight)
        return round(total_price, 2)
