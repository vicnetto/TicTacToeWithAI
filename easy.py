from operational import print_board, next_play, who_is_next, catch_movement
import random


def easy_mode() -> None:
    """ General easy mode function

        This function does everything to play in the easy difficulty. At first, it
        reads the first player movement and in the second time it makes the "IA"
        movement. Of course this isn't an smart IA, because it is the easy mode.
        Finally, the function watches and verify if the game has ended.

    :return: None.
    """

    m_cells = [["_" for __ in range(3)] for _ in range(3)]

    print_board(m_cells)

    while True:
        next_player = who_is_next(m_cells)  # The next_player variable helps the function to be used once.

        if next_player:
            value = catch_movement(m_cells)
        else:
            print('Making move level "easy"')

            value = easy_choice(m_cells, next_player)

        if value:
            break


def easy_choice(m_cells: list, next_one: bool) -> bool:
    """ Make the bot movement in the EASY difficulty

        This function does the IA movement, randomly choosing two positions for the
        row and the column. Due to this, the IA does not make a smart play, it is
        only an random play.


    :param m_cells: The actual board, with all actual moves.
    :param next_one: Is the return of the who_is_next(...) function.
    :return: True if the game has ended or False if the game is still
    happening.
    """

    out, end_game = True, False
    random.seed()

    while out:
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        row = 2 - row  # Correcting the matrix, to start with the 1 in the bottom.

        if m_cells[row][column] == "_":
            end_game = next_play(m_cells, row, column, next_one)
            out = False

    return True if end_game else False
