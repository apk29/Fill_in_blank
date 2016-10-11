#Load Global Vars Here
easy_questions = ["This is a", "So is", "This is a", "So is"]
easy_answers = ["question", "this", "question", "this"]
medium_questions = ["What is", "This is", "What is", "This is", ]
medium_answers = ["that", "this", "that", "this"]
hard_questions = [""]
hard_answers = [""]
blanks = ["__1__", "__2__", "__3__", "__4__"]
#When win condition is met this function is called.
def win():
    print "\n"
    print "Congrats! You have got all questions correct!"
    choice = raw_input("Would you like to play again? (y/n): ")
    if choice == "y":
        welcome()
    if choice == "n":
        print "Ok thanks for playing, goodbye!"
        exit()
    else:
        print "Invalid choice, please try again \n"
        win()
def check(questions, answers):
    questions_counter = 0
    answers_counter = 1
    while questions_counter < 4:
        print "What is", answers_counter, "?"
        answer_input = raw_input("")
        print questions[questions_counter], answer_input
        check = raw_input("is this correct? y/n ")
        if check == 'y':
            if answer_input == answers[questions_counter]:
                print 'Correct! \n'
                questions_counter +=1
                answers_counter +=1
            else:
                print 'Sorry try again! \n'
    for x, y in zip(questions, answers):
        print x, y
    win()

def quiz(questions, answers, blanks):
    
    question_blanked = zip(questions, blanks)
    print "\n"
    for x, y in question_blanked: #x and y are just placeholder vars
        print x, y
    print "\n"
    check(questions, answers)
#This function loads the proper lists to be passed around depending on difficulty
#selected
def welcome():
    print "Welcome to Phil's quiz v.9!"
    difficulty_select = raw_input("Please choose a difficulty(easy, medium, hard): ")
    if difficulty_select == "easy":
        quiz(easy_questions, easy_answers, blanks)
    if difficulty_select == "medium":
        quiz(medium_questions, medium_answers, blanks)
    if difficulty_select == "hard":
        quiz(hard_questions, hard_answers, blanks)
    else:
        print "Invalid entry please try again \n"
        welcome()
welcome()
