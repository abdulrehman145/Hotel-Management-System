import pyttsx3
import datetime

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak and display text
def say_and_show(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
    
# Function to save files according to dates and orders for the day
def save_file(order,quantity,bill):
    date=datetime.datetime.now().strftime('%Y-%m-%d')
    time=datetime.datetime.now().strftime('%H:%M:%S')
    filename=(f"{date}.txt")
    order_details=(f"""\n\n\t ORDER TIME \t{time}
\t ORDER = {order} \t QUANTITY = {quantity} \t BILL = {bill}""") 
    try:
        with open(f"{filename}", "a") as f:
            f.write(order_details)
    except FileNotFoundError:
        with open(f"{filename}", "w") as f:
             f.write(f"""\n\n\t ORDER TIME \t{time}
\t ORDER = {order} \t QUANTITY = {quantity} \t BILL = {bill}""")

        
        

# Function to speak text and take user input
def say_and_input(text):
    engine.say(text)
    engine.runAndWait()
    user_input = input(text)
    return user_input

# Menu dictionaries
dict_menu = {"coffee": 1, "burger": 2, "drink": 3, "pizza":4}  # Menu items with associated IDs
priced_menu = {1: 150, 2: 300, 3: 70, 4:1800}  # Prices for menu items

# Taking order
say_and_show("""\t WELCOME TO OUR DRIVE THRU \t\n
             \tHere is Our Menu\t\n
             \tCOFFEE   RS.150\t
             \tBURGER   RS.300\t
             \tDRINK    RS.70\t
             \tPIZZA    RS.1800\t\n""")
order = say_and_input("What will you like to have, sir?: ").lower()
if order in dict_menu:
    quantity = int(say_and_input("How many, sir?: "))
    item = dict_menu[order]
    price = priced_menu[item]
    bill = quantity * price

    order2 = say_and_input("Of course, sir! Do you want to order something else?: ").lower()
    if order2 in dict_menu:
        quantity2 = int(say_and_input("How many, sir?: "))
        item2 = dict_menu[order2]
        price2 = priced_menu[item2]
        bill2 = quantity2 * price2
        total_bill = (bill+bill2)
        total_quantity=(f"{quantity} , {quantity2}")
        full_order=(f"{order} ,{order2}")
        say_and_show(f"Here is your total, sir: {total_bill}")
        save_file(full_order,full_order,total_bill)
    else:
        say_and_show(f"Here is your total, sir: {bill}")
        say_and_show("Thanks, sir! Hope you enjoy your order.")
        save_file(order,quantity,bill)
else:
    say_and_show("Sorry, sir, you can see our menu again:")
    for item in dict_menu:
        say_and_show(f"{item.capitalize()}")

