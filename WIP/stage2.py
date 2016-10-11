#Stage 2, Final Project, "Fill-in-the-Blanks-Quiz"

blanks = ["___1___", "___2___", "___3___"]


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
def get_level(level):
    n = 0
    if level == "easy":
        print "You'll get 3 guesses"
        print easy_paragraph
        user_input = raw_input("You've chosen the easy level, fill in the answer for" + blanks[n] + ": " ).lower

        replaced = get_user_input(user_input)
        return easy_answers, easy_paragraph

    elif level == "medium":
        print "You'll get 3 guesses"
        user_input = raw_input("You've chosen the medium level, fill in the answer for" + blanks[n] + ":" ).lower
        replaced = get_user_input(user_input)
        print medium_paragraph
        return medium_answers, medium_paragraph

    elif level == "hard":
        print "You'll get 3 guesses"
        user_input = raw_input("You've chosen the hard level, fill in the answer for" + blanks[n] + ":" ).lower
        replaced = get_user_input(user_input)
        print hard_paragraph
        return hard_answers, hard_paragraph
    n = n + 1

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

def get_user_input(user_input):
    n = 0
    attempts = 3
    replaced = []

    while atempts < 3:
      if user_input == answers[n]:
        replaced = fill_blank_in_paragraph(paragraphs)

    else:
      user_input
      n = n + 1



def play_game():#start - ask what level
    level = raw_input ("Choose a level for this game: easy, medium, or hard: " ).lower()

    if level == "easy" or level == "medium" or level == "hard":
        answers, paragraphs = get_level(level)


    else:
        print "Try again"
        play_game()


play_game()














