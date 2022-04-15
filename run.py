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


#A print statement informing the user of the maximum failed attempts they have.
print("You have a maximum of 5 failed attempts to guess what programming language is behind the above asterisks")


#Created a While Not loop and a print statement  requesting the user to enter how many failed attempts they want between 1-5.
chance = 0
while not int(chance) in range(1,6):
    try:
        chance = int(input("How difficult do you want to make the game?\nChoose the number of attempts you think you need to guess the hidden programming language [1-5]"))
    except:
        print('Enter between 1 and 5')
failed_attempts = 1