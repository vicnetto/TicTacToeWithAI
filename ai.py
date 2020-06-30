import random


def easy_choice(m_cells: list, is_medium=False) -> str:
    """ Make the bot movement in the EASY difficulty

        This function does the IA movement, randomly choosing two positions for the
        row and the column. Due to this, the IA does not make a smart play, it is
        only an random play.


    :param is_medium:
    :param m_cells: The actual board, with all actual moves.
    :return: Returns a string with a random move.
    """

    if is_medium == 0:
        print('Making move level "easy"')

    random.seed()

    while True:
        row = random.randint(0, 2)
        column = random.randint(0, 2)

        if m_cells[2 - row][column] == "_":
            return str(column + 1) + " " + str(row + 1)


def medium_choice(m_cells: list, next_player: bool) -> str:
    """ Make the IA movement in the MEDIUM difficulty

        This function searches for a real and important moves. It first searches for
        end game moves and then, if there is no one, it looks for block moves. If no
        one of those are good moves, it makes a random move.

    :param m_cells: The actual board, with all actual moves.
    :param next_player: What is the next player to make the
    play, "O" or "X".
    :return: Returns a string with a good movement.
    """

    print('Making move level "medium"')

    next_player = "X" if next_player else "O"
    position = ""

    # Setting all possible lists, for all needed verification.
    hor_lists = [[value for value in lis] for lis in m_cells]
    ver_lists = [[m_cells[row][column] for row in range(0, 3)] for column in range(0, 3)]
    principal_list = [m_cells[2 - numb][numb] for numb in range(0, 3)]
    secondary_list = [m_cells[numb][numb] for numb in range(0, 3)]
    # Putting them together in one list.
    all_in_one_list = hor_lists + ver_lists + [principal_list] + [secondary_list]

    # Turning every list in a set to see what is the best move.
    for index, lis in enumerate(all_in_one_list):
        set_lis = set(lis)
        if len(set_lis) == 2:
            if list(set_lis)[0] == "_" or list(set_lis)[1] == "_":
                much = [i for i, char in enumerate(all_in_one_list[index]) if char == "_"]
                if len(much) == 1:
                    position = [index, much[0]]
                    if list(set_lis)[0] == next_player or list(set_lis)[1] == next_player:
                        break

    # If there is no best moves, it catches a random move.
    if not position:
        return easy_choice(m_cells, True)

    # Making some transformation to the real game matrix.
    if position[0] <= 2:
        position = str(position[1] + 1) + " " + str(3 - position[0])
    elif 2 < position[0] <= 5:
        position = str(position[0] - 2) + " " + str(3 - position[1])
    elif position[0] == 6:
        position = str(position[1] + 1) + " " + str(position[1] + 1)
    elif position[0] == 7:
        position = str(position[1] + 1) + " " + str(3 - position[1])

    return position
