from gamecontroller import GameController

def play_game():
    
    game = GameController()
    game.prep_player()
    
    while game.ask_play():
        
        game.ask_player_bet()
        game.prep_dealer()
        game.hand_to_player()
        game.hand_to_dealer()
    
        initial_outcome = game.check_initial_hands()
        if initial_outcome != 'game goes on':
            game.process_blackjack(initial_outcome)
            game.collect_used_cards()
            continue

        game.do_player_turn()
        player_status = game.check_player()
        if player_status == 'player_busted':
            game.handle_game_outcome('dealer')
            game.collect_used_cards()
            continue

        game.do_dealer_turn()
        dealer_status = game.check_dealer()
        if dealer_status == 'dealer_busted':
            game.handle_game_outcome('player')
            game.collect_used_cards()
            continue

        outcome = game.find_winner()
        game.handle_game_outcome(outcome)
        game.collect_used_cards()

    print("\nYou go home with $" + str(game.player.bankroll))
    print("Thanks for playing!")
        