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