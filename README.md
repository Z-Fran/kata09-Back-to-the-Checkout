# kata09-Back-to-the-Checkoutout

## Solution 1

Assumptions:
+ Each product has only one specific pricing rule, and each pricing rule applies to only one product.

Rules: 
+ Regular: A's price is $1.1
+ Discount: 20% off
+ Buy N get discount: Buy 3 get 20% off
+ N for M dollars: Three for $1
+ Buy N get M free: Buy two, get 1 free.
+ Weight-based pricing: $2/kg

## Solution 2
Assumptions:
+ Each product has more than one specific pricing rule.

Rules:
+ Regular: A's price is $1.1 -- {"A": 1}
+ Discount: 20% off {"A": 1*0.8}
+ N for M dollars: Three for $1 -- {"AAA": 1}
+ Bundle pricing for multiple products: Two A and One B for $5 -- {"AAB": 5}