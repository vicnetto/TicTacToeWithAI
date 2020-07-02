import random
import global_variables as gv


def easy_choice(m_cells: list, is_medium=False) -> str:
    """ Make the bot movement in the EASY difficulty

        This function does the IA movement, randomly choosing two positions for the
        row and the column. Due to this, the IA does not make a smart play, it is
        only an random play.


    :param is_medium: This keyword argument is only changed when called
    by medium_choice function, only to don't print the easy phrase.
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
    """ Treat hard recursion

        This function is just to treat the hard_recursion() return, and return
        a string to make the move on the board.

    :param m_cells: The actual board, with all actual moves.
    :param player: What is the next player to make a move, "X" or "O".
    :return: The best move of the game, calculated by the minimax
    function (hard_recursion()).
    """

    print('Making move level "hard"')

    player = "X" if player else "O"
    position = ""
    # If it the first move of the board there is no need to calculate that.
    empty_cells = [True for lis in m_cells for elem in lis if elem == "_"]
    if len(empty_cells) == 9:
        return "1 3"
    # If isn't the first move, calls the minimax.
    real_list = hard_recursion(m_cells, player, player)
    index = 0

    # What is the index of the returned number.
    for numb, elements in enumerate(real_list):
        if max(real_list) == elements:
            index = numb
            break

    # Searching in all board free spaces where is the exactly index.
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
    """ Minimax function to find the best move on the board

        This function uses an AI method called minimax. Basically it consists
        on verifying all possible moves on the board, for the AI and the player,
        and sees what is the best play to make on all the possible plays. For
        this, the function uses recursion to pass in between all possible moves.

    :param new_board: Is the board with a new move, testing if is a good move.
    :param player: Is the next player to make the play.
    :param my_player: Is the player who called the game.
    :return: It returns an int when it reached the end. And return an list
    when the function has finished.
    """

    # Verify if it is an end game or a draw.
    state = next_play(new_board, is_hard=1)
    points = []

    # Returns the value calculated by next_play().
    if state == gv.DRAW:
        return 0
    elif state == gv.END:
        if player != my_player:
            return 10
        else:
            return -10

    # This runs for all available moves and calls the recursion again.
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
    :param is_hard:
    :return: True if the game has ended, and False if the game is still
    happening.
    """

    # Setting the new position on the board.
    draw = False
    ver_set = set()
    principal_set = set()
    secondary_set = set()

    for i, lis in enumerate(m_cells):
        hor_set = set(lis)
        secondary_set.add(lis[i])
        principal_set.add(lis[2 - i])

        if len(hor_set) == 1 and list(hor_set)[0] != "_":
            if not is_hard:
                print(f"{list(hor_set)[0]} wins\n")

            return gv.END

        for j, elem in enumerate(lis):
            if not draw:
                if elem == "_":
                   draw = True
            ver_set.add(m_cells[j][i])

        if len(ver_set) == 1 and list(ver_set)[0] != "_":
            if not is_hard:
                print(f"{list(ver_set)[0]} wins\n")

            return gv.END

        hor_set.clear()
        ver_set.clear()

    if not draw:
        if not is_hard:
            print("Draw\n")

        return gv.DRAW

    if len(principal_set) == 1 and list(principal_set)[0] != "_":
        if not is_hard:
            print(f"{list(principal_set)[0]} wins\n")

        return gv.END

    if len(secondary_set) == 1 and list(secondary_set)[0] != "_":
        if not is_hard:
            print(f"{list(principal_set)[0]} wins\n")

        return gv.END

    return gv.KEEP
