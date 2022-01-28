# Yang Liu
# CMPT 120 D400
# January 26, 2022
# This program is a chatbot

def yangChatbot():
    
    # Ask for the user's name
    user_name = input("Welcome to Yang's chatbot v2! Nice to meet you, may I ask for your name?")
    print('Hello ' + user_name + '!')

    # Define list of colors
    colors = ['red', 'green', 'blue', 'yellow', 'orange', 'pink', 'black', 'white']

    # QUESTION 1 - Get user's favorite color
    fav_color = input('What is your favorite color?').lower().strip("~!@#$%^&*()_+,./;'[]")

    print(fav_color)

yangChatbot()
