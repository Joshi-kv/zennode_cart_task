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
total_packages = 0



# Loop to input quantity of products
for product, price in catalog.items():
    qty = int(input(f'Enter quantity of {product}: '))
    total_price_for_product = qty * price
    sub_total += total_price_for_product
    
    order_summary.append((product, qty, total_price_for_product))
    total_qty += qty

print('\nOrder Summary')
print('------------------')

for product, qty, total_price_for_product in order_summary:
    print(f'{product} x {qty}: ${total_price_for_product}')

print('------------------')
print(f'Subtotal: ${sub_total}')
    
    
#calculating total price 
def calculate_shipping_charge() :
    packages = total_qty//units_per_package
    shipping_fees = shipping_fees_per_package * packages
    return shipping_fees
    
total_shipping_fees = calculate_shipping_charge()
print('----------------')
print(f'shipping charge : ${total_shipping_fees}')
        
# calculate_shipping_charge()

        
# def calculate_total(subtotal, shipping_fees) :
#     total = subtotal + shipping_fees
#     return total

# total_price = calculate_total(sub_total,calculate_shipping_charge)
# print(total_price)
