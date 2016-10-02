def menu():
    '''list of options of unit types to have converted for the user
    ex:
    >>> _1)Length
        _2)Tempurature
        _3)Volume
    '''

    print('_1)Length\n' '_2)Temperature\n' '_3)Volume\n' '_4)Mass\n' '_5)Area\n'
          '_6)Time\n' '_7)Speed\n' '_8)Digital Storage\n')

    ask_user()
    sub_menu(user_input)

def ask_user():
    ''' asks the user what units they would like converted
    ex:
    >>> what units do you need to convert? meter, feet
    >>> 3.281
    '''
    user_input = input("Make a selection: ")
    print ("you entered",  user_input)
    #conversion(user_input)
    return user_input

def convert_meters_to_feet(num):
    '''converts a user determined ammount of meters into feet
    ex:
    >>> convert_meters_to_feet(50)
    >>> 164.042
    '''

    num_feet = num * 3.28084
    print(num_feet)


def convert_fahrenheit_to_celsius(num):
    '''converts a user determined temperature in fahrenheit to celsius
    ex:
    >>> convert_fahrenheit_to_celsius(60)
    >>> 15.6
    >>> convert_fahrenheit_to_celsius(32)
    >>> 0
    '''

    degree_celsius = (num - 32) * (5/9)
    print(round(degree_celsius, 2))


def sub_menu(num):
    '''routes the user from the main menu to a sub menu based on
    their first selection'''

    if user_input == '1':
        print('_1)Kilometers\n' '_2)Meters\n' '_3)Centimeters\n' '_4)Millimeters\n'
              '_5)Mile\n' '_6)Yard\n' '_7)Foot\n' '_8)Inch\n' '_9)Nautical Mile\n')

        ask = input('Make a selection (starting unit)')
        return
    if user_input == '2':
        print('_1)Fahrenheit\n' '_2)Celsius\n' '_3)Kelvin\n')
        ask = input('Make a selection (starting unit)')
        return

"""quiz_questions = ["__1__", "__2__", "__3__", "__4__"]
quiz1_answers = ["Wrigley", "Chicago", "ivy", "Arrieta"]

quiz1 = '''The Cubs play at ___1___ Field in the city of ___2___. Every spring the outfield walls becomed covered
with __3__, a trademark of the field.  In 2015 the Cubs had the best pitcher in the National League, Jake __4__,
who won the Cy Young Award.'''

quiz2 = "Blah blah blah"
quiz3 = "Go Cubs Go"

def choose_level(level):
    if level == 'newbie':
        print quiz1
    elif level == 'seasoned':
        print quiz2
    elif level == 'master':
        print quiz3
    else:
        return choose_level(raw_input ( 'Enter your level of expertise: newbie, seasoned, master:'))

def check_answer(answer):
    answer = str(answer)
    number_of_tries = 3
    n = 0
    while number_of_tries > 0:
        if answer == quiz1_answers[n]:
            n = n + 1
            if n < 5:
                print "That is correct!"
                user_input = raw_input("What should fill in: " +quiz_questions[n]+"")
                answer = user_input
            else:
                print "That is correct! Congratulations you are a Diehard Cub Fan!  GO CUBS GO!"

        else:
            number_of_tries = number_of_tries - 1
            if number_of_tries == 0:
                print "Game Over!  Sorry you are not a diehard Cub fan!"

            else:
                print "Please Try Again.  You have : " + str(number_of_tries) + " strikes left!"
                user_input = raw_input("What should fill in: " +quiz_questions[n]+"")
                answer = user_input


def play_game():
    level = choose_level(raw_input ('Choose your level of expertise. Type newbie, seasoned, master:'))
    n = 0
    user_input = raw_input("What should fill in: "+quiz_questions[n]+"")
    word = user_input
    check_answer(word)

play_game()


   attempts = 3
   for each blank in the blanks
        get answer for blank
        match the answer with answers
        if answer matches, replace blank with the answer
        ask what the next blank is
        if answer is wrong, ask the question again with the raw_input

for each blank in blank:
while (answer is wrong   &&   attempts <3)

get input

for each blank in blank:
while (answer is wrong   &&   attempts <3)
get answer
def get_answer(answers):
   ask = str(ask)
   replace = []
   index = 0
   attempts = 0
   while attempts < 3:
       if ask != answers[index]:
           attempts += 1

   for items in blanks:
       ask = raw_input("Please fill in the answer for" + items + ".").lower
       while ask != answers(index):
           ask = raw_input("Please fill in the answer for" + items + ".").lower
       index += 1"""