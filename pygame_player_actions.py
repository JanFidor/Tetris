from game_tetris import Tetris
import pygame
import operations


GET_OPERATION_FROM_KEYDOWN = {
    pygame.K_a: operations.GoLeft,
    pygame.K_d: operations.GoRight,
    pygame.K_s: operations.GoDown,
    pygame.K_q: operations.TurnLeft,
    pygame.K_e: operations.TurnRight,
}


def intercept_player_actions(tetris_game: Tetris, lower_block_event):
    """
    Intercept possible player actions

    Keyword arguments: tetris_game -> model containing current state of tetris
    game
    Keyword arguments: lower_block_event -> id of event for lowering block
    """
    for event in pygame.event.get():
        execute_player_action(event, tetris_game, lower_block_event)


def execute_player_action(event, tetris_game: Tetris, lower_block_event):
    """
    Execute game action

    Keyword arguments: event - current pygame event
    Keyword arguments: tetris_game - model containing current state of tetris
    game
    Keyword arguments: lower_block_event - id of event for lowering block
    """
    if event.type == pygame.QUIT:
        tetris_game.game_over()
    elif event.type == lower_block_event:
        tetris_game.execute_operation(operations.GoDown)
    elif event.type == pygame.KEYDOWN:
        execute_operation(event, tetris_game)


def execute_operation(event, tetris_game: Tetris):
    """
    Execute operation

    Keyword arguments: event - current pygame event
    Keyword arguments: tetris_game - model containing current state of tetris
    game
    """
    if event.key in GET_OPERATION_FROM_KEYDOWN:
        operation = GET_OPERATION_FROM_KEYDOWN[event.key]
        tetris_game.execute_operation(operation)
    elif event.key == pygame.K_SPACE:
        tetris_game.drop_block()
