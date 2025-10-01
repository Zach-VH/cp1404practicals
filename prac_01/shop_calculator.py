"""
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total
before the amount is displayed on the screen.
"""

#variables
item_price_list = []
MENU = """A - Add item to list
C - Calculate total cost
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()

#shopping calculator
while choice != "Q":
    if choice == "C":
        if not item_price_list:
            print("Item list empty. Add item to list before using calculator.")
        else:
            total_cost = sum(item_price_list)
            if total_cost > 100:
                total_cost = total_cost*0.9

            print(f"Number of items: {len(item_price_list)}",end='\n')
            for i in range(0,len(item_price_list),1):
                print(f"Item {i+1} cost: ${item_price_list[i]:.2f}",end='\n')
            print(f"Total price: ${total_cost:.2f}",end='\n')
    elif choice == "A":
        item_price_list.append(float(input("Enter cost of item: $")))
    else:
        print("Invalid Option")
    print(MENU)
    choice = input(">>> ").upper()
print("Goodbye")