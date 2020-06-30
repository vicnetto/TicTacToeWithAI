import global_variables as gv
from ai import easy_choice, medium_choice


def basic_mode(player_one: int, player_two: int) -> None:
    """ Initial game function

    This function basically runs calls all the functions. In the start, it
    receives the initial statement of the board. After that, it reads the
    wanted position and verifies if is a valid one, inserting the play and
    possibly ending the game.

    :param player_one: This parameter is the type of the "X" player, if is
    a player it contains gv.PLAYER, if is an easy bot it contains gv.EASY.
    :param player_two: This one is the same of "player_one", but is the "O"
    player, or second player.
    :return: None
    """

    m_cells = [["_" for __ in range(3)] for _ in range(3)]  # Making the default list.

    print_board(m_cells)

    while True:
        next_player = who_is_next(m_cells)

        if next_player:  # Making a big verification what is the type of the player, to call the right function.
            position = (catch_movement() if player_one == gv.USER else easy_choice(m_cells) if player_one == gv.EASY
                        else medium_choice(m_cells, who_is_next(m_cells)))
        else:
            position = (catch_movement() if player_two == gv.USER else easy_choice(m_cells) if player_two == gv.EASY
                        else medium_choice(m_cells, who_is_next(m_cells)))

        value = do_verifications(m_cells, position)  # If this value returns true, it is time to end the game.

        if value:
            break


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


def catch_movement() -> str:
    """ Catch the next player move

    This function is only for organization. This basically gets the user
    input, transforming it to a string and returning what is the move, for
    the program do some verifications with the position.

    :return: It return the string with the user movement.
    """

    print("Enter the coordinates: > ", end="")
    position = str(input())

    return position


def do_verifications(m_cells: list, position: str) -> bool:
    """ Make all game verifications

    This functions is important for all game verifications on insertion,
    like if the cell is already used, if you inserted an alphabet and if
    the number is too big for the board. If the position is free, it will
    return True and if isn't will result False.

    :param m_cells: The actual board, with all actual moves.
    :param position: Is the current move.
    :return: True if the game has ended, or False if the input is
    wrong or the game is still running.
    """
    end_game = False

    # Making the verification if the number is a real number, and the input is correct.
    if len(position) == 3 and position[gv.COLUMN].isnumeric() and position[1] == ' ' and position[gv.ROW].isnumeric():
        row, column = 2 - (int(position[gv.ROW]) - 1), int(position[gv.COLUMN]) - 1  # Correcting to the real matrix

        # Seeing if this value is valid.
        if 0 <= row <= 2 and 0 <= column <= 2:
            # Lastly, returning if the space is empty or occupied.
            if m_cells[row][column] == '_':
                m_cells[row][column] = "X" if who_is_next(m_cells) else "O"
                print_board(m_cells)
                end_game = next_play(m_cells, row, column, who_is_next(m_cells))
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")

    return True if end_game else False


def who_is_next(m_cells: list) -> bool:
    """ What player should play next

    This function will return who will be the next one to play, the X
    or the O.

    :param m_cells: The actual board, with all actual moves.
    :return: True if the next player is "X", or False to "O".
    """

    numb_x, numb_o = 0, 0
    str_cells = "".join(char for lis in m_cells for char in lis)  # Transforming the matrix to a str.

    for char in str_cells:
        if char == "X":
            numb_x += 1
        elif char == "O":
            numb_o += 1

    return True if numb_x == numb_o else False


def next_play(m_cells: list, row: int, column: int, next_player: bool) -> bool:
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
            print(f"{actual} wins\n")
            return True

        # If has no empty spaces on the board, the game is over.
        elif len([True for lis in m_cells for char in lis if char == '_']) == 0 and element == 0:
            print("Draw\n")
            return True

    return False

