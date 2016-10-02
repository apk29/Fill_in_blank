##############################################
### PSEUDOCODE FOR P2 - CODE YOUR OWN QUIZ ###
##############################################

# define question for different levels
easy_paragraph = '''Bono is the lead singer of the band called "__1__". The happiest place on earth is "__2__". The color of grass is "__3__". The color of the sky is "__4__".'''
medium_paragraph ='''The first president of the US was "__1__". The second president of the US was "__2__". The third president of the US was "__3__". The first African-American president is "__4__.'''
hard_paragraph = '''The us has three branches of government, the "__1__" branch, the "__2__" branch, and the "__3__" branch. Who was the president who freed the slaves, __4__?'''

# define answers for the questions for the different levels
easy_answers = ['u2', 'disneyland', 'green', 'blue']
medium_answers = ['George Washington', 'John Adams', 'Thomas Jefferson','Barack Obama']
hard_answers = ['Executive', 'Legislative', 'Judicial','Abraham Lincoln']

# define the list of four blanks
blanks = ["___1___", "___2___", "___3___","___4___"]
          
# start the game by asking for the level
def get_level(level):
    if level == "easy":
        return easy_answers, easy_paragraph
    if level == "medium":
        return medium_answers, hard_paragraph
    if level == "hard":
        return hard_answer, hard_paragraph


    


def quiz_answers(answers,paragaphs):
    index = 0
    print answers
    for answer in answers:
        blank = blank[index]
        player_guess = raw_input("fill in the" + blank)
        while player_guess != raw_input("Try again: "):
        fill_blank_in_paragraph(paragraph)
        index = index + 1
        
def play_game():
    print "Please choose easy, medium, or hard"
    level = raw_input("type here:   ").lower()
      
    if level == "easy" or "medium" or "hard":
        answers, paragraphs = get_level(level)
        print paragraphs
        print "You get three guesses"

        replace = quiz_answer(answers,paragraphs)

    else:
        print "Try again"
        play_game() 

play_game()       
# start game in the selected difficulty
# take care to account for wrong inputs of the user
# display appropriate paragraph

# (OPTIONAL: show how many tries left)

# prompt for answer to the first blank

# if the answer is correct,
# congratulate
# fill the text with the correct word
# and show what is the next blank
def fill_blank_in_paragraph(answers, paragraphs,blanks):
    
# if the answer is wrong, prompt to try again on the same blank
# display the same text as before

# when all answers are correctly filled,
# show the full text
# and say a hearty congratulations!

# (OPTIONAL: if all tries are used up)
# (end game with message, and ask if the user wants to try again)
