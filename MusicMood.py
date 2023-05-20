"""
Sanyerlis Camacaro - CSC235 - Sancamac@uat.edu Assignment:
How to use objects and Libraries in Python.

"Music Mood"
MusicMood is a unique application that suggests music based on your mood.

This code demonstrates how to:
Create a new Python application.
Give your program the ability to do new things and have new features using 3rd party libraries.
Give your program the ability to do new things and have new features using Python Objects.
Your application must do something innovative and interesting, not just demo libraries and objects.
Make a great User experience.
Over comment your code showing your intent and your understanding of what your code does.
"""

# Importing required third-party libraries
from textblob import TextBlob
from prettytable import PrettyTable


# Music library categorized by mood
class MusicLibrary:
    def __init__(self):
        # Using Python Dictionary object to store music data categorized by mood
        self.music_library = {
            "happy": ["Don't Stop Me Now - Queen", "Happy - Pharrell Williams", "I Wanna Dance with Somebody - Whitney Houston"],
            "sad": ["Someone Like You - Adele", "Say Something - A Great Big World", "The Sound of Silence - Simon & Garfunkel"],
            "neutral": ["Let It Be - The Beatles", "Imagine - John Lennon", "Counting Stars - OneRepublic"],
            "angry": ["Break Stuff - Limp Bizkit", "Given Up - Linkin Park", "Platypus (I Hate You) - Green Day"]
        }

    # Function to get music by mood
    def get_music(self, mood):
        # Lookup the music library with the provided mood
        # Returns an empty list if no matching mood is found
        return self.music_library.get(mood, [])


# Function to analyse user mood
def analyse_mood(user_text):
    # Using TextBlob for sentiment analysis
    blob = TextBlob(user_text)
    # Get the polarity of the sentiment
    polarity = blob.sentiment.polarity
    # Determine mood based on polarity
    if polarity > 0.5:
        return "happy"
    elif polarity < -0.5:
        return "angry"
    elif polarity == 0:
        return "neutral"
    else:
        return "sad"


# User interaction function
def interact_with_user():
    # Print introduction to the app
    print("\nWelcome to MusicMood!")
    print("\nMusicMood is a unique application that suggests music based on your mood.")
    print("\nTell us about your day, and we'll analyze your mood and suggest some music.")
    print("\nTo quit the application at any time, simply type 'quit'.")

    # Instantiate the music library
    music_library = MusicLibrary()
    while True:
        # User input
        user_text = input("\nTell me about your day, and I'll suggest some music: ")
        # If user wants to quit
        if user_text.lower() == "quit":
            print("\nThank you for using MusicMood! See you next time!")
            break
        # Analyse user mood
        mood = analyse_mood(user_text)
        # Get music suggestions
        music_suggestions = music_library.get_music(mood)
        # If there are music suggestions
        if music_suggestions:
            # Using PrettyTable to display data
            table = PrettyTable()
            table.field_names = ["Mood", "Music Suggestions"]
            for song in music_suggestions:
                table.add_row([mood.capitalize(), song])
            print("\nHere are some music suggestions for you:\n")
            print(table)
        else:
            print("\nSorry, I don't have any music suggestions for your current mood.")


# Run the user interaction function
if __name__ == "__main__":
    interact_with_user()
