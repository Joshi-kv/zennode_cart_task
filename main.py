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



# Loop to input quantity of products
for product, price in catalog.items():
    qty = int(input(f'Enter quantity of {product}: '))
    total_price_for_product = qty * price
    sub_total += total_price_for_product
    
    order_summary.append((product, qty, total_price_for_product))

print('\nOrder Summary')
print('------------------')

for product, qty, total_price_for_product in order_summary:
    print(f'{product} x {qty}: ${total_price_for_product}')

print('------------------')
print(f'Subtotal: ${sub_total}')
    
    




        

