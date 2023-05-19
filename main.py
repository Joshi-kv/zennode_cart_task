#catelog of product
catelog = {
    "Product A" : 20,
    "Product B" : 40,
    "Product C" : 50,
}

# discount rules 

discount_rules = {
    "flat_10_discount": {"threshold_limit": 200, "discount": 10},
    "bulk_5_discount": {"threshold_limit": 10, "discount": 0.05},
    "bulk_10_discount": {"threshold_limit": 20, "discount": 0.1},
    "tiered_50_discount": {"quantity_threshold_limit": 30, "single_product_threshold_limit": 15, "discount": 0.5}
}


#fees

gift_wrap_fees = 1
shipping_fees_per_packege = 5
items_per_packege = 10

#fuction to calculate the discount 

def calculate_discount(cart) : 
    eligible_discount = []
    
    #checks if flat_discount_10 is applicable 
    
    if cart > discount_rules["flat_10_discount"]["threshold_limit"] :
        eligible_discount.append(('flat_10_discount',discount_rules['flat_10_discount']['discount']))
        
        return eligible_discount
    

