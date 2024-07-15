#Credit to chrishorton for the word bank and hangman pics
import random
import time

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def update_blanks(word, guessed_letters):
    blanks = ["_" if letter not in guessed_letters else letter for letter in word]
    return " ".join(blanks)

def main():
    theWord = random.choice(words)
    guessed_letters = set()
    hangmanCount = 0
    max_attempts = len(HANGMANPICS) - 1

    print("Hello, welcome to the hangman game!")
    time.sleep(2)

    while hangmanCount < max_attempts:
        print(HANGMANPICS[hangmanCount])
        print(update_blanks(theWord, guessed_letters))
        userGuess = input("Please guess the golden letter: ").lower()

        if userGuess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif userGuess in theWord:
            print("YESSER!")
            guessed_letters.add(userGuess)
        else:
            print("BooBoo, incorrect!")
            hangmanCount += 1
            guessed_letters.add(userGuess)
            time.sleep(2)

        if all(letter in guessed_letters for letter in theWord):
            print(f"YAY! You guessed the word: {theWord}")
            break
    else:
        print(HANGMANPICS[hangmanCount])
        print(f"U so nooooooooob. The word was: {theWord}")

if __name__ == "__main__":
    main()
