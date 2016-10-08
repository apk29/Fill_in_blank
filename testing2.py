a = ["__1__", "__2__", "__3__","__4__"]

easy_paragraph = '''Bono is the lead singer of the band called "__1__". The happiest place on earth is "__2__".
                    The color of grass is "__3__". The color of the sky is "__4__".'''

medium_paragraph ='''The first president of the US was "__1__". The second president of the US was "__2__".
                    The third president of the US was "__3__". The first African-American president is "__4__.'''

hard_paragraph = '''The us has three branches of government, the president's branch is called the "__1__" branch,
                    the congressional branch is called the "__2__" branch, and the supreme court is the "__3__" branch.
                    Who was the president who freed the slaves, __4__?'''

easy_answers = ['u2', 'disneyland', 'green', 'blue']
medium_answers = ['George Washington', 'John Adams', 'Thomas Jefferson','Barack Obama']
hard_answers = ['executive', 'legislative', 'judicial','Abraham Lincoln']

def remove_spaces(text):
    text_without_spaces = '' #empty string for now
    while text != '':
        next_character = text[0]
        print next_character
        if next_character != ' ':    #that's a single space
            text_without_spaces = text_without_spaces + next_character
        text = text[1:]
        
    return text_without_spaces
print remove_spaces("hello my name is andy how are you?")

