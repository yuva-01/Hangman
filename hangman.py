# hangman game 
import random
import nltk
from nltk.corpus import words
from hangman_images import hangman_images 

nltk.download('words')




list_words = words.words()
chosen_word = random.choice([word for word in list_words if len(word) >= 4 and len(word) <= 8 and word.isalpha()]).lower()
length = len(chosen_word)

# print (chosen_word)  

display_string = ["_"] * length

print(" ".join(display_string))

lives = 6


def game():
    global lives
    guess = input("Guess a letter: ").lower()
    found = False
    for index in range(length):
        if chosen_word[index] == guess:
            display_string[index] = guess
            found = True
    if not found:
        lives -= 1
        print(f"Wrong guess. Lives left: {lives}")
        print(hangman_images[6 - lives])  
    print(" ".join(display_string))
    if lives == 0:
        print("***** You lost *****")
        print(f"The word was: {chosen_word}")
        exit()


while "".join(display_string) != chosen_word:
    game()

print("***** You won ***** ")
