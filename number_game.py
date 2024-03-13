class NumberGame:
    def __init__(self, secret):
        self.secret = secret
        self.guesses = 0
    
    def guess(self, guess: int):
        if not isinstance(guess, int):
            raise ValueError("Guess is not integer. Guess: " + str(guess))
        self.guesses += 1
        if self.secret == guess:
            return 0
        if self.secret > guess:
            return 1
        if self.secret < guess:
            return -1

        
    def get_guesses(self):
        return self.guesses
    
    def clear_guesses(self):
        self.guesses = 0
        return 0
    