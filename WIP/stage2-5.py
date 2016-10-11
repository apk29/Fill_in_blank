#Stage 2, Final Project, "Fill-in-the-Blanks-Quiz"

blanks = ["__1__", "__2__", "__3__","__4__"]

easy_paragraph = ["Bono is the lead singer of the band called", "The happiest place on earth is",
"The color of grass is", "The color of the sky is"]

medium_paragraph =["The first president of the US was", "The second president of the US was",
"The third president of the US was", "The first African-American president is"]

hard_paragraph = ["The US has three branches of government, the president's branch is called the",
"The congressional branch is called the", "The supreme court is the","The 16th president of the us was"]

easy_answers = ['u2', 'disneyland', 'green', 'blue']
medium_answers = ['George Washington', 'John Adams', 'Thomas Jefferson','Barack Obama']
hard_answers = ['executive', 'legislative', 'judicial','Abraham Lincoln']

#def start(user_input):
    #print 'pick a level: easy, medium, or hard' + user_input

def end(paragraphs,answers):
    print ""
    print paragraphs[0] + " " + answers[0] + "." + " " + paragraphs[1] + " " +answers[1] + "." + " " + paragraphs[2] + " " + answers[2] + "." + " " + paragraphs[3] + " " + answers[3] + "."
    print ""
    print "Thanks for playing!"

def get_level(level): #3 one the has been chosen, this correlates the level to the level of the answers and paragraphs

    if level == "easy":
        return easy_answers, easy_paragraph
    elif level == "medium":
        return medium_answers, medium_paragraph
    elif level == "hard":
        return hard_answers, hard_paragraph

def answer_questions(answers,paragraphs,blanks):#7 this function takes care of which questions to ask, takes in answers, and determines what to do.
    index = 0
    question_count = 1
    blank_count = 0
    max_tries = 4
    attempts = 3
    chance = 2
    chances = 1
    while index < max_tries: #8 This gives players the number of tries they have.
        #9 the line below is asking for the player's input
        player_guess = raw_input("What is your answer for" + " " + blanks[index] + " " + "?" + " ")
        if player_guess == answers[index]: #9 if the player's input matches the answers list in the index postion, it executes the next few lines
            print "Correct" + "," + " " + str(paragraphs[index]) + " " + player_guess + "."
            print ""
            if question_count < max_tries: #10 this additonal if statement is needed for the line to execute properly
                print paragraphs[question_count] + " " + blanks[question_count] + "."
            index += 1
            question_count += 1
        else:#11 if the player's input doesn't match the answers list index, this is the next step
            blank_count = blank_count + 1
            if blank_count < attempts:
                if blank_count == chances: #account for chance vs chances, not necessary but grammatically correct
                    print "2 chances left"
                elif blank_count == chance:
                    print "1 chance left"
            else:
                print "Game over!"
                exit(0)

    end(paragraphs,answers)

def play_game():#1 start - ask what level inputs and correlates the definitions of the answers & paragraphs lists, starts the answers_questions function
    level = raw_input ("Choose a level for this game: easy, medium, or hard: " )
    print ""
    if level == "easy" or level == "medium" or level == "hard":
        answers, paragraphs = get_level(level) #2 this points to the get_level(level) function
        #4 the line below prints out the paragraphs (question) as determined by level.
        print paragraphs[0] + " " + blanks[0] + "." + " " + paragraphs[1] + " " + blanks[1] + "." + " " + paragraphs[2] + " " + blanks[2] + "." + " " + paragraphs[3] + " " + blanks[3] + "."
        print "" #5 this prints out a blank line to seperate, so its not bunched up all together.
        #6 anser_question is the next function to goto
        answer_questions(answers,paragraphs,blanks)

    else:
        print "Try again"
        play_game()

play_game()

