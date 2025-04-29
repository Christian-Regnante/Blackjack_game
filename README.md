# Blackjack Game

Welcome to the **Blackjack Game**! This project is a Python-based implementation of the popular card game Blackjack. The game allows you to play against a dealer, with the goal of getting as close to 21 as possible without going over.

## How the Game Works

1. **Objective**: 
   - The goal is to have a hand value closer to 21 than the dealer's hand without exceeding 21.
   - If you exceed 21, you lose. If you hit exactly 21, you win (Blackjack).

2. **Card Values**:
   - Number cards (2-10) are worth their face value.
   - Face cards (J, Q, K) are worth 10 points.
   - Aces (A) can be worth 11 or 1, depending on the situation.

3. **Gameplay**:
   - Both the player and the dealer start with two cards.
   - The player can choose to "hit" (draw another card) or "stand" (keep their current hand).
   - The dealer will draw cards until their hand value is at least 13.
   - The game ends when the player stands or goes over 21.

4. **Winning Conditions**:
   - If your hand value is closer to 21 than the dealer's, you win.
   - If the dealer exceeds 21, you win.
   - If both you and the dealer have the same hand value, it's a draw.

## Features

- **Shuffling and Dealing**: Cards are shuffled randomly before being dealt to the player and dealer.
- **Dynamic Ace Handling**: Aces can switch between 11 and 1 to prevent the player from going over 21.
- **Dealer Logic**: The dealer automatically draws cards until their hand value is at least 13.
- **Interactive Gameplay**: The player can choose to hit or stand during their turn.
- **Game Status Messages**: The game provides detailed messages about the current state, including the player's and dealer's cards, scores, and the final result.

## How to Play

1. Run the Python script.
2. Choose whether to play a game of Blackjack by typing `'y'` or `'n'`.
3. If you choose to play, you can also view a quick demo of the game rules.
4. During the game:
   - Type `'y'` to hit (draw another card).
   - Type `'n'` to stand (end your turn).
5. The game will display the results and determine the winner.

## Code Highlights

- **Decks**: The game uses two separate dictionaries for the player's and dealer's decks, mapping card names to their values.
- **Shuffling**: The `shuffle_deck` function ensures randomness in card dealing.
- **Dealer Logic**: The `dealer_part` function handles the dealer's card drawing strategy.
- **Game Display**: The `display_game` function manages the main game loop, including player decisions and result evaluation.

## Example Output

```
----Welcome to the Blackjack Game!----

Your Cards: [A, seven], current score: 18
Dealer's first Card: [K, ?]
---Status: You are still in the game.

Type 'y' to hit(get another card), type 'n' to stand(pass): y

Your Cards: [A, seven, three], final score: 21
Dealer's first Card: [K, J], final score: 20
---Status: You hit a Blackjack 😎
---Game: You Win:)
```

## Requirements

- Python 3.x
- No additional libraries are required as the game uses Python's built-in `random` module.

## Future Improvements

- Add support for multiple players.
- Implement betting and chip management.
- Enhance the dealer's strategy for more challenging gameplay.
