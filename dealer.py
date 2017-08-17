from blackjackhand import BlackjackHand

class Dealer(object):
    def __init__(self, deck):
        self.deck = deck
        self.hand = BlackjackHand()
        
    def deal_card(self):
        return self.deck.draw()
        
    def take_card(self, card):
        self.hand.add_card(card)
        
    def empty_hand(self):
        self.hand = BlackjackHand()
    
    def show_hand(self, hide_card=True):
        self.hand.show(hide_card)
    
    def play_turn(self):
        while True:
            
            if self.hand.is_busted():
                print 'Dealer busted!'
                return
            
            if self.hand.is_dealer_limit():
                print 'Dealer reached limit!'
                return
                        
            card = self.deal_card()
            self.take_card(card)