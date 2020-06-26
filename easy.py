import random


def easy_choice(m_cells: list, next_one: bool) -> str:
    """ Make the bot movement in the EASY difficulty

        This function does the IA movement, randomly choosing two positions for the
        row and the column. Due to this, the IA does not make a smart play, it is
        only an random play.


    :param m_cells: The actual board, with all actual moves.
    :param next_one: Is the return of the who_is_next(...) function.
    :return: True if the game has ended or False if the game is still
    happening.
    """

    print('Making move level "easy"')

    out, end_game = True, False
    random.seed()

    while out:
        row = random.randint(0, 2)
        column = random.randint(0, 2)

        if m_cells[2 - row][column] == "_":
            return str(column + 1) + " " + str(row + 1)
