def make_coffee(water_boiled, add_milk, add_sugar):
    """
    Function to make coffee based on whether the water is boiled, and whether milk and sugar are added.

    Args:
    water_boiled (bool): True if the water is boiled, False otherwise.
    add_milk (bool): True if milk should be added, False otherwise.
    add_sugar (bool): True if sugar should be added, False otherwise.

    Returns:
    str: Description of the coffee making status.
    """
    if not water_boiled:
        return "Please boil the water."

    coffee = "Coffee with hot water"
    
    if add_milk and add_sugar:
        coffee += ", milk, and sugar."
    elif add_milk:
        coffee += " and milk."
    elif add_sugar:
        coffee += " and sugar."
    else:
        coffee += "."

    return coffee

# Example usage:
print(make_coffee(True, True, True))
