from datetime import datetime


def save_to_file(score):
    """
    Save score and date to file

    Keyword arguments: score - tetris score achieved by player
    """

    with open('scores.txt', 'a') as file:
        file.write(format_date_and_score(score))


def format_date_and_score(score):
    """
    Format date and score to string
    
    Keyword arguments: score - tetris score achieved by player
    """

    formatted_date = f"Date: {datetime.today().isoformat()}"
    formatted_score = f"Score: {score}"
    return f"{formatted_date}, {formatted_score}\n"
