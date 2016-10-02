easy_paragraph = '''Bono is the lead singer of the band called "__1__". The happiest place on earth is "__2__". The color of grass is "__3__".'''
medium_paragraph ='''The first president of the US was "__1__". The second president of the US was "__2__". The third president of the US was "__3__".'''
hard_paragraph = '''The us has three branches of government, the "__1__" branch, the "__2__" branch, and the "__3__" branch. '''

#-# what is this list used for?
# paragraphs = ['easy_paragraph', 'medium_paragraph', 'hard_paragraph']

easy_answers = ['u2', 'disneyland', 'green']
medium_answers = ['George Washington', 'John Adams', 'Thomas Jefferson']
hard_answers = ['Executive', 'Legislative', 'Judicial']

#-# what is this list used for?
# answers = ['easy_answers', 'medium_answers', 'hard_answers']



#-# added a list for blanks here
#-# watch out you'll need 4 blanks each to pass the rubric
blanks = ["__1__", "__2__", "__3__"]



#-# remove legacy code, shouldn't be kept in because it only confuses
# def start(user_input):
    #print 'pick a level: easy, medium, or hard' + user_input

def get_level(level):
  #-# write DOCSTRINGS for your functions!
  if level == "easy":
      print "You'll get 3 guesses"
      return easy_answers, easy_paragraph

  elif level == "medium":
      print "You'll get 3 guesses"
      return medium_answers, medium_paragraph

  elif level == "hard":
      print "You'll get 3 guesses"
      return hard_answers, hard_paragraph

def match_items(a,b): #-# what is this function supposed to do?
  #-# write DOCSTRINGS for your functions!
  for items in b:
    if items in a:
      return items
  return None

def fill_blank_in_paragraph(paragraph): #-# i changed the attribute to `paragraph` (singular)
  #-# write DOCSTRINGS for your functions!
  split_paragraph = paragraph.split()
  for items in paragraph:

    #-# suggestion: if item == blank[index] and user_answer == answers[index]:


    replacement = match_items(a,b) #-# I'd suggest string.replace()
    if replacement != None:
      items = items.replace(replacement, user_input)
      replaced.append(items)
  else:
      replaced.append(items)
  #-# here on the next line you're calling the function recursively! what are you trying to achieve?
  # print fill_blank_in_paragraph(paragraph, answers)

def select_quiz(hard_answers, paragraph): #-# added answers, paragraph
  #-# write DOCSTRINGS for your functions!
  print answers
  index = 0
  for answer in answers:
    #-# here switched to the assignment operator =
    blank = blanks[index]
    #-# no need for this
    # print paragraphs
    player_guess = raw_input("Fill in the" + blank)

    while player_guess != answer:
      player_guess = raw_input("Try again: ")
    # right answer makes the ne
    fill_blank_in_paragraph(paragraph)
    index = index + 1
  print paragraph

def play_game():#start - ask what level
  #-# write DOCSTRINGS for your functions!
  level = raw_input ("Choose a level for this game: easy, medium, or hard: " ).lower() #-# good that you are making input easier

  if level == "easy" or level == "medium" or level == "hard":
      #-# nice job here, correctly assigning both outputs of the function to new variables
      #-# that's quite advanced :)
      #-# !! what's happening with `answers` though? !!
      answers, paragraph = get_level(level)
      print paragraph #-# this needs to go somewhere if you want to use it forward!

      replace = select_quiz(answers, paragraph) #-# added answers, paragraph

  else:
      print "Try again"
      play_game() #-# also here, great job for catching wrong inputs





play_game()