import math
import random

# Base Player class
class Player:
    def __init__(self, letter):
        self.letter = letter

    # Placeholder method to be overridden
    def get_move(self, game):
        pass

# Random Computer Player (chooses moves randomly)
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        return random.choice(game.available_moves())

# Human Player (takes input from user)
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input move (0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val

# Genius Computer Player (uses minimax algorithm to find best move)
class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            # Random move if board is empty
            square = random.choice(game.available_moves())
        else:
            # Use minimax to find best move
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, game, player):
        max_player = self.letter  # The AI itself
        other_player = 'O' if player == 'X' else 'X'

        # Check if previous move is a winner
        if game.current_winner == other_player:
            return {
                'position': None,
                'score': 1 * (game.num_empty_squares() + 1) if other_player == max_player else -1 * (game.num_empty_squares() + 1)
            }

        # Tie game
        if not game.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # maximize the score
        else:
            best = {'position': None, 'score': math.inf}   # minimize the score

        for possible_move in game.available_moves():
            # Make a move
            game.make_move(possible_move, player)
            sim_score = self.minimax(game, other_player)['score']

            # Undo move
            game.board[possible_move] = ' '
            game.current_winner = None

            # Update best move
            if player == max_player:
                if sim_score > best['score']:
                    best = {'position': possible_move, 'score': sim_score}
            else:
                if sim_score < best['score']:
                    best = {'position': possible_move, 'score': sim_score}
        return best