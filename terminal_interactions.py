from constants import DIFFICULTIES_MULTIPLIERS


def print_options():
    """
    Display possible difficulties.
    """
    print("Choose difficulty level")
    print("1 - Easy")
    print("2 - Medium")
    print("3 - Hard")


def set_difficulty_loop():
    """
    Creates loop forcing the user to choose the correct difficulty
    and returns it
    """

    while True:
        print_options()
        difficulty_level = input()
        chosen_difficulty = chosen_difficulty_or_none(difficulty_level)
        if chosen_difficulty is not None:
            return chosen_difficulty


def chosen_difficulty_or_none(difficulty_level):
    """
    Check if chosen difficulty is correct and return it or none

    Keyword arguments: difficulty_level: string, difficulty level chosen by 
    user, might be incorrect.

    Returned: difficulty multiplier if correct difficulty, else None
    """

    if difficulty_level in DIFFICULTIES_MULTIPLIERS:
        return DIFFICULTIES_MULTIPLIERS[difficulty_level]
    return None


# return chosen difficulty
def set_game_difficulty():
    return set_difficulty_loop()


# displat game over and achieved score
def display_game_over(score):
    print("Game Over")
    print(f"Score: {score}")
