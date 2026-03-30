# Function to add items to the cart
def add_items():
    cart = []  # list to store items

    # Take number of items from user
    n = int(input("Enter number of items: "))

    # Loop to take input for each item
    for i in range(n):
        print(f"\nItem {i+1}")

        # Taking item details
        name = input("Enter item name: ")
        price = float(input("Enter price: "))
        qty = int(input("Enter quantity: "))

        # Append item as a list [name, price, quantity]
        cart.append([name, price, qty])

    return cart  # return the cart


# Function to display cart items
def view_cart(cart):
    print("\n--- Cart Items ---")

    # Loop through each item and print details
    for item in cart:
        print(f"Name: {item[0]} | Price: {item[1]} | Qty: {item[2]}")


# Function to calculate total price
def calculate_total(cart):
    total = 0  # initialize total

    # Loop to calculate total = price * quantity
    for item in cart:
        total += item[1] * item[2]

    return total  # return total price


# Function to apply discount based on total amount
def apply_discount(total):

    # Apply discount rules
    if total >= 1000:
        discount = 0.20   # 20% discount
    elif total >= 500:
        discount = 0.10   # 10% discount
    else:
        discount = 0      # no discount

    # Calculate final price after discount
    final_price = total - (discount * total)

    return final_price, discount


# ---------------- MAIN PROGRAM ----------------

# Step 1: Add items to cart
cart = add_items()

# Step 2: Display cart
view_cart(cart)

# Step 3: Calculate total bill
total = calculate_total(cart)
print(f"\nTotal Price: {total}")

# Step 4: Apply discount
final_price, discount = apply_discount(total)

# Step 5: Display final results
print(f"Discount Applied: {discount * 100}%")
print(f"Final Price: {final_price}")