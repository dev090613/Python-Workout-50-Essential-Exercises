MENU = {'sandwich': 10, 'tea': 7, 'salad': 9}

def restaurant():
    """Pseudo Code
    order = input
    if order in menu, Then print price and total. goto loop
    if order not in menu, Then scold. goto loop
    if order is empty string, Then break
    """
    total = 0
    while True:
        order = input("What is your order? ").lower().strip()
        if order == "":
            break
        elif order in MENU:
            total += MENU[order]
            print(f"price: {MENU[order]}, total: {total}")
        else:
            print("scold")
    msg = f"Total price is {total}"
    return msg

print(restaurant())
