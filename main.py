#catalog 

catalog = {
    'Product A' : 20,
    'Product B' : 40,
    'Product C' : 50,
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

#fuction to calculate total 

def calculate_total(subtotal, shipping_charge,gift_wrap_fees) : 
    if shipping_charge >= 1 :
        total = subtotal + shipping_charge
    if gift_wrap_fees >= 1 :
        total = subtotal + shipping_charge + gift_wrap_fees
    else :
        total = subtotal
    return total

total_price = calculate_total(sub_total,total_shipping_fees,total_gift_wrap_fees)




#display details 
print('\nOrder Summary')
print('----------------------------')

for product, qty, total_price_for_product in order_summary:
    print(f'{product} x {qty}: ${total_price_for_product}')

print('----------------------------')
print(f'Subtotal: ${sub_total}')

print('----------------------------')
print(f'shipping charge : ${total_shipping_fees}')
print(f'Gifts Wrapped charge : ${total_gift_wrap_fees}')

print('----------------------------')
print(f'Total Price : {total_price}')