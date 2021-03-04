
import random
#using this function to clear the screen from previous guesses
from replit import clear

print("Welcome to Hangman")
print()

words_list = ['accepted', 'accessibility', 'activated', 'adjust','administrator', 'advertisement', 'agricultural', 'anniversary', 'biotechnology', 'bluetooth', 'broadway', 'butterfly', 'capability', 'cardiovascular', 'carnival', 'chemistry', 'citizenship', 'clearance', 'crossword', 'decisions', 'defendant', 'diagnosis', 'discount', 'download', 'fence', 'license', 'chief', 'intend', 'terrific', 'wood', 'reproduce', 'behavior', 'alert', 'hungry', 'satisfying','telephone', 'song', 'stocking', 'lively', 'airplane', 'flawless', 'food']

# using the random.choice function to randomize a word in my list.
choice_word = (random.choice(words_list))

# a list of visuals for the user that will show how many lives are left
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



# Creating an empty list, then adding an underscore to each letter in the randomly selected word
display = []
for letter in choice_word:
    display += "_"

# creating a variable to base while loop on..
end_of_game = False

#Variable keeping track of how many lives the player has. 
lives = 6

# while loop to continue looping and asking user for a letter until all spaces are filled.  ends on line #104 if user runs out of lives, or on line 115.
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()
    # If user has already guessed the letter, print line 91
    if guess in display:
        print("You've already guessed this letter")
    # Checking guessed letter 
    for position in range(len(choice_word)):
        letter = choice_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    
    # does a seperate check.. goes through random word.. if true, minus 1 life
    if guess not in choice_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(stages[lives])

''' 
once all of the positions are filled, setting condition of while loop to True to break it..
then printing "You win"
'''

if "_" not in display:
    end_of_game = True
    print("You win")
        
        








        
        
