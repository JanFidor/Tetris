from board import Board
from constants import PYGAME_TEXT_LOCATION, TETRIS_BLOCK_WIDTH, PYGAME_TEXT_SIZE, Color
import pygame


def TETRIS_BLOCK(row, column):
    """
    Return pygame.Rect of constant width at (x, y)

    Keyword arguments: row -> x coorinate of block on screen
    Keyword arguments: column -> y coorinate of block on screen
    
    Returnen: pygame.Rect at row, column, of constant width
    """
    return pygame.Rect(row, column, TETRIS_BLOCK_WIDTH, TETRIS_BLOCK_WIDTH)


def create_screen(board_width, board_height):
    """
    Save score and date to file

    Keyword arguments: board_width - width of the tetris board
    Keyword arguments: board_height - height of the tetris board
    Returned: Game screen
    """

    screen_width = board_width * TETRIS_BLOCK_WIDTH
    screen_height = board_height * TETRIS_BLOCK_WIDTH
    screen_dimensions = (screen_width, screen_height)
    screen = pygame.display.set_mode(screen_dimensions)
    pygame.display.set_caption("Tetris")
    show_score(screen, 0)
    return screen


def draw_board(screen, tetris_board: Board):
    """
    Display current state of tetris board

    Keyword arguments: screen - tetris game screen
    Keyword arguments: tetris_board - model containing state of tetris board
    """
    width, height = tetris_board.dimensions()
    for x in range(width):
        for y in range(height + 1):
            draw_square(screen, tetris_board, x, y)


def create_square_from_location(tetris_board: Board, x, y):
    """
    Create square at proper screen location from board model location

    Keyword arguments: tetris_board - model containing state of tetris board
    Keyword arguments: x -> x coorinate of block in tetris board model
    Keyword arguments: y -> y coorinate of block in tetris board model
    Returned: pygame.Rect at correct screen location
    """
    height = tetris_board.dimensions()[1]
    column = x * TETRIS_BLOCK_WIDTH
    row = (height - y - 1) * TETRIS_BLOCK_WIDTH

    return TETRIS_BLOCK(column, row)


def get_square_color_from_location_or_black(tetris_board: Board, x, y):
    """
    Retrun color of block at location (x,y) of board model

    Keyword arguments: tetris_board - model containing state of tetris board
    Keyword arguments: x -> x coorinate of block in tetris board model
    Keyword arguments: y -> y coorinate of block in tetris board model

    Returned - Color at location or Black
    """
    color = tetris_board.get_block(x, y)
    if color is None:
        return Color.BLACK
    return color


def draw_square(screen: pygame.Surface, tetris_board: Board, x, y):
    """
    Display square

    Keyword arguments: tetris_board - model containing state of tetris board
    Keyword arguments: x -> x coorinate of block in tetris board model
    Keyword arguments: y -> y coorinate of block in tetris board model

    Returned - Color at location or Black
    """
    color = get_square_color_from_location_or_black(tetris_board, x, y)
    square = create_square_from_location(tetris_board, x, y)
    pygame.draw.rect(screen, color.value, square)


def show_score(screen, score):
    """
    Display current score

    Keyword arguments: screen - tetris game screen
    Keyword arguments: score - current game score

    """
    font = pygame.font.Font('freesansbold.ttf', PYGAME_TEXT_SIZE)
    score_displayed = font.render(f"Score: {score}", True, Color.GREEN.value)
    screen.blit(score_displayed, PYGAME_TEXT_LOCATION)
