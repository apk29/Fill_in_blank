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

def get_level(level):

    if level == "easy":
        return easy_answers, easy_paragraph        
    elif level == "medium":        
        return medium_answers, medium_paragraph        
    elif level == "hard":       
        return hard_answers, hard_paragraph
    
def answer_questions(answers,paragraphs,blanks):
    index = 0 
    question_count = 1
    blank_count = 0

    while index < 4:
        guesses = []
        player_guess = raw_input("What is your answer for" + " " + blanks[index] + " " + "?" + " ")
        if player_guess == answers[index]:
            print "Correct!"
            print str(paragraphs[index]) + " " + player_guess + "."
            print ""
            if question_count < 4:
                print paragraphs[question_count] + " " + blanks[question_count] + "."
            index += 1
            question_count += 1
        else:
            blank_count = blank_count + 1
            if blank_count < 3:
                if blank_count > 1:
                    print str(3-blank_count) + " chance left"
                else:
                    print str(3-blank_count) + " chances left"
            else:
                print "Game over!"
                exit(0)
                       
    end(paragraphs,answers)
    
def play_game():#start - ask what level
    level = raw_input ("Choose a level for this game: easy, medium, or hard: " )
    print ""
    if level == "easy" or level == "medium" or level == "hard":
        answers, paragraphs = get_level(level)
        print paragraphs[0] + " " + blanks[0] + "." + " " + paragraphs[1] + " " + blanks[1] + "." + " " + paragraphs[2] + " " + blanks[2] + "." + " " + paragraphs[3] + " " + blanks[3] + "."
        print ""                  
        answer_questions(answers,paragraphs,blanks)

    else:
        print "Try again"
        play_game()

play_game()

