product_list = ["Laptop", "Mobile", "Headphones"]
cart_list = []
user_list = ["admin_user", "customer_1"]
order_list = []

while True:
    print("\n=== SHOPPING CART SYSTEM ===")
    print("1. ADMIN")
    print("2. USER")
    print("3. EXIT")
    role = input("Select Role (1-3): ")
   
    if role == '1':
        while True:
            print("\n--- ADMIN MENU ---")
            print("1. Add Product\n2. Update Product\n3. Remove Product\n4. View Products\n5. View Users\n6. Exit")
            choice = input("Enter choice (1-6): ")
            
            if choice == '1':
                new_product = input("Enter product name: ")
                product_list.append(new_product)
                print("Added successfully.")
                
            elif choice == '2':
                print("\n--- CURRENT PRODUCTS ---")
                for i in range(len(product_list)):
                    print(f"{i} : {product_list[i]}")
                idx=input("Enter position number to change (0, 1, 2..) or enter no to cancel:")
                if idx=='no':
                    print('update canceled')
                    continue
                new_value = input("Enter new name: ")
                product_list[idx] = new_value
                print(" Updated successfully.")
                
            elif choice == '3':
                print("\n--- CURRENT PRODUCTS ---")
                for i in range(len(product_list)):
                    print(f"{i} : {product_list[i]}")
                idx = int(input("Enter product position number to remove: "))
               
                product_list.pop(idx)
                print(" Removed successfully.")
                
            elif choice == '4':
                print("\n--- PRODUCTS ---")
                for item in product_list:
                    print(item)
                    
            elif choice == '5':
                print("\n--- USERS ---")
                for user in user_list:
                    print(user)
                    
            elif choice == '6':
                break

    
    elif role == '2':
        while True:
            print("\n--- USER MENU ---")
            print("1. View Products\n2. Add to Cart\n3. Remove from Cart\n4. View Cart\n5. Checkout\n6. Exit")
            choice = input("Enter choice (1-6): ")
            
            if choice == '1':
                print("\n--- AVAILABLE PRODUCTS ---")
                for i in range(len(product_list)):
                    print(f"{i} : {product_list[i]}")
                    
            elif choice == '2':
                print("\n--- AVAILABLE PRODUCTS ---")
                for i in range(len(product_list)):
                    print(f"{i} : {product_list[i]}")
                    
                idx = int(input("Enter product number to add (0, 1, 2..): "))
                if idx>=0 and idx<len(product_list):
                    cart_item = product_list[idx]
                    cart_list.append(cart_item)
                    print(f" Your product '{cart_item}' added to cart.")
                else:    
                    print("item not available")
                
            elif choice == '3':
                print("\n--- YOUR CART ---")
                
                for i in range(len(cart_list)):
                    print(f"{i} : {cart_list[i]}")
                
                idx = int(input("Enter item position number to remove from cart: "))
                cart_list.pop(idx)
                print(" Removed from cart.")
                
            elif choice == '4':
                print("\n--- YOUR CART ITEMS ---")
                for item in cart_list:
                    print(item)
                
            elif choice == '5':
                for item in cart_list:
                    order_list.append(item)
                
                while len(cart_list) > 0:
                    cart_list.pop()
                print(" Order placed and cart cleared.")
                
            elif choice == '6':
                print('Thank you')
                break
                
    elif role == '3':
        print("Goodbye!")
        break

