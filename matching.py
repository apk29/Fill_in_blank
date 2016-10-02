easy_answers = ['u2', 'disneyland', 'green']
answers = ['u', 'lala', 'green']

def match_items(a,b): #-# what is this function supposed to do?
  #-# write DOCSTRINGS for your functions!
  for items in b:
    if items in a:
      return items
  return None


print match_items(easy_answers, answers)