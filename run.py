#importing the libraries
import random


#The list of programming languages to guess for the game.
guess_the_language_list = ['html','java', 'javascript', 'python', 'ruby', 'sql', 'php', 'css', 'c++']


#Generates a random language from the list of languages that is to be guessed by the user
language = random.choice(guess_the_language_list)
#
language_guessed = list('*'*len(language))
#Defined 
characters_guessed=[]


#This function reveals the '*' with each guessed character.
def reveal(guess):
    revealing_indices=[index for index,value in enumerate(language) if value==guess]
    global language_guessed
    for i in revealing_indices:
            language_guessed[i]=guess


#Welcome message printed to the screen.
print('Welcome to guess the programming language\n')
print('The programming language is: {}\n'.format(''.join(language_guessed)))
