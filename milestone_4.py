import random

class Hangman:
    def __init__(self, word_list,num_lives):
        self.word_list = word_list
        self.num_lives = 5
        self.word = random.choice(word_list)
        self.word_guessed = list(len(self.word)* '_')
        self.num_letters = set(self.word)
        list_of_guesses = []
        print(self.num_letters)
        print(self.word_guessed)
        print(list_of_guesses)
    
        
