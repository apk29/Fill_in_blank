blanks = ["___1___", "___2___", "___3___", "___4___"]


easy_paragraph = '''Bono is the lead singer of the band called "__1__". The happiest place on earth is "__2__". The color of grass is "__3__".'''
medium_paragraph ='''The first president of the US was "__1__". The second president of the US was "__2__". The third president of the US was "__3__".'''
hard_paragraph = '''The us has three branches of government, the "__1__" branch, the "__2__" branch, and the "__3__" branch. '''

paragraphs = ['easy_paragraph', 'medium_paragraph', 'hard_paragraph']

easy_answers = ['u2', 'disneyland', 'green']
medium_answers = ['George Washington', 'John Adams', 'Thomas Jefferson']
hard_answers = ['Executive', 'Legislative', 'Judical']

answers = ['easy_answers', 'medium_answers', 'hard_answers']

#def start(user_input):
    #print 'pick a level: easy, medium, or hard' + user_input
def get_level(level):  #[JK] (2) EXECUTION JUMPS HERE WHEN THE FUNCTION IS CALLED (from line 79).  Let's say the level is medium.
    if level == "easy":  #[JK] (2a) check if level is easy.  False, Level is not "easy," so skip this block, and check the next block
        print "You've chosen the easy level, it's a piece of cake!"
        print easy_paragraph
        print "You'll get 5 guesses"


    elif level == "medium":  #[JK] (2b1) Yes, level == "medium" returns true, so execute this block
        print "You've chosen the medium level, hope you know your US presidents!"
        print medium_paragraph
        print "You'll get 5 guesses"   #[JK] (2b2) finish this block, there is nothing left, so RETURN TO LINE 79 where this function was called.

    elif level == "hard":
        print "You've chosen the hard level, that civics class will come in handy!"
        print hard_paragraph
        print "You'll get 5 guesses"

    else:
        play_game()


def items_in_blanks(word, blanks):
    for blank in blanks:
        if blank in word:
            return blank
    return None

def get_answer(answer,question):
    replaced = []
    user_answer = ""

    index = 0
    for blank in blanks:
        # Where the questions and answers gets stated.
        question = "What is your answer for " + blank + "?"
        print question
        user_answer = raw_input("Type here: ")
        user_answer = user_answer.lower()

        while user_answer != answers[index]:
            print "Your answer was wrong. Please try again."
            user_answer = raw_input("Type it here again: ")
            user_answer = user_answer.lower()

        print "Awesome, that's correct!"

        replaced = fill_in_answers(paragraph, blanks, replaced, user_answer, index)
        print replaced

        index += 1

    return replaced, index





def play_game():  #[JK] (1) EXECUTION JUMPS HERE FROM LINE 86 IN THE CALL TO play_game().
    level = raw_input ("Choose a level for this game: easy, medium, or hard: " ).lower()

    if level == "easy" or level == "medium" or level == "hard":
        get_level(level)  #[JK] (1a) if the user enters "easy," "medium", or "hard," this block will be executed.  call to get_level() will JUMP TO LINE 18 where get_level is defined, passing "level" as our input to the function.
							#[JK] (3) RETURNING AFTER EXECUTING get_level(), THERE IS NOTHING LEFT TO EXECUTE IN THIS FUNCTION, SO WE RETURN BACK TO WHERE play_game() was called, line 86.
    else:
        print "Try again"
        play_game()  #[JK] (1b) if the user inputs something other than "easy," "medium," or "hard," execution jumps here, and points us back to line 75,
        replaced = get_answer(answer,question)

play_game()     #[JK] (0) Execution starts here.  JUMP TO LINE 75 WHERE THIS FUNCTION IS DEFINED.  Return back here when function play_game() finishes executing.
				#[JK] (4) Nothing left to execute.  Done.


    #userInput = inpur (0,1)
    #if userInput = 0:
        #return "kayak"
        #if userInput = 1:
            #return "udacious"
        #else:
            #return "something else"
"""n = 0
        blank_answer = user_input
        user_input = raw_input("Type in your answer for" + blanks[n] + "")"""