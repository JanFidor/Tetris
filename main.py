from pygame_tetris import initialize_tetris_game
from saving_to_file import save_to_file
from terminal_interactions import display_game_over, set_game_difficulty

difficulty_multiplier = set_game_difficulty()

score = initialize_tetris_game(difficulty_multiplier)
display_game_over(score)
save_to_file(score)
