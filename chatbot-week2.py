# Yang Liu
# CMPT 120 D400
# January 19, 2022
# This program is a chatbot

def chatBot():
    
    # QUESTION 1 - Ask user for name
    print("Hi, welcome to Yang's chatbot!")
    print('May I please ask for your name?')
    users_name = input()

    print('Nice to meet you ' + users_name + '!')

    # QUESTION 2 - Ask user for favorite color
    print('Which color do you like the most out of red, green, and blue?')

    users_favorite_color = input()

    if users_favorite_color == 'red':
        print('Neat! I like red too, tomatoes are yummy.')
    elif users_favorite_color == 'green':
        print('Ooo green is a cool color, trees make me happy!')
    elif users_favorite_color == 'blue':
        print('Blue is my favorite color! The ocean is blue.')
    else:
        print("It seems like you wrote an option that wasn't provided :/")

    # QUESTION 3 - Ask user if they like coding
    print("The bot that you're talking to right now is written in Python, do you like programming too?")

    users_programming_interest = input()

    if users_programming_interest == 'yes' or users_programming_interest == 'Yes':
        print("Nice! Maybe you can look through my source code and see what I'm capable of!")
    else:
        print("That's fine, there are plenty of other cool hobbies out there too!")

    users_programming_interest_summary_sentence = ''
    # Check to see if user likes programming to prepare for ending summary sentence
    if users_programming_interest == 'yes' or users_programming_interest == 'Yes':
        users_programming_interest_summary_sentence = ' and you like programming!'
    else:
        users_programming_interest_summary_sentence = " and you don't enjoy programming but prefer other hobbies instead."

    # If user likes programming and user's favorite color is blue, they will be displayed a hidden message
    if users_favorite_color == 'blue' and (users_programming_interest == 'yes' or users_programming_interest == 'Yes'):
        print('Wow! You are just like me. My favorite color is blue and I too enjoy programming :)')

    print('It was great chatting with you, here are some things that I learned about you during this short time.')
    print('Your name is ' + users_name + ', your favorite color is ' + users_favorite_color + users_programming_interest_summary_sentence)

chatBot()