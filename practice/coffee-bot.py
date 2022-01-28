def coffee_bot():

    cream = input("Hi I'm CoffeeBot. Would you like cream with your coffee? ").lower()

    if cream == 'yes':
        print("Here's your coffee with cream.")
    elif cream == 'no':
        print("Here's your coffee without cream.")
    else:
        print("I don't know what " + cream + " means.")

coffee_bot()