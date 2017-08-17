from blackjackhand import BlackjackHand

class Player(object):
    def __init__(self, bankroll=100):
        self.bankroll = bankroll
        self.hand = BlackjackHand()
        
    def add_win(self, amount): 
        self.bankroll += amount
        print 'You win ' + str(amount) + '. Your total is now: ' + str(self.bankroll)
        
    def sub_loss(self, amount):
        self.bankroll -= amount
        print 'You lose ' + str(amount) + '. Your total is now: ' + str(self.bankroll)
        
    def take_card(self, card):
        self.hand.add_card(card)
        
    def empty_hand(self):
        self.hand = BlackjackHand() 
        
    def show_hand(self, hide_card=False):
        self.hand.show(hide_card)
        
    def ask_bet(self):
        bet = 0
        while bet <= 0 or bet > self.bankroll:
            try:
                bet = int(raw_input('How much do you want to bet?'))
                
            except:
                print 'Bet must be a positive integer!'
                
            if bet <= 0:
                print 'Bet must be positive!'
                continue
                
            if bet > self.bankroll:
                print "You don't have enough money"
                continue
                
            if bet == self.bankroll:
                print 'Betting the farm!'
                
        return bet
    
    def play_turn(self):
        answer = ''
        while answer != 'h' and answer != 's':
            answer = raw_input('Do you wish to hit or stay(h/s)?')
            
        return answer