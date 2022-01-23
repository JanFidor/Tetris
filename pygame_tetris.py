import pygame
from game_tetris import Tetris
from pygame_player_actions import intercept_player_actions
from pygame_ui import draw_board, create_screen, show_score
from constants import SECOND_IN_MILIS


def initialize_tetris_game(difficulty=1):
    """
    Initialize tetris game

    Keyword arguments: difficulty - difficulty multiplier chosen by player
    (default 1)

    Returned - score achieved by player
    """

    pygame.init()

    tetris_game = Tetris(difficulty)

    timer_event_id = set_timer(difficulty)
    screen = create_screen(*tetris_game.get_board().dimensions())

    initialize_game_loop(tetris_game, timer_event_id, screen)

    return tetris_game._points


def initialize_game_loop(tetris_game: Tetris, lower_block_event, screen):
    """
    Initiaize tetris game loop

    Keyword arguments: tetris_game - model containing state of tetris game
    Keyword arguments: lower_block_event -> id of event responsible for
    lowering block
    Keyword arguments: screen - tetris game screen
    """

    while tetris_game.is_running():
        intercept_player_actions(tetris_game, lower_block_event)

        draw_board(screen, tetris_game.get_board())
        show_score(screen, tetris_game._points)
        pygame.display.update()


def set_timer(difficulty):
    """
    Set timer responsible for event of lowering block

    Keyword arguments: difficulty - difficulty multiplier chosen by player

    Returned - Id of timer event
    """
    time_delay = SECOND_IN_MILIS // difficulty
    lower_block_event = pygame.USEREVENT+1
    pygame.time.set_timer(lower_block_event, time_delay)
    return lower_block_event
