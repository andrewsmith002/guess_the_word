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
i = 0
while not int(i) in range(1,6):
    try:
        i = int(input("How difficult do you want to make the game?\nChoose the number of attempts you think you need to guess the hidden programming language [1-5]"))
    except:
        print('Enter between 1 and 5')
failed_attempts = 1




#Created a While loop
while failed_attempts<=i:
    #Print statement containing join()methods and a format()mentod
    print('\nGuess to reveal the programming language: ',''.join(language_guessed))
    print('Previous letters guessed: ', ','.join(characters_guessed))
    guess = input("Failed attempt number: {}\nPlease enter the character or guess the language here:".format(failed_attempts))



    #Created an IF statement when the user inputs a character that was already inputed to display a message.
    if guess in characters_guessed:
        print("You already tried that letter, please choose another letter that you have not chosen\n")
        continue
    characters_guessed.append(guess)


    #Created an IF statement when the user inputs the correct programming language a message with be displayed with the correct language.
    if guess == language:
        print('You guessed the correct language\nThe programming language is: "{}"'.format(language))
        print("Congratulations!")
        exit(0)
        
    #Created an IF statement to display when the user inputs a correct character in the programming language and the reveal() function will display the correct character.
    if guess in language and len(guess)!=0:
        print('Correct, the letter "{}" is in this programming language'.format(guess))
        reveal(guess)


    #Else statement created and will execute if the above IF statement is incorrect.
    else:
        print('Incorrect, please try again')
        failed_attempts+=1


    #Created an IF statement that will display a print statement if the user inputs the correct programming language and an exit function.
    if '*' not in language_guessed:
        print('Congratulations, you have guessed the correct programming language, the language is: "{}"'.format(language))
        exit(0)