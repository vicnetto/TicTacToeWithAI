COLUMN = 0
ROW = 2


def print_board(m_cells: list) -> None:
    """ Print the game board

    This function is used to print the board."""

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


def do_verifications(m_cells: list, position: str, row: str, column: str) -> bool:
    """ Make all game verifications

        This functions is important for all game verifications on insertion,
        like if the cell is already used, if you inserted an alphabet and if
        the number is too big for the board. If the position is free, it will
        return True and if isn't will result False."""

    # Making the verification if the number is a real number, and the input is correct.
    if column.isnumeric() and position[1] == ' ' and row.isnumeric() and len(position) == 3:
        row, column = 2 - (int(row) - 1), int(column) - 1  # Correcting to the real matrix

        # Seeing if this value is valid.
        if 0 <= row <= 2 and 0 <= column <= 2:
            # Lastly, returning if the space is empty or occupied.
            if m_cells[row][column] == '_':
                return True
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")

    return False


def who_is_next(m_cells: list) -> bool:
    """What player should play next

       This function will return who will be the next one to play, the X
       or the O."""

    numb_x, numb_o = 0, 0
    str_cells = "".join(char for lis in m_cells for char in lis)  # Transforming the matrix to a str.

    for char in str_cells:
        if char == "X":
            numb_x += 1
        elif char == "O":
            numb_o += 1

    return True if numb_x == numb_o else False


def next_play(m_cells: list, row: int, column: int, next: bool) -> None:
    """ Make the real play

    This function basically makes all the play and see if a player won
    or lost."""

    m_cells[row][column] = "X" if next else "O"  # Setting the new position on the board.
    print_board(m_cells)
    hor, ver, diag = 0, 0, 0

    for element in range(2, -1, -1):
        actual = m_cells[element][2 - element]

        for numb in range(0, 3):
            if actual == '_':  # Verify if has an empty space on the line, automatically ignoring this line.
                break
            if actual == m_cells[element][numb]:
                hor += 1
            if actual == m_cells[numb][element]:
                ver += 1

        if m_cells[1][1] != "_":
            # Checking the two diagonals
            if m_cells[2][0] == m_cells[1][1] == m_cells[0][2] or m_cells[0][0] == m_cells[1][1] == m_cells[2][2]:
                actual = m_cells[1][1]
                diag += 3

        if hor == 3 or ver == 3 or diag == 3:
            print(f"{actual} wins")
            break
        elif len([True for lis in m_cells for char in lis if
                  char == '_']) == 0:  # If has no empty spaces on the board, the game is over.
            print("Draw")
            break
        elif element == 0:
            print("Game not finished")
            break

        hor, ver, diag = 0, 0, 0


if __name__ == "__main__":
    cells = str(input("Enter cells: > "))
    m_cells = ([[cells[index] for index in range(limit * 3, (limit * 3) + 3)]
            for limit in range(0, 3)])  # Transform the string in a matrix.

    print_board(m_cells)

    while True:
        print("Enter the coordinates: > ", end="")
        position = str(input())

        row = position[ROW]
        column = position[COLUMN]
        next = do_verifications(m_cells, position, row, column)  # Passing the input.

        if next:
            row, column = 2 - (int(row) - 1), int(column) - 1  # Correcting to the real matrix.
            next_play(m_cells, row, column, who_is_next(m_cells))
