#catalog 

catalog = {
    'Product A' : 20,
    'Product B' : 40,
    'Product C' : 50,
}

#discount rules 

discount_rules = {  
    "flat_10_discount": {"threshold": 200, "discount": 10},
    "bulk_5_discount": {"threshold": 10, "discount": 0.05},
    "bulk_10_discount": {"threshold": 20, "discount": 0.10},
    "tiered_50_discount": {"quantity_threshold": 30, "single_product_threshold": 15, "discount": 0.50}
}

#fees 
gift_wrap_fees = 1
shipping_fees_per_package = 5
units_per_package = 10


sub_total = 0
order_summary = []
total_price = 0
total_qty = 0
total_shipping_fees = 0
total_gift_wrap_fees = 0

eligible_discount = []
wrapped_gifts = 0

# Loop to input quantity of products
for product, price in catalog.items():
    qty = int(input(f'Enter quantity of {product}: '))
    gift_wrap = input(f'Is {product} gift wrapped ? (y/n) : ')
    
    if gift_wrap.lower() == 'y' :
        wrapped_gifts += 1
        
    
    
    total_price_for_product = qty * price
    sub_total += total_price_for_product
    
    order_summary.append((product, qty, total_price_for_product))
    total_qty += qty


    
    
#calculating total price 
def calculate_shipping_charge() :
    packages = total_qty//units_per_package
    shipping_fees = shipping_fees_per_package * packages
    
    return shipping_fees
    
    
total_shipping_fees = calculate_shipping_charge()

#fuction to calculate gift wrap fees 

def calculate_gift_wrap_charge() : 
     gift_wrap_charge = wrapped_gifts * gift_wrap_fees
     return gift_wrap_charge
 
total_gift_wrap_fees = calculate_gift_wrap_charge()


# Function to calculate flat 10 discount
def calculate_flat_10_discount():
    flat_10_discount_rate = 0
    if sub_total > discount_rules['flat_10_discount']['threshold'] :
        flat_10_discount_rate = discount_rules['flat_10_discount']['discount']
    eligible_discount.append({'flat_10_discount': flat_10_discount_rate})
    return flat_10_discount_rate

    
# Fuction to calculate bulk 5 discount       
def calculate_bulk_5_discount():
    total_bulk_5_discount_amount = 0
    for _, qty, price in order_summary :
        if qty > discount_rules['bulk_5_discount']['threshold'] :
            discount_amount = price * 0.05
            total_bulk_5_discount_amount += discount_amount
    eligible_discount.append({'bulk_5_discount':total_bulk_5_discount_amount})
    return total_bulk_5_discount_amount
    
#Fuction to calculate bulk 10 discount
def calculat_bulk_10_discount():
    bulk_10_discount_rate = 0
    if total_qty > discount_rules['bulk_10_discount']['threshold'] : 
        bulk_10_discount_rate = sub_total * discount_rules['bulk_10_discount']['discount']
    eligible_discount.append({'bulk_10_discount' : bulk_10_discount_rate })
    return bulk_10_discount_rate

#Fuction to calculate tiered 50 discount
def calculate_tiered_50_discount():
    tiered_50_discount_rate = 0
    for product, qty, _ in order_summary:
        product_price = catalog[product]
        if qty > discount_rules['tiered_50_discount']['single_product_threshold']:
            original_units = min(qty, discount_rules['tiered_50_discount']['single_product_threshold'])
            discounted_units = max(qty - discount_rules['tiered_50_discount']['single_product_threshold'], 0)
            discount_amount = (discounted_units * product_price * discount_rules['tiered_50_discount']['discount'])
            tiered_50_discount_rate += discount_amount
            
    eligible_discount.append({'tiered_50_discount' : tiered_50_discount_rate})
    return tiered_50_discount_rate
        


    
flat_10_discount_amount = calculate_flat_10_discount()       
bulk_5_discount_amount = calculate_bulk_5_discount()
bulk_10_discount_amount = calculat_bulk_10_discount()
tiered_50_discount_amount = calculate_tiered_50_discount()





#fuction to calculate total 

def calculate_total(subtotal, shipping_charge,gift_wrap_fees,flat_10_discount,bulk_5_discount,bulk_10_discount,tiered_50_discount) :  
    total_discount_amount = flat_10_discount + bulk_5_discount + bulk_10_discount + tiered_50_discount
    total = subtotal + shipping_charge + gift_wrap_fees - total_discount_amount         
    return total

total_price = calculate_total(
    sub_total,
    total_shipping_fees,
    total_gift_wrap_fees,
    flat_10_discount_amount,
    bulk_5_discount_amount,
    bulk_10_discount_amount,
    tiered_50_discount_amount
    )




#display details 
print('\nOrder Summary')
print('----------------------------')

for product, qty, total_price_for_product in order_summary:
    print(f'{product} x {qty}: ${total_price_for_product}')

print('----------------------------')
print(f'total quantity : {total_qty}')
print(f'Subtotal: ${sub_total}')

print('----------------------------')
print(f'shipping charge : ${total_shipping_fees}')
print(f'Gifts Wrapped charge : ${total_gift_wrap_fees}')

for discount in eligible_discount :
    for discount_rule, discount_rate in discount.items() :
        print(f'{discount_rule } : ${discount_rate}')
    

print('----------------------------')
print(f'Total Price : {total_price}')

