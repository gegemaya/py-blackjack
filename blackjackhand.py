class BlackjackHand(object):
    values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
    
    def __init__(self):
        self.cards = []
        
    def add_card(self, card):
        self.cards.append(card)
        
    def get_total(self):
        total = 0
        for card in self.cards:
            total += BlackjackHand.values[card.rank]
            
        for card in self.cards:
            if card.rank == 'A' and total < 12:
                total += 10
                
        return total
    
    def is_blackjack(self):
        return len(self.cards) == 2 and self.get_total() == 21
        
    def is_busted(self):
        return self.get_total() > 21
        
    def is_dealer_limit(self):
        return self.get_total() > 16
            
    def show(self, hide_card=False):
        print '____________________'
        if len(self.cards) == 0:
            print 'Hand is empty.'
        else:
            if hide_card == True:
                print '#:#'
            else:
                print self.cards[0]
            
            for card in self.cards[1:]:
                print card