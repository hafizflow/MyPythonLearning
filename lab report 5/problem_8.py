# 8.There is a grocery shop which takes regular input from customers. After taking items if they want
# to add or remove items from their bucket list. We have to generate a program in python.

bucket = []

while True:
    print('\nGrocery Shop Management')
    print('Enter 1 to add product')
    print('Enter 2 to remove product')
    print('Enter 3 to display product')
    print('Enter 4 to Exit')
    choice = int(input('Enter your choice (1-5): '))

    if choice == 1:
        bucket.append(input('Enter product name: '))
        print('Product added to bucket successfully')
    elif choice == 2:
        remove_product = input('Enter product name: ')
        if remove_product not in bucket:
            print('The product is not in the bucket !!!')
        else:
            bucket.remove(remove_product)
            print('Product removed from bucket successfully')
    elif choice == 3:
        print(f'Item in the bucket are: {bucket}')
    elif choice == 4:
        print('Thank you. See you soon')
        break
    else:
        print('Invalid choice, Please choose between 1-4')
