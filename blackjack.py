import random
cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"] # Not needed.

player_deck = {
    "A": 11,
    # "ace": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}

dealer_deck = {
        "A": 11,
    # "ace": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}

def shuffle_deck(player):
    simulator = []
    if player == "dealer":
        for card in dealer_deck.keys():
            simulator.append(card)

        random.shuffle(simulator)
        return simulator
        
    elif player == "player":
        for card in player_deck.keys():
            simulator.append(card)

        random.shuffle(simulator)
        return simulator

def dealer_part():
    dealer = []   #names

    for count_dealer in range(2):
        random_card_dealer = random.choice(shuffle_deck("dealer"))
        dealer.append(random_card_dealer)


    while True:
        if sum(dealer_deck[count] for count in dealer) < 13:
            for count in range(1):
                random_card = random.choice(shuffle_deck("dealer"))
                dealer.append(random_card)
            continue

        else:
            break

    # if sum(dealer_cards) > 21:
    #     # print("Stop!_Loss")
    #     dealer_cards = final_cards
    #     return dealer_cards

    # elif 21 > sum(dealer_cards) >= 20:   # first condition.
    #     # print("Stop!_ probably win with 20 or 21 Big nber")
    #     pass

    # elif 21 > sum(dealer_cards) >= 18:  # second condition.
    #     # print("Apply the 0 and 1 dice roll number")
    #     pass

    # elif 18 > sum(dealer_cards) >= 13:  # third condition.
    #     # print("Apply the 1 and 2 dice roll number")
    #     pass

    # elif 13 > sum(dealer_cards) >= 8:   # fourth condition.
    #     # print("Apply the 1 to 3 dice roll number")
    #     pass

    # elif sum(dealer_cards) < 8:  # fifth condition.
    #     # print("Apply the 1 to 5 dice roll number")
    #     pass
    
    return dealer


def display_game():
    player_cards = []
    dealer_cards = dealer_part().copy()  # Copying the dealer's cards to use it later.

    for count in range(2):
        random_card_player = random.choice(shuffle_deck("player"))
        player_cards.append(random_card_player)

    def player_part():
        for count in range(1):
            random_card_player = random.choice(shuffle_deck("player"))
            player_cards.append(random_card_player)
        
        # hitted_player_cards = player_cards.copy()

        # sum_player_cards = 0 # sum of the player's cards.

        # for key, value in simulation.items():
        #     for count in hitted_player_cards:
        #         if key == count:
        #             sum_player_cards += simulation[key]
        # sum_player_cards = sum(simulation[key] for key in hitted_player_cards)

        # return sum_player_cards

    def final_dealer():
        final_cards = dealer_cards    # values

        # sum_final_cards = 0 # sum of the dealer's cards.   

        # for key, value in simulation.items():
        #     for count in final_cards:
        #         if key == count:
        #             sum_final_cards += simulation[key]
        sum_final_cards = sum(dealer_deck[key] for key in final_cards)

        return sum_final_cards
    

    while True:
        def message_output():
            current_score = sum(player_deck[count] for count in player_cards)
            if current_score > 21:
                temp_score = 0
                for card in player_cards:
                    if card == "A":
                        player_deck[card] = 1  # Change Ace from 11 to 1 if the score goes over 21.
                    temp_score += player_deck[card]
                current_score = temp_score

            player_card_holder = ""
            for count in player_cards:
                player_card_holder += str(count) + ", "
            player_card_holder = player_card_holder[:-2]  # Remove the last comma and space.

            dealer_card_holder = ""
            for count in dealer_cards:
                dealer_card_holder += str(count) + ", "

            dealer_card_holder = dealer_card_holder[:-2]  # Remove the last comma and space.


            if current_score > 21:
                print(" " * 5, f"Your Cards: [{player_card_holder}], final score: {current_score}")
                print(" " * 5, f"Dealer's first Card: [{dealer_card_holder}], final score: {final_dealer()}")
                print(" " * 10, "---Status: You went over.")
                # print(" " * 10, "---Game: You went over. You lose 😭")  # OR
                # print(" " * 10, "---Game: You won:). Due to the dealer wen over.\n")
                
                def game_status():
                    if final_dealer() < 21:
                        return print(" " * 10, "---Game: You went over. You lose 😭")
                    
                    elif final_dealer() > 21:
                        return print(" " * 10, "---Game: You won:). Due to the dealer wen over.")
                    
                    elif final_dealer() == 21:
                        return print(" " * 10, "---Game: You went over. You lose 😭")
                game_status()
                print()
                return True
            
            elif current_score == 21:
                print(" " * 5, f"Your Cards: [{player_card_holder}], final score: {current_score}")
                print(" " * 5, f"Dealer's first Card: [{dealer_card_holder}], final score: {final_dealer()}")
                print(" " * 10, "---Status: You hit a Blackjack 😎")
                # print(" " * 10, "---Game: __You Win!__ | __It's a Draw!__\n")     #When the dealer also has 21(hit the Blackjack).

                def blackjack_status():
                    if final_dealer() < 21:
                        return print(" " * 10, "---Game: You Win:)")
                    
                    elif final_dealer() == 21:
                        return print(" " * 10, "---Game: It's a Draw:(. You both hit a Blackjack.")
                blackjack_status()

                print()
                return True
            
            elif 21 < current_score == 21:
                return False
            
            print(" " * 5, f"Your Cards: [{player_card_holder}], current score: {current_score}")
            print(" " * 5, f"Dealer's first Card: [{dealer_cards[0]}, ?]")
            print(" " * 10, "---Status: You are still in the game.")


        if message_output():
            break

        player_decision = input("Type 'y' to hit(get another card), type 'n' to stand(pass): ").lower()

        player_card_holder = ""
        for count in player_cards:
            player_card_holder += str(count) + ", "

        player_card_holder = player_card_holder[:-2]  # Remove the last comma and space.

        dealer_card_holder = ""
        for count in dealer_cards:
            dealer_card_holder += str(count) + ", "

        dealer_card_holder = dealer_card_holder[:-2]  # Remove the last comma and space.

        if player_decision == "n":
            final_score = sum(player_deck[count] for count in player_cards)
            
            if final_score > 21:
                temp_score = 0
                for card in player_cards:
                    if card == "A":
                        player_deck[card] = 1  # Change Ace from 11 to 1 if the score goes over 21.
                    temp_score += player_deck[card]
                final_score = temp_score
            print()
            print(" " * 5, f"Your Cards: [{player_card_holder}], final score: {final_score}")
            print(" " * 5, f"Dealer's final hand: [{dealer_card_holder}], final score: {final_dealer()}")
            # print(" " * 10, "Game: __You Win!__  __Dealer Win!__")

            def final_status():
                    if final_score > final_dealer():
                        return print(" " * 10, "---Game: You Win:)")
                    
                    elif final_dealer() > final_score:
                        return print(" " * 10, "---Game: Dealer Win!")
                        
                    elif final_dealer() == final_score:
                        if final_dealer() == 21 and final_score == 21:
                            return print(" " * 10, "---Game: It's a Draw:(. You both hit a Blackjack.")
                        else:
                            return print(" " * 10, "---Game: It's a Draw:(")
            final_status()

            print()
            break

        elif player_decision == "y":

            print()
            player_part()
            # if message_output(player_part()):
            #     break
            continue

        else:
            print()
            print("Invalid input! Please enter 'y' or 'n'.")

while True:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play == "n":
        print("Goodbye!")
        break

    elif play == "y":
        print("\n" * 30, "----Welcome to the Blackjack Game!----")
        print()
        demo = input("Do you want to see a quick demo before playing? Type 'y' or 'n' to play: ").lower()
        if demo == "y":
            print("\nIn this game, you will be dealt two cards. You can choose to hit (draw another card) or stand (keep your current hand).")
            print("The goal is to get as close to 21 as possible without going over.")
            print("If you go over 21, you lose. If you get exactly 21, you win!")
            print("You can also choose to play with a dealer who will also be dealt two cards.")
            print("Good luck!")
            print()

            if input("press 'Enter' to continue: ") == "":
                print()
                display_game()

        elif demo == "n":
            print()
            display_game()

        else:
            print("Wrong Input! Please enter 'y' or 'n'.")

    else:
        print("Wrong Input! Please enter 'y' or 'n'.")
        