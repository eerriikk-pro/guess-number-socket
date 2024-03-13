from enum import Enum

class NumberGame:
    def __init__(self, secret):
        self.secret = secret
        self.guesses = 0
    
    def guess(self, guess: int):
        if not isinstance(guess, int):
            raise ValueError("Guess is not integer. Guess: " + str(guess))
        self.guesses += 1
        if self.secret == guess:
            return GuessResult.GUESS_CORRECT.value
        if self.secret > guess:
            return GuessResult.GUESS_TOO_SMALL.value
        if self.secret < guess:
            return GuessResult.GUESS_TOO_LARGE.value

        
    def get_guesses(self):
        return self.guesses
    
    def clear_guesses(self):
        self.guesses = 0
        return 0
    
class GuessResult(Enum):
    GUESS_CORRECT = 0
    GUESS_TOO_LARGE = 1
    GUESS_TOO_SMALL = 2
    GUESS_ERROR = 3

