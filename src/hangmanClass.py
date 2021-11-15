from random import choice

WORDS = set(['apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 'pineapple', 'apricot', 'lemon', 'coconut', 'watermelon', 'cherry', 'papaya', 'berry', 'peach', 'lychee', 'muskmelon']) 

class HangMan:
    def __init__(self) -> None:
        self.word = list(choice(list(WORDS)))
        self.guessed = set()
        self.lives = 10 # We give 10 chances to guess the word.
        self.display = ['_' for _ in range(len(self.word))]
        self.win = False
        self.lose = False
        self.guess = ''
    
    def guess_letter(self, letter: str) -> None:
        if letter in self.guessed:
            pass
            # print('You already guessed this letter.')
        elif letter in self.word:
            self.guessed.add(letter)
            self.display = []

            for char in self.word:
                if char == letter or char in self.guessed:
                    self.display.append(char)
                else:
                    self.display.append('_')
            
            if self.display == self.word:
                self.win = True
        else:
            self.guessed.add(letter)
            self.lives -= 1
            if self.lives == 0:
                self.lose = True
    
    def guess_word(self, word: str) -> None:
        word = list(word)
        if word == self.word:
            self.display = list(word) # This splits The characters of the word into a list.
            self.win = True
        else:
            self.lives -= 1
            if self.lives == 0:
                self.lose = True

    '''
    # This method is needed if you want to play Hangman in Command Line interface.
    def play(self):
        while not self.win and not self.lose:
            print(' '.join(self.display))
            print('You have {} lives left.'.format(self.lives))
            print('Guess:')
            
            # letter = input()
            # self.guess_letter(letter)
            # print('Guess a word:')
            # word = input()
            # self.guess_word(word)
            
            txt = input().strip()
            if len(txt) == 1:
                self.guess_letter(txt)
            else:
                self.guess_word(txt)

        if self.win:
            print('You win!')
        else:
            print('You lose!')
        print('The word was {}.'.format(self.word))
    '''
