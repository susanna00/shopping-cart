# shopping_cart.py

import datetime as dt

TAX_RATE = 0.06


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coco1nut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#
# Information input
#

checkout_start_at = dt.datetime.now()
subtotal_price = 0
selected_ids = []

while True:
    selected_id = input("Please input a product identifier, or 'DONE' if there are no more identifier:") #> "g" (string)
    if selected_id == "DONE":
        break
    else:
        selected_ids.append(selected_id)


#
# Information output
#

print("---------------------------------")
print("ITALIAN GROCERY")        # Print a grocery store name of your choice
print("---------------------------------")
print("Phone Number: +1 (202)-364-0187") 
print("Website: WWW.SHOP-ITALIAN-GROCERY.COM") 
print("Address: 3700 O Str N.W. Washington, D.C. 20057")      # A grocery store  website URL and address of choice
print("---------------------------------")
print("Checkout Time: " + checkout_start_at.strftime("%Y-%m-%d %I:%M %p"))        # The date and time of the beginning of the checkout process, formatted in a human-friendly way
print("---------------------------------")


# Name and price of each shopping cart item

def to_usd(my_price):
    return f"${my_price:,.2f}" # Price formatted as US dollars and cents

print("Shopping Cart Items:")

for selected_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    subtotal_price = subtotal_price + matching_product["price"]
    print("..." + matching_product["name"] + " (" + to_usd(matching_product["price"]) + ")")

tax = subtotal_price * TAX_RATE

total_price = subtotal_price + tax 

print("---------------------------------")
print("SUBTOTAL: " + to_usd(subtotal_price))        # The total cost of all shopping cart items
print("TAX: " + to_usd(tax))        # The amount of tax owed
print("TOTAL: " + to_usd(total_price))      # The total amount owed, formatted as US dollars and cents
print("---------------------------------")
print("Thank you for shopping with us, we hope to see you soon!")       # A friendly message thanking the customer and/or encouraging the customer to shop again
print("---------------------------------")



