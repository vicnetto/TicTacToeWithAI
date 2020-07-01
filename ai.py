import random
import global_variables as gv


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


def hard_choice(m_cells: list, player: bool) -> str:
    print('Making move level "hard"')

    player = "X" if player else "O"
    position = ""
    real_list = hard_recursion(m_cells, player, player)
    index = 0

    for numb, elements in enumerate(real_list):
        if max(real_list) == elements:
            index = numb
            break

    new_index = 0
    for i, lis in enumerate(m_cells):
        for j, char in enumerate(lis):
            if char == "_":
                if new_index != index:
                    new_index += 1
                else:
                    position = str(j + 1) + " " + str(3 - i)
                    break

        if position:
            break

    return position


def hard_recursion(new_board: list, player: str, my_player: str):
    state = next_play(new_board, is_hard=1)
    points = []

    if state == gv.DRAW:
        return 0
    elif state == gv.END:
        if player != my_player:
            return 10
        else:
            return -10

    for i, lis in enumerate(new_board):
        for j, char in enumerate(lis):
            if char == "_":
                new_board[i][j] = player

                result = hard_recursion(new_board, "X" if player == "O" else "O", my_player)
                if type(result) != int:
                    result = max(result) if player != my_player else min(result)
                points.append(result)

                new_board[i][j] = "_"

    return points


def next_play(m_cells: list, is_hard=0) -> bool:
    """ Make the real play

    This function basically makes all the play and see if a player won
    or lost.

    :param m_cells: The actual board, with all actual moves.
    :param row: Is the row position for the inserted value.
    :param column: Is the column position for the inserted value.
    :param next_player: Is the return of the who_is_next(...) function.
    :return: True if the game has ended, and False if the game is still
    happening.
    """

    # Setting the new position on the board.
    diag_sec, diag_prin = 0, 0

    for element in range(2, -1, -1):
        actual = m_cells[element][2 - element]
        actual_diag = m_cells[1][1] if m_cells[1][1] != "_" else "@"  # Symbolic value, just to differ.
        hor, ver = 0, 0

        for numb in range(0, 3):
            if actual == '_':  # Verify if has an empty space on the line, automatically ignoring this line.
                break
            if actual == m_cells[element][numb]:
                hor += 1
            if actual == m_cells[numb][2 - element]:
                ver += 1

        # Checking the two diagonals
        if actual_diag == m_cells[element][element]:
            diag_sec += 1
        if actual_diag == m_cells[element][2 - element]:
            diag_prin += 1

        actual = actual if diag_prin != 3 != diag_sec else actual_diag  # Printing the right character.
        if hor == 3 or ver == 3 or diag_prin == 3 or diag_sec == 3:
            if not is_hard:
                print(f"{actual} wins\n")

            return gv.END

        # If has no empty spaces on the board, the game is over.
        elif len([True for lis in m_cells for char in lis if char == '_']) == 0 and element == 0:
            if not is_hard:
                print("Draw\n")

            return gv.DRAW

    return gv.KEEP


def print_board(m_cells: list) -> None:
    """ Print the game board

    This function is used to print the board.

    :param m_cells: The actual board, with all actual moves
    :return: None
    """

    print("---------")

    for element in range(0, 3):
        print("|", end="")
        for numb in range(0, 3):
            if m_cells[element][numb] == "_":
                print("  ", end="")
            else:
                print(" " + m_cells[element][numb], end="")
        print(" |")

    print("---------")
