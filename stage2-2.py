#Stage 2, Final Project, "Fill-in-the-Blanks-Quiz"

blanks = ["___1___", "___2___", "___3___","___4___"]

easy_paragraph = '''Bono is the lead singer of the band called "__1__". The happiest place on earth is "__2__". The color of grass is "__3__". The color of the sky is "__4__".'''
medium_paragraph ='''The first president of the US was "__1__". The second president of the US was "__2__". The third president of the US was "__3__". The first African-American president is "__4__.'''
hard_paragraph = '''The us has three branches of government, the "__1__" branch, the "__2__" branch, and the "__3__" branch. Who was the president who freed the slaves, __4__?'''

easy_answers = ['u2', 'disneyland', 'green', 'blue']
medium_answers = ['George Washington', 'John Adams', 'Thomas Jefferson','Barack Obama']
hard_answers = ['Executive', 'Legislative', 'Judicial','Abraham Lincoln']

#def start(user_input):
    #print 'pick a level: easy, medium, or hard' + user_input
def get_level(level):

    if level == "easy":
        return easy_answers, easy_paragraph

    elif level == "medium":
        return medium_answers, medium_paragraph

    elif level == "hard":
        return hard_answers, hard_paragraph


def match_items(a,b):
  for items in b:
    if items in a:
      return items
  return None

def fill_blank_in_paragraph(paragraphs):
  split_paragraph = paragraphs.split()
  for items in paragraphs:
    replacement = match_items(a,b)
    if replacement != None:
      items = items.replace(replacement, user_input)
      replaced.append(items)
  else:
      replaced.append(items)
  print fill_blank_in_paragraph(paragraphs,answers)

def quiz_answer(answers):
    index = 0
    attempts = 0
    replaced = []
    while attempts < 3:
        if guess_answer == answers[index]:
            print "Correct!"
            replaced = fill_blank_in_paragraph(paragraphs)
            index = index + 1
            if index < 4:
                guess_answer = raw_input("What should be filled: " + blanks[index])
                
            else:
                print "Great you're done!"
                break
        else:
            attempts = attempts + 1
            if attempts == 3:
                print "That's all folks!"

            else:
                print "This is your" + str(attempts)
                guess_answer = raw_input("What should be filled: " + answers[index])
            
    

def play_game():#start - ask what level
    level = raw_input ("Choose a level for this game: easy, medium, or hard: " )

    if level == "easy" or level == "medium" or level == "hard":
        answers, paragraphs = get_level(level)
        print paragraphs, 
        print "You get four guesses"
        replaced = quiz_answer(answers)


    else:
        print "Try again"
        play_game()


play_game()














