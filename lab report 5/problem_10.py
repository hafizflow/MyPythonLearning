# 10. Mr Rakib to purchase four product items while minimizing cost . He wants to identify the
# minimum cost of the buying product in the market . SO the four items are Rice , Salt , Fish ,
# Orange.

products = ['Rice', 'Salt', 'Fish', 'Orange']
stores = []

# Input prices for each product in different stores
for product in products:
    store_prices = {}
    print(f"Enter prices for {product} in different stores:")

    for i in range(1, 5):
        price = float(input(f"Enter price for {product} in Store {i}: "))
        store_prices[f'Store {i}'] = price

    stores.append(store_prices)

# Find the minimum cost for each product
min_costs = {}
for i, product in enumerate(products):
    min_store = min(stores, key=lambda x: x[f'Store {i + 1}'])
    min_costs[product] = (min_store, min_store[f'Store {i + 1}'])

# Print the results
for product, (store, price) in min_costs.items():
    print(f"For {product}, the minimum cost is {price} in {store}.")
