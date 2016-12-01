# game exercise for part 36

# Task 1: import modules
from sys import exit

player_score = 0

player_strikes = 0

# Task 2: define start
def start(player_name):
    print "Welcome to LyriKing, %s" % player_name
    print "This is the Easy Listening Room"
    print "Read the lyrics carefully and then make your decision."
    print "Good luck!"
    print "Truly Madly Deeply - Savage Garden"
    print "\nI'll be your hope, I'll be your love be everything that you need."
    print "\nNow choose the line that comes after:"

    print "1: I want to stand with you on a mountain."
    print "2: I love you more with every breath truly madly deeply do.."
    print "3: I love you with every breath truly sadly deeply do.."

    choice = raw_input("Pick a number> ")

    if "2" in choice:
        score = score + 1
        print "Excellent work! Go to question two."
        print player_score
        question_two(player_name, score, strikes)
    elif "1" in choice or "3" in choice:
        strikes = strikes + 1
        print "That was incorrect. You get a strike."
        question_two(player_name, score, strikes)
    elif "1" not in choice or "2" not in choice or "3" not in choice:
        print "You need to choose between 1, 2 or 3."
        start(player_name)
    else:
        dead(0)

# task 4: define questions
def question_two(player_name, score, strikes):

    print "%s, you have %d points and %d strikes." % (player_name, score, strikes)

    print "Lead Me On - Maxine Nightingale"
    print "\nCome on and tease me all night long"
    print "\nChoose the correct lyric that follows:"

    print "1: Lovin' you I know it's right"
    print "2: Come on and lead me on"
    print "3: Time goes on, seems nothing's changed"

    choice = raw_input("Pick a number> ")

    if "1" in choice:
        print "That is correct, you're awesome!"
        score = score + 1
        question_three(player_name, score, strikes)
    elif "2" or "3" in choice:
        print "I'm sorry, that is not correct."
        strikes = strikes + 1
        question_three(player_name, score, strikes)
    else:
        print "Please pick either 1, 2 or 3"
        question_two(player_name, score, strikes)


def question_three(player_name, score, strikes):
    print "Yay, %s! Question three with %s points and %s strikes" % (player_name, score, strikes)

# task 3: define dead
def dead():
    print "Goodbye."
    exit(0)

print "Welcome."
print """
You will be asked to read a line from a song
and then identify the line that comes right
after it.
"""
print "What is your name?"
player_name = raw_input("> ")
start(player_name)
