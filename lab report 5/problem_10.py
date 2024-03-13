# 10. Mr Rakib want to purchase four product items while minimizing cost. He wants to identify the
# minimum cost of the buying product in the market . SO the four items are Rice , Salt , Fish ,
# Orange.

products = {
    'Rice': [45, 42, 41, 40],
    'Salt': [34, 35, 36, 36],
    'Fish': [200, 202, 201, 205],
    'Orange': [100, 99, 101, 102]
}

product_name = input('Enter product name: ')

if product_name in products:
    prices = products[product_name]
    market = prices.index(min(prices)) + 1
    min_prince = min(prices)

    print(f'{product_name} -> market {market} value = {min_prince}')
else:
    print('Invalid product name !!!')
