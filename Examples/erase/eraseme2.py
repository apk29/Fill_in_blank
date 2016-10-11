quiz_questions = ["__1__", "__2__", "__3__", "__4__"]
quiz1_answers = ["Wrigley", "Chicago", "ivy", "Arrieta"]
quiz2_answers = ["goat", "Harry Carey", "Ferris Bueller", "Ryne Sandberg"]
quiz3_answers = ["1870", "1908", "1945", "let's play two"]

quiz1 = '''The Cubs play at __1__ Field in the city of __2__. Every spring the outfield walls becomed covered
with __3__, a trademark of the field.  In 2015 the Cubs had the best pitcher in the National League, Jake __4__,
who won the Cy Young Award.'''

def choose_level(level):
    if level == 'Double AA':
        print quiz1
        return level
    elif level == 'Triple AAA':
        print quiz2
        return level
    elif level == 'Major League':
        print quiz3
        return level
    else:
        return choose_level(raw_input ( 'Enter your level of expertise: Double AA, Triple AAA, Major League:'))
def check_answer1(answer):
    answer = str(answer)
    number_of_strikes = 0
    n = 0
    while number_of_strikes < 3:
        if answer == quiz1_answers[n]:
            print "That is correct!"
            answer_index = n
            print replace_blanks1(answer_index, quiz1)
            n = n + 1
            if n < 4:
                user_input = raw_input("What should fill in: " +quiz_questions[n]+"")
                answer = user_input
            else:
                print "That is correct! Congratulations you are a Diehard Cub Fan!  GO CUBS GO!"
                break
        else:
            number_of_strikes = number_of_strikes + 1
            if number_of_strikes == 3:
                print "Strike Three!  You are out!  Sorry you are not a diehard Cub fan!"

            else:
                print "Strike " + str(number_of_strikes) +"! Please Try Again."
                user_input = raw_input("What should fill in: " +quiz_questions[n]+"")
                answer = user_input

def word_transformer1(answer_index, blank):
    blank = str(blank)
    if blank == quiz_questions[answer_index]:
        return quiz1_answers[answer_index]
    else:
        return blank[0]

def replace_blanks1(x, quiz_filled_in):
    replacement = ""
    index = 0
    box_length = 5
    while index < len(quiz_filled_in):
        frame = quiz_filled_in [index: index + box_length]
        to_replace = word_transformer1(x, frame)
       
        replacement += to_replace
        if len(to_replace) == 1:
            index += 1
        else:
            index += 5
    
    return replacement

def play_game():
    level = choose_level(raw_input ('Choose your level of expertise. Type: Double AA, Triple AAA, Major League:'))
    n = 0
    user_input = raw_input("What should fill in w: "+quiz_questions[n]+"")
    word = user_input
    level = str(level)
    if level == 'Double AA':
        check_answer1(word)
    elif level == 'Triple AAA':
        check_answer2(word)
    elif level == 'Major League':
        check_answer3(word)
play_game()
