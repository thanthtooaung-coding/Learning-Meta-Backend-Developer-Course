menu = {
    1: {"name": 'espresso', "price": 1.99},
    2: {"name": 'coffee', "price": 2.50},
    3: {"name": 'cake', "price": 2.79},
    4: {"name": 'soup', "price": 4.50},
    5: {"name": 'sandwich', "price": 4.99}
}

def calculate_subtotal(order):
    """Calculates the subtotal of an order.

    [IMPLEMENT ME]
        1. Add up the prices of all items in the order.
        2. Round the result to 2 decimal places and return it.

    Args:
        order (list): A list of dicts, where each dict represents an item with a name and price.

    Returns:
        float: The subtotal of all item prices, rounded to 2 decimal places.
    """
    print('Calculating bill subtotal...')
    ### WRITE SOLUTION HERE
    subtotal = sum(item['price'] for item in order)
    return round(subtotal, 2)


def calculate_tax(subtotal):
    """Calculates the tax of an order.

    [IMPLEMENT ME]
        1. Calculate 15% of the subtotal.
        2. Round the tax to 2 decimal places and return it.

    Args:
        subtotal (float): The subtotal amount.

    Returns:
        float: The calculated tax amount, rounded to 2 decimal places.
    """
    print('Calculating tax from subtotal...')
    ### WRITE SOLUTION HERE
    tax = subtotal * 0.15
    return round(tax, 2)


def summarize_order(order):
    """Summarizes the order.

    [IMPLEMENT ME]
        1. Calculate subtotal and tax.
        2. Compute the total (subtotal + tax) and round to 2 decimal places.
        3. Extract the item names and return them with the total.

    Args:
        order (list): A list of dicts, where each dict represents an item with a name and price.

    Returns:
        tuple: A list of item names and the total amount (rounded to 2 decimal places).
    """
    print_order(order)
    ### WRITE SOLUTION HERE
    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)
    total = round(subtotal + tax, 2)

    item_names = [item["name"] for item in order]

    return item_names, total


# This function is provided for you and will print out the items in an order
def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = [item["name"] for item in order]
    print(items)
    return order

# This function is provided for you and will display the menu
def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

# This function is provided for you and will create an order by prompting the user to select menu items
def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        attempts = 3
        while attempts > 0:
            try:
                item = int(input(f'Select menu item number {count} (from 1 to 5): '))
                if item in menu:
                    order.append(menu[item])
                    count += 1
                    break
                else:
                    print("Invalid selection. Please choose a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")

            attempts -= 1
            if attempts == 0:
                print("Too many invalid attempts. Moving to the next item.")

    return order


'''
Here are some sample function calls to help you test your implementations.
Feel free to change, uncomment, and add these as you wish.
'''
def main():
    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))

    tax = calculate_tax(subtotal)
    print("Tax for the order is: " + str(tax))

    names, total = summarize_order(order)
    print(f"Order summary: Items: {names}, Total: {total}")

if __name__ == "__main__":
    main()
