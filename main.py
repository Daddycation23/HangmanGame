import random
import time

WORDS = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
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
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def main():
    word = random.choice(WORDS)
    guessed_letters = set()
    hangman_count = 0
    max_attempts = len(HANGMANPICS) - 1

    print("Hello, welcome to the hangman game!")
    time.sleep(2)

    while hangman_count < max_attempts:
        print(HANGMANPICS[hangman_count])
        print(update_blanks(word, guessed_letters))
        
        guess = input("Please guess the golden letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in word:
            print("YESSER!")
            guessed_letters.add(guess)
        else:
            print("BooBoo, incorrect!")
            hangman_count += 1
            guessed_letters.add(guess)
        
        time.sleep(2)
        
        if set(word) <= guessed_letters:
            print(f"YAY! You guessed the word: {word}")
            return

    print(HANGMANPICS[hangman_count])
    print(f"U so nooooooooob. The word was: {word}")

if __name__ == "__main__":
    main()
