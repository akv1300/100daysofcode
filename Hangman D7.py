# You have 6 attemts counted onlly when wrong to guess the animal name before the man hangs
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

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
import random
word = random.choice(words)
play = True
code = []
lives = 0
for i in word:
    code.append("*")
while play:
    letter = input("Guess a letter from the word \n")
    for position in range (len(word)):
        if word[position] == letter:
            code[position] = letter
            print(code)
    if letter not in word:
        lives+=1
        print(HANGMANPICS[lives])
    if "*" not in code:
        print("You Won")
        play = False
    elif lives == 6:
        print("You lose")
        play = False
print(code)