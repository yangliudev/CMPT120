# Yang Liu
# CMPT 120 D400
# January 28, 2022
# This program is a chatbot

def music_chatbot():
    
    # QUESTION 1 - Ask for the user's name
    user_name = input("Welcome to Yang's music chatbot! Nice to meet you, may I ask for your name? ")
    print('Hello ' + user_name + '!')

    # Define list of music genres
    genres = ['pop', 'hip-hop', 'rap', 'rock', 'edm', 'metal', 'k-pop', 'classical', 'country', 'rnb']

    # QUESTION 2 - Get user's favorite genre
    fav_genre = input('What is your favorite genre of music? ').lower().strip("~!@#$%^&*()_+,./;'[]")

    if fav_genre in genres:
        print('Your favorite genre is amongst the popular ones!')
    else:
        print("Nice, you have a unique taste and have different preferences compared to the majority.")

    # Define list of instruments
    instruments = ['piano', 'violin', 'trumpet', 'clarinet', 'flute', 'saxophone', 'guitar']

    # QUESTION 3 - Get user's favorite instrument
    fav_instrument = input('What is your favorite instrument? ').lower().strip("~!@#$%^&*()_+,./;'[]")

    if fav_instrument in instruments:
        if fav_genre in genres:
            print('Your favorite instrument and genre are amongst the most popular ones!')
        else:
            print('Your favorite instrument is amongst the most popular ones!')
    else:
        print('Nice, you have a unique taste and have different preferences compared to the majority.')

    replies = [user_name, fav_genre, fav_instrument]

    print("It was fun getting to know you! I will now list out the things I've learned about you")

    for i in range(len(replies)):
        if i == 0:
            print('Your name is', replies[0])
        elif i == 1:
            print('Your favorite genre of music is', replies[1])
        elif i == 2:
            print('Your favorite instrument is', replies[2])
        
music_chatbot()
