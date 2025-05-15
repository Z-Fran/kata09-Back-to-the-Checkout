import pytest
from src.strategy import (PricingStrategy,
                          RegularPricing,
                          DiscountPricing,
                          NDiscountMPricing,
                          BuyNGetMFreePricing,
                          NForMPricing,
                          WeightPricing)    

def test_pricing_strategy_valid_prices():
    # Test integer price
    strategy = PricingStrategy(10)
    assert strategy.price == 10.0
    
    # Test float price
    strategy = PricingStrategy(10.5)
    assert strategy.price == 10.5
    
    # Test price rounding
    strategy = PricingStrategy(10.666)
    assert strategy.price == 10.67
    strategy = PricingStrategy(10.444)
    assert strategy.price == 10.44

def test_pricing_strategy_invalid_prices():
    # Test negative price
    with pytest.raises(ValueError):
        PricingStrategy(-1)

    # Test non-numeric price
    with pytest.raises(TypeError):
        PricingStrategy("10")
    
    with pytest.raises(TypeError):
        PricingStrategy(None)

def test_regular_pricing():
    # Test the RegularPricing strategy
    regular_pricing = RegularPricing(2)
    assert regular_pricing.calculate_price(2) == 4.0
    assert regular_pricing.calculate_price(0) == 0.0
    assert regular_pricing.calculate_price(1.111) == 2.22

def test_discount_pricing_invalid_prices():
    with pytest.raises(TypeError):
        DiscountPricing(10, "10")
    with pytest.raises(ValueError):
        DiscountPricing(10, -1)
    with pytest.raises(ValueError):
        DiscountPricing(10, 101)
    with pytest.raises(TypeError):
        DiscountPricing(10, 10.1)

def test_discount_pricing_valid_prices():
    discount_pricing = DiscountPricing(10, 10)
    assert discount_pricing.calculate_price(10) == 90.0
    assert discount_pricing.calculate_price(0) == 0.0

def test_n_discount_m_pricing_invalid_prices():
    with pytest.raises(TypeError):
        NDiscountMPricing(10, "10", 1)
    with pytest.raises(TypeError):
        NDiscountMPricing(10, 1, 1.1)
    with pytest.raises(ValueError):
        NDiscountMPricing(10, -1, 1)

def test_n_discount_m_pricing_valid_prices():
    n_discount_m_pricing = NDiscountMPricing(10, 10, 10)
    assert n_discount_m_pricing.calculate_price(10) == 90.0
    assert n_discount_m_pricing.calculate_price(5) == 50.0

def test_buy_n_get_m_free_pricing_invalid_prices():
    with pytest.raises(TypeError):
        BuyNGetMFreePricing(10, "10", 1)
    with pytest.raises(TypeError):
        BuyNGetMFreePricing(10, 1, 1.1)
    with pytest.raises(ValueError):
        BuyNGetMFreePricing(10, -1, 1)

def test_buy_n_get_m_free_pricing_valid_prices():
    buy_n_get_m_free_pricing = BuyNGetMFreePricing(1, 3, 2)
    assert buy_n_get_m_free_pricing.calculate_price(11) == 7.0
    assert buy_n_get_m_free_pricing.calculate_price(9) == 6.0
    assert buy_n_get_m_free_pricing.calculate_price(3) == 3.0

def test_n_for_m_pricing_invalid_prices():
    with pytest.raises(TypeError):
        NForMPricing(10, "10", 1)
    with pytest.raises(ValueError):
        NForMPricing(10, -1, 1)

def test_n_for_m_pricing_valid_prices():
    n_for_m_pricing = NForMPricing(10, 3, 20)
    assert n_for_m_pricing.calculate_price(7) == 50.0
    assert n_for_m_pricing.calculate_price(2) == 20.0

def test_weight_pricing_invalid_prices():
    with pytest.raises(TypeError):
        WeightPricing(10, "10")
    with pytest.raises(ValueError):
        WeightPricing(10, -1)

def test_weight_pricing_valid_prices():
    weight_pricing = WeightPricing(10, 2)
    assert weight_pricing.calculate_price(3) == 15.0
