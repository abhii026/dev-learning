# restaurant_menu = {
#     "Paneer Butter Masala": 180,
#     "Chicken Biryani": 220,
#     "Veg Fried Rice": 140,
#     "Masala Dosa": 100,
#     "Cold Coffee": 80,
#     "Gulab Jamun": 60
# }
# print("Welcome to Abhi Restaurant\n\nMenu")
# print("Paneer Butter Masala: ₹180\nChicken Biryani: ₹220\nVeg Fried Rice: ₹140\nMasala Dosa: ₹100\nCold Coffe: ₹80\nGulab Jamun: ₹60")
# order_total=0;
# item=input("Select order from menu: ")
# if item in restaurant_menu:
#     order_total+=restaurant_menu[item]
#     print(f"Your item is {item} and total amount is {order_total}")
# else:
#     print(f"!! Sorry ! {item} is not available in the menu.")


restaurant_menu = {
    "Paneer Butter Masala": 180,
    "Chicken Biryani": 220,
    "Veg Fried Rice": 140,
    "Masala Dosa": 100,
    "Cold Coffee": 80,
    "Gulab Jamun": 60
}

print("Welcome to Abhi Restaurant\n\nMenu")
for item, price in restaurant_menu.items():
    print(f"{item}: ₹{price}")

order_total = 0

while True:
    item = input("\nSelect an item from the menu: ")

    if item in restaurant_menu:
        order_total += restaurant_menu[item]
        print(f"{item} added! Current total: ₹{order_total}")
    else:
        print(f"!! Sorry ! {item} is not available in the menu.")

    choice = input("Do you want to order more? (yes/no): ").strip().lower()
    if choice != "yes":
        break

print(f"\nThank you for ordering! Your final bill is ₹{order_total}")
