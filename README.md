To run this code, you need Python 3 in your machine. To install the necessary packages, run the commands:
pip install tweepy
pip install better_profanity

Then, to run the code, run the command
python bot.py

This is a program designed to receive and output user submitted information about the current status of GMU Parking lots in real time. The bot currently will rank a lots fullness on a scale of 0-5, in which 0 is to represent an empty lot (every parking spot is open), and 5 representing a lot without any spaces available (every parking spot is filled). When running, the program should scan any messages sent to it for matching keywords and then act accordingly (either updating the appropriate lots, or sending out a message on the current lots availability)

Due to the current pandemic, we couldn't find easily accessible data to work with, so we focused on creating an easily expandable system that can be easily adjusted to refine both the heuristic classes information (defining a parking lots base level of fullness), and the parser's keywords its searching for.

There are two unit tests, that are the files apitest.py and filtertest.py
