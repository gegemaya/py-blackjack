class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def is_ace(self):
        return self.rank == 'A'
        
    def __str__(self):
        return self.suit + ':' + self.rank