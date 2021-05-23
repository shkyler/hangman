import numpy as np
import os
import time

# global variables required for a game
answer = ""
show_ans = ""
wrong_guess = []
lives = 0
# read the word list in from a csv file
words = []
with open("words.csv", "r") as myfile:
    for word in myfile: 
        words.append(word.rstrip()) 

# define the allowable inputs from the users
allowable_inputs =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# define a funtion for turning a list into a string
def stringify(list_in):
    ret_string=""
    for i in list_in:
        ret_string=ret_string+str(i)
    return ret_string    

def print_out():
    #clear the screen, show how many lives are left and the current state of the answer
    os.system('cls')
    gallows(lives)
    print("Lives: ", lives)
    print("Word: ", stringify(show_ans))
    print("Incorrect Guesses:", wrong_guess)

# define a function for a turn
def turn():
    global answer
    global show_ans
    global wrong_guess
    global lives

    print_out()
    # ask the user to guess a letter
    guess = input("Please guess a letter: ").lower()
    while guess not in allowable_inputs:
        guess = input("You must enter a letter: ").lower()

    while guess in wrong_guess or guess in show_ans:
        guess = input("You already guessed that, try again: ")

    if guess in answer:
        for i in range(0,len(answer)):
            if guess == answer[i]:
                show_ans[i] = guess
    else:
        lives=lives-1
        wrong_guess.append(guess) 

#define a function for a game
def new_game():
    # use the global variables
    global answer
    global show_ans
    global wrong_guess
    global lives
    # choose a word for the game
    answer = np.random.choice(words)

    # create a word in dashes on the screen for each letter in the answer
    show_ans = []
    for i in range(len(answer)):
        show_ans.append('_')

    # user gets 7 lives 
    lives = 7
    # list of wrong guesses
    wrong_guess = []

    # keep taking turns until the word is guessed or you run out of lives
    while lives > 0 and "_" in show_ans:
        turn()               
    # if you run out of lives its game over
    if lives == 0:
        print_out()
        print("Game Over, the correct answer was: ", answer) 
        # wait 8 seconds and return to main menu
        time.sleep(8)
        main()
    # if you guess the word you win
    else:
        print_out()
        print("You Win! You correctly guessed", answer)
        # wait 8 seconds and return to main menu
        time.sleep(8)
        main()
    
def main():
    splash()
    start_game = input("Would you like to play? (y/n)").lower()
    while start_game not in ['y','n']:
        splash()
        start_game = input("Would you like to play? (y/n)").lower()
    if start_game == 'n':
        print("OK, Bye!")
        quit()
    else:
        new_game()    

# graphics
def splash():
    os.system('cls')    
    print("* * * * * * * * * * * * * * * * * * * * *")
    print("*                                       *")
    print("*              HANGMAN                  *")
    print("*                                       *")
    print("*                2021                   *")
    print("*                                       *")
    print("*            Patrick Moore              *")
    print("*                                       *")
    print("* * * * * * * * * * * * * * * * * * * * *")

def gallows(lives_remaining):
    os.system('cls')
    if lives_remaining == 7:    
        print("* * * * * * * * * * * * * * * * * * * * *")
        print("*                                       *")
        print("*                                       *")
        print("*                                       *")
        print("*                                       *")
        print("*                                       *")
        print("*                                       *")
        print("*                                       *")
        print("* * * * * * * * * * * * * * * * * * * * *")
    elif lives_remaining == 6:  
        print("* * * * * * * * * * * * * * * * * * * * *")
        print("*       ___________                     *")
        print("*      |           |                    *")
        print("*      |                                *")
        print("*      |                                *")
        print("*      |                                *")
        print("*      |                                *")
        print("*      |________________                *")
        print("* * * * * * * * * * * * * * * * * * * * *")
    elif lives_remaining == 5:  
        print("* * * * * * * * * * * * * * * * * * * * *")
        print("*       ___________                     *")
        print("*      |           |                    *")
        print("*      |           O                    *")
        print("*      |                                *")
        print("*      |                                *")
        print("*      |                                *")
        print("*      |________________                *")
        print("* * * * * * * * * * * * * * * * * * * * *")
    elif lives_remaining == 4:  
        print("* * * * * * * * * * * * * * * * * * * * *")
        print("*       ___________                     *")
        print("*      |           |                    *")
        print("*      |           O                    *")
        print("*      |           |                    *")
        print("*      |                                *")
        print("*      |                                *")
        print("*      |________________                *")
        print("* * * * * * * * * * * * * * * * * * * * *")    
    elif lives_remaining == 3:  
        print("* * * * * * * * * * * * * * * * * * * * *")
        print("*       ___________                     *")
        print("*      |           |                    *")
        print("*      |           O                    *")
        print("*      |         / |                    *")
        print("*      |                                *")
        print("*      |                                *")
        print("*      |________________                *")
        print("* * * * * * * * * * * * * * * * * * * * *")
    elif lives_remaining == 2:  
        print("* * * * * * * * * * * * * * * * * * * * *")
        print("*       ___________                     *")
        print("*      |           |                    *")
        print("*      |           O                    *")
        print("*      |         / | \                  *")
        print("*      |                                *")
        print("*      |                                *")
        print("*      |________________                *")
        print("* * * * * * * * * * * * * * * * * * * * *")
    elif lives_remaining == 1:  
        print("* * * * * * * * * * * * * * * * * * * * *")
        print("*       ___________                     *")
        print("*      |           |                    *")
        print("*      |           O                    *")
        print("*      |         / | \                  *")
        print("*      |          /                     *")
        print("*      |         /                      *")
        print("*      |________________                *")
        print("* * * * * * * * * * * * * * * * * * * * *")
    elif lives_remaining == 0:  
        print("* * * * * * * * * * * * * * * * * * * * *")
        print("*       ___________                     *")
        print("*      |           |                    *")
        print("*      |           O                    *")
        print("*      |         / | \                  *")
        print("*      |          / \                   *")
        print("*      |         /   \                  *")
        print("*      |________________                *")
        print("* * * * * * * * * * * * * * * * * * * * *")   
main()