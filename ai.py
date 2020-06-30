import random


def easy_choice(m_cells: list, is_medium=False) -> str:
    """ Make the bot movement in the EASY difficulty

        This function does the IA movement, randomly choosing two positions for the
        row and the column. Due to this, the IA does not make a smart play, it is
        only an random play.


    :param is_medium:
    :param m_cells: The actual board, with all actual moves.
    :return: True if the game has ended or False if the game is still
    happening.
    """

    if is_medium == 0:
        print('Making move level "easy"')

    out, end_game = True, False
    random.seed()

    while out:
        row = random.randint(0, 2)
        column = random.randint(0, 2)

        if m_cells[2 - row][column] == "_":
            return str(column + 1) + " " + str(row + 1)


def medium_choice(m_cells: list, next_player: bool) -> str:
    print('Making move level "medium"')

    next_player = "X" if next_player else "O"
    position = ""

    hor_lists = [[value for value in lis] for lis in m_cells]
    ver_lists = [[m_cells[row][column] for row in range(0, 3)] for column in range(0, 3)]
    principal_list = [m_cells[2 - numb][numb] for numb in range(0, 3)]
    secondary_list = [m_cells[numb][numb] for numb in range(0, 3)]
    all_in_one_list = ([hor_lists[0]] + [hor_lists[1]] + [hor_lists[2]] + [ver_lists[0]] + [ver_lists[1]] +
                       [ver_lists[2]] + [principal_list] + [secondary_list])

    for index, lis in enumerate(all_in_one_list):
        set_lis = set(lis)
        if len(set_lis) == 2:
            if list(set_lis)[0] == "_" or list(set_lis)[1] == "_":
                much = [i for i, char in enumerate(all_in_one_list[index]) if char == "_"]
                if len(much) == 1:
                    position = [index, much[0]]
                    if list(set_lis)[0] == next_player or list(set_lis)[1] == next_player:
                        break

    if not position:
        return easy_choice(m_cells, True)

    if position[0] <= 2:
        position = str(position[1] + 1) + " " + str(3 - position[0])
    elif 2 < position[0] <= 5:
        position = str(position[0] - 2) + " " + str(3 - position[1])
    elif position[0] == 6:
        position = str(position[1] + 1) + " " + str(position[1] + 1)
    elif position[0] == 7:
        position = str(position[1] + 1) + " " + str(3 - position[1])

    return position
