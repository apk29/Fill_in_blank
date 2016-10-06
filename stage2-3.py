#Stage 2, Final Project, "Fill-in-the-Blanks-Quiz"

blanks = ["__1__", "__2__", "__3__","__4__"]

easy_paragraph = '''Bono is the lead singer of the band called "__1__". The happiest place on earth is "__2__". The color of grass is "__3__". The color of the sky is "__4__".'''
medium_paragraph ='''The first president of the US was "__1__". The second president of the US was "__2__". The third president of the US was "__3__". The first African-American president is "__4__.'''
hard_paragraph = '''The us has three branches of government, the president's branch is called the "__1__" branch, the congressional branch is called the "__2__" branch, and the supreme court is the "__3__" branch. Who was the president who freed the slaves, __4__?'''

easy_answers = ['u2', 'disneyland', 'green', 'blue']
medium_answers = ['George Washington', 'John Adams', 'Thomas Jefferson','Barack Obama']
hard_answers = ['executive', 'legislative', 'judicial','Abraham Lincoln']

#def start(user_input):
    #print 'pick a level: easy, medium, or hard' + user_input
def get_level(level):

    if level == "easy":
        
        return easy_answers, easy_paragraph
        
    elif level == "medium":
        
        return medium_answers, medium_paragraph
        
    elif level == "hard":
       
        return hard_answers, hard_paragraph
        

def match_items(paragraphs,blanks):
  for items in blanks:
    if items in paragraphs:
      return items
  return None

#def replace_blank(paragraphs,player_guess,index, replaced):
    
    
    
def fill_blank_in_paragraph(paragraphs,player_guess,replaced, index):
    replaced = []
    split = paragraphs.split()
    for word in split:
        replacement = match_items(paragraphs,blanks)
        if replacement != None:
            
            word = word.replace(replacement, player_guess)
            replaced.append(word)
            
        else:
            replaced.append(word)
    replaced = " ".join(replaced) 
    
    print replaced
    
        


def quiz_answer(answers,paragraphs):
    replaced = []
    index = 0
    blank_count = 0
    
    while index < 4: 
        player_guess = raw_input("Fill in the " + blanks[index] + " ")
        
        if player_guess == answers[index]:
            print "Correct!"
            replaced = fill_blank_in_paragraph(paragraphs,player_guess,index,replaced)            
            index = index + 1             
        else:
            blank_count = blank_count + 1
            if blank_count < 3:
                if blank_count > 1:
                    print str(3-blank_count) + " chance left"
                else:
                    print str(3-blank_count) + " chances left"
            else:
                print "Game over!"
                break
                
                
                  
        

def play_game():#start - ask what level
    level = raw_input ("Choose a level for this game: easy, medium, or hard: " )
    
    print ""
    if level == "easy" or level == "medium" or level == "hard":
        answers, paragraphs = get_level(level)
        print paragraphs
        print ""                  
        replace = quiz_answer(answers, paragraphs)

    else:
        print "Try again"
        play_game()


play_game()
